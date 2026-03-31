from contextlib import asynccontextmanager
import aiosqlite
import logging
from typing import AsyncIterator
from pathlib import Path

from core.config import DB_PATH

logger = logging.getLogger(__name__)

_DB_PATH = DB_PATH / 'database.db'
_is_db_init = False

@asynccontextmanager
async def get_db(path: str | Path = _DB_PATH) -> AsyncIterator[aiosqlite.Connection]:
    global _is_db_init
    async with aiosqlite.connect(path) as db:
        # 啟用 WAL 模式，讓讀寫不互相阻塞
        await db.execute("PRAGMA journal_mode=WAL")
        await db.execute("PRAGMA busy_timeout=10000")  # 等鎖 10 秒
        db.row_factory = aiosqlite.Row

        # init db
        if not _is_db_init:
            await create_tables()
            _is_db_init = True

        yield db

async def create_tables():
    global _is_db_init

    if _is_db_init:
        return
    
    _is_db_init = True


    try:
        async with get_db() as db:
            await db.execute("""
                CREATE TABLE IF NOT EXISTS metas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    list_name TEXT NOT NULL,         
                    list_played_times INTEGER DEFAULT 0,
                    list_last_played_at TEXT,
                    list_created_at TEXT,
                    loop_status TEXT DEFAULT 'none',
                    type TEXT,
                    UNIQUE(user_id, list_name, type)
                )
            """)
            
            await db.execute("""
                CREATE TABLE IF NOT EXISTS custom_play_list (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    list_name TEXT NOT NULL,
                    video_url TEXT NOT NULL,
                    title TEXT NOT NULL,
                    duration_int INTEGER NOT NULL,
                    thumbnail_url TEXT NOT NULL,
                    created_at TEXT,
                    UNIQUE(user_id, list_name, video_url)
                )
            """)
            
            await db.execute("""
                CREATE TABLE IF NOT EXISTS temp_urls (
                    video_id TEXT PRIMARY KEY,
                    title TEXT,
                    video_url TEXT,
                    audio_url TEXT,
                    thumbnail_url TEXT,
                    duration TEXT,
                    duration_int INTEGER,
                    cached_at TEXT DEFAULT (datetime('now'))
                )
            """)

            await db.execute("""
                CREATE TABLE IF NOT EXISTS prefer_loop (
                    user_id TEXT PRIMARY KEY,
                    loop TEXT
                )""")
            
            await db.commit()

    except:
        logger.error('Error while creating tables.', exc_info=True)