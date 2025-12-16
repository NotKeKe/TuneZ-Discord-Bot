## 📢 指令呼叫方式
- 使用 TuneZ 的前綴: `$` 來呼叫指令
- 使用 Discord 內建的 slash command (`/`)

## 📜 指令們
將會用以下格式說明:  
`/指令名稱 [參數]` (其他調用指令的方法) ─ 變數名稱+說明 ─ 該指令的功能
### 🎵 音樂播放
- `/播放 [query]` ($play, $p) ─ query: 連結或關鍵字 ─ 歌曲正在播放時，也可以使用 /播放 而不用 /新增
- `/新增 [query]` ($add) ─ query: 連結或關鍵字
- `/跳過` ($skip, $s) ─ 跳過歌曲
- `/上一首` ($back) ─ 跳回上一首歌
- `/暫停` ($pause, $ps) ─ 暫停歌曲
- `/繼續` ($resume, $rs) ─ 繼續播放歌曲
- `/停止播放並離開頻道` ($stop)
- `/循環 [loop_type]` ($loop) ─ loop_type: 循環狀態，可為 None、single、list (不循環播放、單曲循環、播放清單循環) ─ 設定循環播放模式
- `/正在播放` ($nowplaying, $np, $now) ─ 顯示正在播放的歌曲
- `/播放清單` ($queue) ─ 顯示當前的播放清單
- `/移除播放清單中的歌曲 [number]` ($remove, $rm) ─ number: 第幾首歌
- `/清除播放清單` ($clear, $cq) ─ 清除播放清單中的所有歌曲，輸入指令後要點擊 ✅ 才會刪除
- `/離開` ($leave) ─ 等同於 `/停止播放並離開頻道`
- `/調整音量 [volume]` ($volume) ─ volume: 可填可不填，不填的話可以用按鈕調音量
### 📝 自定義播放清單
- `/播放自訂播放清單 [list_name]` ($play_custom_list) ─ list_name: 播放清單名稱，沒設定過的話會是空白的
- `/加入自訂播放清單 [url] [list_name]` ($add_custom_list) ─ url: 要加入播放清單的歌曲連結。 list_name: 播放清單名稱，如果要新創建播放清單，直接打名字就好不用選。 ─ 將歌曲加入播放清單
- `/刪除自訂播放清單 [list_name]` ($delete_custom_list, $del_custom_list) ─ list_name: 選擇要刪除播放清單的名稱
- `/列出自訂播放清單的歌曲 [list_name]` ($show_custom_list) ─ 顯示單一播放清單的歌曲列表
### 🛠️ 表情符號管理
- `/emoji [name]` ($emoji) ─ name: emoji 的名稱，例如: next, stop, refresh ─ 顯示 TuneZ 內建的表情符號
- `/reload_emoji [type]` ($reload_emoji) ─ type: all, default, custom，分別表示重載 全部、預設(TuneZ的預設)、自定義表情符號
    - 有關自定義表情符號，請詳閱[該文檔](https://github.com/NotKeKe/TuneZ-Discord-Bot)的**特色**部分