import pytest
import pytest_asyncio
import asyncio
import tempfile
import os
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, PropertyMock
from datetime import datetime, timedelta, timezone

# 測試用的假 DB 路徑工廠
_temp_db_paths = []

def get_test_db_path():
    """建立一個唯一的測試資料庫路徑"""
    fd, path = tempfile.mkstemp(suffix='.db', prefix='test_music_bot_')
    os.close(fd)
    _temp_db_paths.append(path)
    return Path(path)

@pytest.fixture(scope='session')
def event_loop():
    """建立 session 等級的 event loop"""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest_asyncio.fixture
async def test_db_path():
    """每個測試使用獨立的臨時資料庫"""
    path = get_test_db_path()
    yield path
    # 清理：測試結束後刪除檔案
    if path.exists():
        try:
            path.unlink()
        except PermissionError:
            # Windows 有時需要等一下才能刪除
            import time
            time.sleep(0.1)
            try:
                path.unlink()
            except:
                pass

@pytest_asyncio.fixture
async def setup_test_database(test_db_path):
    """建立測試資料表並填充測試資料"""
    import aiosqlite
    
    async with aiosqlite.connect(test_db_path) as db:
        # 建立 metas 資料表
        await db.execute("""
            CREATE TABLE IF NOT EXISTS metas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                list_name TEXT NOT NULL,
                list_last_played_at TEXT,
                list_played_times INTEGER DEFAULT 0,
                loop_status TEXT DEFAULT 'none',
                type TEXT DEFAULT 'custom_play_list',
                UNIQUE(user_id, list_name)
            )
        """)
        
        # 建立 custom_play_list 資料表
        await db.execute("""
            CREATE TABLE IF NOT EXISTS custom_play_list (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                list_name TEXT NOT NULL,
                video_url TEXT NOT NULL,
                title TEXT,
                UNIQUE(user_id, list_name, video_url)
            )
        """)
        
        await db.commit()
    
    yield test_db_path
    
    # teardown: 清理資料庫（這裡已經在 test_db_path fixture 處理）

@pytest_asyncio.fixture
async def populated_database(setup_test_database):
    """填充測試資料的資料庫"""
    import aiosqlite
    
    user_id = "123456789"
    base_time = datetime(2024, 1, 15, 12, 0, 0, tzinfo=timezone.utc)
    
    test_data = [
        # (user_id, list_name, last_played_at, play_times)
        (user_id, "My Favorites", (base_time - timedelta(days=1)).isoformat(), 10),
        (user_id, "Workout Mix", (base_time - timedelta(days=5)).isoformat(), 5),
        (user_id, "Chill Vibes", base_time.isoformat(), 20),
        (user_id, "Coding Playlist", "", 3),  # 空的 last_played_at
        (user_id, "測試播放列表", (base_time - timedelta(days=2)).isoformat(), 8),
        # 另一個用戶的資料（不應該被查到）
        ("999999999", "Other User List", base_time.isoformat(), 100),
    ]
    
    async with aiosqlite.connect(setup_test_database) as db:
        for uid, name, last_played, times in test_data:
            await db.execute("""
                INSERT INTO metas (user_id, list_name, list_last_played_at, type, list_played_times)
                VALUES (?, ?, ?, 'custom_play_list', ?)
                ON CONFLICT(user_id, list_name) DO UPDATE SET
                    list_last_played_at = excluded.list_last_played_at,
                    list_played_times = excluded.list_played_times
            """, (uid, name, last_played, times))
        await db.commit()
    
    return setup_test_database, user_id

@pytest.fixture
def mock_interaction(populated_database):
    """Mock Discord Interaction 物件"""
    db_path, user_id = populated_database
    
    mock_inter = MagicMock()
    mock_inter.user.id = user_id  # 測試用戶 ID
    mock_inter.user.display_name = "TestUser"
    
    return mock_inter, db_path

@pytest.fixture
def mock_interaction_other_user():
    """另一個用戶的 Mock Discord Interaction（不依賴 populated_database，由測試自行處理）"""
    mock_inter = MagicMock()
    mock_inter.user.id = "999999999"  # 另一個用戶 ID
    mock_inter.user.display_name = "OtherUser"
    
    return mock_inter
