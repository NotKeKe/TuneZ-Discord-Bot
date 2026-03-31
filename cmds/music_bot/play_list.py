from datetime import datetime, timezone
import yt_dlp
import asyncio
from discord.ext import commands
from concurrent.futures import ProcessPoolExecutor
import uuid

from .utils import convert_to_short_url, is_url, QUEUE
from .player import Player, loop_option

from core.sql import get_db

def _get_url_title(url: str) -> dict:
    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        info = ydl.extract_info(url, download=False)
        return {
            'title': info['title'], # type: ignore
            'duration': info['duration'], # type: ignore 原本就是 int
            'thumbnail': info['thumbnail'], # type: ignore
        }

async def get_url_title(short_url: str):
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as executor:
        result: dict = await loop.run_in_executor(executor, _get_url_title, short_url)

    return result

async def add_to_custom_list(url: str, list_name: str, user_id: int) -> str | bool:
    """將使用者指定的連結，加入 MongoDB 當中

    Returns:
        str: True | 'Invaild url'
    """    
    if not is_url(url): return 'Invaild url'
    short_url = convert_to_short_url(url)
    if not short_url: return 'Cannot convert your url to "https://youtu.be/..."'

    async with get_db() as db:
        # add to metas
        cursor = await db.execute(
            'SELECT * FROM metas '
            'WHERE type="custom_play_list" and user_id=? and list_name=?'
            'LIMIT 1',
            (user_id, list_name)
        )

        if (await cursor.fetchone()) is None:
            await db.execute(
                'INSERT INTO metas (type, user_id, list_name, list_played_times, list_created_at, list_last_played_at) '
                'VALUES (?, ?, ?, ?, ?, ?)',
                ('custom_play_list', user_id, list_name, 0, datetime.now(timezone.utc).isoformat(), '')
            )
            await db.commit()

        # add to custom_play_list
        cursor = await db.execute(
            'SELECT * FROM custom_play_list '
            'WHERE user_id=? and list_name=? and video_url=?'
            'LIMIT 1',
            (user_id, list_name, short_url)
        )

        if (await cursor.fetchone()) is None:
            # 取得影片資訊
            task_id = str(uuid.uuid4())
            await QUEUE.add_task(task_id, 1, get_url_title(short_url))
            result = await QUEUE.get_result(task_id)

            title = result['title']
            duration = result['duration']
            thumbnail = result['thumbnail']

            # 加到 db
            await db.execute(
                'INSERT INTO custom_play_list (user_id, list_name, video_url, created_at, title, duration_int, thumbnail_url) '
                'VALUES (?, ?, ?, ?, ?, ?, ?)',
                (user_id, list_name, short_url, datetime.now(timezone.utc).isoformat(), title, duration, thumbnail)
            )
            await db.commit()

        return True

async def del_custom_list(list_name: str, user_id: int):
    async with get_db() as db:
        await db.execute(
            'DELETE FROM metas '
            'WHERE user_id=? and list_name=? and type="custom_play_list"',
            (user_id, list_name)
        )

        await db.execute(
            'DELETE FROM custom_play_list '
            'WHERE user_id=? and list_name=?',
            (user_id, list_name)
        )

        await db.commit()

async def get_custom_list(list_name: str, user_id: int) -> list[tuple[str, str]]:
    async with get_db() as db:
        cursor = await db.execute(
            'SELECT * FROM custom_play_list '
            'WHERE user_id=? and list_name=? '
            'ORDER BY created_at ASC', # 由遠到近
            (user_id, list_name)
        )

        datas = await cursor.fetchall()

        return [(item['title'], item['video_url']) for item in datas]
    
async def remove_one_from_custom_list(list_name: str, index: int, user_id: int):
    """
    Async generator for removing one song from custom list.
    
    Yield 1: {'title': ..., 'video_url': ...} - song info for confirmation
    Yield 2: True - deletion confirmed
    """
    async with get_db() as db:
        cursor = await db.execute(
            'SELECT id, video_url, title FROM custom_play_list '
            'WHERE user_id=? and list_name=? '
            'ORDER BY created_at ASC',
            (user_id, list_name)
        )

        datas = await cursor.fetchall()
        datas = list(datas)

        if not datas:
            yield 'List is empty'
            return

        if index < 1 or index > len(datas):
            yield f'Index: `{index}` out of range (1-{len(datas)})'
            return

        data = datas[index - 1]  # user sees 1-based index
        data = dict(data)
        
        # 第一次 yield：回傳歌曲資訊用於確認
        yield {'title': data['title'], 'video_url': data['video_url'], 'id': data['id']}

        # 第二次 yield：執行刪除
        await db.execute(
            'DELETE FROM custom_play_list WHERE id=?',
            (data['id'],)
        )
        await db.commit()
        yield True


class CustomListPlayer:
    '''這個類主要用於將 custom_play_list 的歌曲 加進 Player 物件當中'''
    def __init__(self, ctx: commands.Context, list_name: str):
        self.user_id = ctx.author.id
        self.player = Player(ctx)
        self.ctx = ctx
        self.list_name = list_name

        self.songs: list[str] = [] # list[url]

        self.playlist_load_task: asyncio.Task | None = None

    def __del__(self):
        try:
            if self.playlist_load_task:
                self.playlist_load_task.cancel()
                del self.playlist_load_task
        except:
            ...
    
    async def load_songs(self):
        async with get_db() as db:
            cursor = await db.execute(
                'SELECT * FROM custom_play_list '
                'WHERE user_id=? and list_name=? '
                'ORDER BY created_at ASC',
                (self.user_id, self.list_name)
            )

            async for song in cursor:
                self.songs.append(song['video_url'])

            # 順便修改 metas 的 list_last_played_at

            # 更新
            await db.execute("""
                INSERT INTO metas (type, user_id, list_name, list_played_times, list_created_at, list_last_played_at)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT (user_id, type, list_name) DO UPDATE SET
                    list_last_played_at = excluded.list_last_played_at,
                    list_played_times = metas.list_played_times + 1
                """,
                ('custom_play_list', self.user_id, self.list_name, 0, datetime.now(timezone.utc).isoformat(), '')
            )
            await db.commit()

            # 查詢最新資訊
            cursor = await db.execute(
                'SELECT * FROM metas '
                'WHERE user_id=? and type=? and list_name=?',
                (self.user_id, 'custom_play_list', self.list_name)
            )
            new_doc = await cursor.fetchone()
            if not new_doc: raise
            self.new_doc = dict(new_doc)

    async def add_songs_to_player(self):
        # 先讓兩首歌出去後，剩下的歌用背景任務的方式新增，避免使用者等待過久
        await self.player.add(self.songs[0], self.ctx)
        if len(self.songs) > 1:
            await self.player.add(self.songs[1], self.ctx)
        
        if len(self.songs) > 2:
            async def task():
                for song in self.songs[2:]:
                    await self.player.add(song, self.ctx, 2)

            asyncio.create_task(task())

    def change_loop_status(self):
        self.player.loop(self.new_doc.get('loop_status') or 'None')

    def cover_functions(self):
        # cover turn_loop function
        _filter = {'user_id': self.user_id, 'type': 'custom_play_list', 'list_name': self.list_name}
        def turn_loop(self: Player):
            index = loop_option.index(self.loop_status)
            index = (index + 1) % len(loop_option)
            self.loop_status = loop_option[index]

            async def change_to_metas():
                async with get_db() as db:
                    await db.execute(
                        "INSERT INTO metas (user_id, type, list_name, loop_status) VALUES (?, ?, ?, ?) "
                        "ON CONFLICT (user_id, type, list_name) "
                        "DO UPDATE SET loop_status = excluded.loop_status",
                        (_filter['user_id'], _filter['type'], _filter['list_name'], self.loop_status)
                    )
                    await db.commit()

            asyncio.create_task(change_to_metas())

        self.player.turn_loop = turn_loop.__get__(self.player) # what is this um

    async def run(self) -> Player:
        await self.load_songs()
        await self.add_songs_to_player()
        self.change_loop_status()
        self.cover_functions()
        return self.player