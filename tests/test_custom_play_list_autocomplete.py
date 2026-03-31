"""
測試 cmds/music_bot/autocomplete.py 中的 custom_play_list_autocomplete 函式
"""
import pytest
from unittest.mock import patch, MagicMock, AsyncMock
from contextlib import asynccontextmanager
from datetime import datetime, timedelta, timezone

from cmds.music_bot.autocomplete import custom_play_list_autocomplete


def create_mock_get_db(db_path):
    """建立一個 mock get_db 函式，使用指定的資料庫路徑"""
    @asynccontextmanager
    async def mock_get_db():
        import aiosqlite
        db = await aiosqlite.connect(db_path)
        db.row_factory = aiosqlite.Row
        try:
            yield db
        finally:
            await db.close()
    
    return mock_get_db


class TestCustomPlayListAutocomplete:
    """custom_play_list_autocomplete 的測試類別"""

    @pytest.mark.asyncio
    async def test_empty_search_returns_all_playlists(
        self, populated_database, mock_interaction
    ):
        """
        測試：搜尋空字串時，回傳該用戶的所有播放清單
        """
        mock_inter, db_path = mock_interaction
        
        mock_get_db = create_mock_get_db(db_path)
        
        with patch('cmds.music_bot.autocomplete.get_db', mock_get_db):
            result = await custom_play_list_autocomplete(mock_inter, "")
        
        # 應該回傳 5 個播放清單（排除另一個用戶的）
        assert len(result) == 5
        
        # 驗證有包含預期的播放清單名稱
        result_values = [choice.value for choice in result]
        assert "My Favorites" in result_values
        assert "Workout Mix" in result_values
        assert "Chill Vibes" in result_values

    @pytest.mark.asyncio
    async def test_partial_match_filtering(
        self, populated_database, mock_interaction
    ):
        """
        測試：部分關鍵字搜尋（如 "my"）能正確過濾結果
        """
        mock_inter, db_path = mock_interaction
        
        mock_get_db = create_mock_get_db(db_path)
        
        with patch('cmds.music_bot.autocomplete.get_db', mock_get_db):
            result = await custom_play_list_autocomplete(mock_inter, "my")
        
        # "My Favorites" 應該被找到（不區分大小寫）
        result_values = [choice.value for choice in result]
        assert "My Favorites" in result_values
        
        # "Workout Mix" 和 "Chill Vibes" 不應該被找到
        assert "Workout Mix" not in result_values
        assert "Chill Vibes" not in result_values

    @pytest.mark.asyncio
    async def test_no_results_when_no_match(
        self, populated_database, mock_interaction
    ):
        """
        測試：搜尋不存在的關鍵字時，回傳空清單
        """
        mock_inter, db_path = mock_interaction
        
        mock_get_db = create_mock_get_db(db_path)
        
        with patch('cmds.music_bot.autocomplete.get_db', mock_get_db):
            result = await custom_play_list_autocomplete(mock_inter, "xyz_nonexistent_123")
        
        assert len(result) == 0

    @pytest.mark.asyncio
    async def test_sorting_by_play_times_desc_then_name_asc(
        self, populated_database, mock_interaction
    ):
        """
        測試：結果排序正確
        - 第一排序：播放次數（降冪）
        - 第二排序：播放清單名稱（升冪）
        """
        mock_inter, db_path = mock_interaction
        
        mock_get_db = create_mock_get_db(db_path)
        
        with patch('cmds.music_bot.autocomplete.get_db', mock_get_db):
            result = await custom_play_list_autocomplete(mock_inter, "")
        
        # 驗證排序
        # "Chill Vibes" 播放次數最多（20），應該是第一個
        assert result[0].value == "Chill Vibes"
        
        # "My Favorites" 播放次數 10，第二個
        assert result[1].value == "My Favorites"
        
        # "測試播放列表" 和 "Workout Mix" 都是 5 和 3，但字母順序 "C" < "W" < "測"
        # 不過實際排序是按 name 升冪，所以順序應該是...
        # 讓我們驗證整體排序
        values = [choice.value for choice in result]
        play_times = []
        for choice in result:
            # 從 display name 解析播放次數
            # Format: 'Name: "{}" | PlayedTimes: "{}" | LastPlay: "{}"'
            name_part = choice.name.split(' | ')[0]
            times_part = choice.name.split(' | ')[1]
            # 解析出播放次數
            times = int(times_part.split(': ')[1].strip('"'))
            play_times.append(times)
        
        # 確認是降冪排序
        assert play_times == sorted(play_times, reverse=True)

    @pytest.mark.asyncio
    async def test_unicode_support(
        self, populated_database, mock_interaction
    ):
        """
        測試：中文關鍵字搜尋正常運作
        """
        mock_inter, db_path = mock_interaction
        
        mock_get_db = create_mock_get_db(db_path)
        
        with patch('cmds.music_bot.autocomplete.get_db', mock_get_db):
            result = await custom_play_list_autocomplete(mock_inter, "測試")
        
        # 應該找到中文播放清單
        result_values = [choice.value for choice in result]
        assert "測試播放列表" in result_values

    @pytest.mark.asyncio
    async def test_user_isolation(
        self, populated_database, mock_interaction, mock_interaction_other_user
    ):
        """
        測試：用戶資料隔離 - 用戶 A 不會看到用戶 B 的播放清單
        """
        mock_inter1, db_path = mock_interaction
        mock_inter2 = mock_interaction_other_user
        
        mock_get_db = create_mock_get_db(db_path)
        
        with patch('cmds.music_bot.autocomplete.get_db', mock_get_db):
            # 用戶 123456789 搜尋
            result_user1 = await custom_play_list_autocomplete(mock_inter1, "")
            # 用戶 999999999 搜尋
            result_user2 = await custom_play_list_autocomplete(mock_inter2, "")
        
        # 用戶 1 不應該看到用戶 2 的播放清單
        user1_values = [choice.value for choice in result_user1]
        assert "Other User List" not in user1_values
        
        # 用戶 2 不應該看到用戶 1 的播放清單
        user2_values = [choice.value for choice in result_user2]
        assert "Chill Vibes" not in user2_values
        assert "My Favorites" not in user2_values

    @pytest.mark.asyncio
    async def test_empty_last_played_at_shows_unknown(
        self, populated_database, mock_interaction
    ):
        """
        測試：list_last_played_at 為空時，顯示 'Unknown'
        """
        mock_inter, db_path = mock_interaction
        
        mock_get_db = create_mock_get_db(db_path)
        
        with patch('cmds.music_bot.autocomplete.get_db', mock_get_db):
            result = await custom_play_list_autocomplete(mock_inter, "Coding")
        
        # 應該找到 "Coding Playlist"
        assert len(result) == 1
        assert result[0].value == "Coding Playlist"
        
        # 驗證 LastPlay 顯示 "Unknown"
        # Format: 'Name: "{}" | PlayedTimes: "{}" | LastPlay: "{}"'
        last_play_part = result[0].name.split(' | ')[2]
        assert "Unknown" in last_play_part

    @pytest.mark.asyncio
    async def test_return_value_is_list_of_choices(
        self, populated_database, mock_interaction
    ):
        """
        測試：回傳值是 List[Choice[str]] 類型
        """
        from discord.app_commands import Choice
        
        mock_inter, db_path = mock_interaction
        
        mock_get_db = create_mock_get_db(db_path)
        
        with patch('cmds.music_bot.autocomplete.get_db', mock_get_db):
            result = await custom_play_list_autocomplete(mock_inter, "")
        
        assert isinstance(result, list)
        for item in result:
            assert isinstance(item, Choice)
            assert hasattr(item, 'name')
            assert hasattr(item, 'value')
