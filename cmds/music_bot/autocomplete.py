from discord import Interaction
from discord.app_commands import Choice
from typing import List
from datetime import datetime, timedelta, timezone

from core.utils import redis_client
from core.sql import get_db

async def custom_play_list_autocomplete(inter: Interaction, curr: str) -> List[Choice[str]]:
    query = (
        'SELECT list_name, list_played_times, list_last_played_at FROM metas '
        'WHERE type="custom_play_list" and user_id=? '
        'and list_name LIKE ? COLLATE NOCASE '
        'LIMIT 25'
    )

    results = []

    async with get_db() as db:
        cursor = await db.execute(query, (inter.user.id, f"%{curr}%"))
        async for meta in cursor:
            name = meta['list_name']
            play_times = meta['list_played_times']
            last_play_utc_str = meta["list_last_played_at"]
            if last_play_utc_str != '':
                last_play_utc = datetime.fromisoformat(last_play_utc_str) # utc 0
                last_play_utc8 = last_play_utc.astimezone(timezone(timedelta(hours=8))) # 轉為 utc+8
                last_play = last_play_utc8.strftime('%Y/%m/%d %H:%M:%S %A')
            else:
                last_play = 'Unknown'

            results.append((
                name, # str
                play_times, # int
                last_play # str
            ))

    results.sort(key=lambda x: (-x[1], x[0]))

    format_template = 'Name: "{}" | PlayedTimes: "{}" | LastPlay: "{}"'

    return [
        Choice(name=format_template.format(name, play_time, last_play), value=name) 
        for name, play_time, last_play in results
    ] # 給使用者顯示的, list_name

async def play_query_autocomplete(inter: Interaction, curr: str) -> List[Choice[str]]:
    '''曾經在 play or add 中使用的 query，最多 10 項'''
    key = f'musics_query:{inter.user.id}'
    results = await redis_client.lrange(key, 0, 9) # type: ignore
    await redis_client.expire(key, 60*60*24*30) # 約一個月

    if curr:
        results = [result for result in results if curr.lower().strip() in result.lower().strip()]

    return [Choice(name=result, value=result) for result in results]