---
layout: default
title: 常見問題
lang: zh-TW
permalink: /zh-TW/faq/
breadcrumb:
  - title: 主頁
    url: /zh-TW/
  - title: 常見問題
    url: /zh-TW/faq/
---

# 常見問題

關於 TuneZ 的常見問題和解答。

---

## ❓ 基本問題

### 什麼是 TuneZ？

TuneZ 是一個基於 Python 的 Discord 音樂機器人，可以讓您在 Discord 語音頻道中播放 YouTube 音樂。它具有播放清單管理、循環模式和自訂播放清單等功能，開箱即用。

### TuneZ 與其他音樂機器人有什麼不同？

- **開箱即用**：最少設定即可運作
- **自架主機**：您可以控制自己的機器人和資料
- **自訂表情符號**：內建精美的動畫表情符號，可自由定制
- **多語言支援**：支援英文、繁體中文和簡體中文

### 使用 TuneZ 需要付費嗎？

不需要，TuneZ 完全免費且開源，採用 Apache License 2.0 授權。

---

## 🔧 安裝與設定

### 執行 TuneZ 需要什麼？

- Discord Bot Token（可從 Discord 開發者入口網站取得），具體參考[註冊 Discord Bot]({{ '/zh-TW/register-discord-bot/' | relative_url }})
- 以下任一環境：
  - Windows 電腦（使用 .exe）
  - 已安裝 Docker（使用 Docker）
  - Python 3.10+（使用 uv）

### 我沒有 Discord Bot Token，要如何取得？

1. 前往 [Discord 開發者入口網站](https://discord.com/developers/applications)
2. 點擊「New Application」並命名
3. 在左側邊欄點擊「Bot」
4. 點擊「Add Bot」並確認
5. 複製您的 Token（如需重置，點擊「Reset Token」）
6. 在「Privileged Gateway Intents」下啟用：
   - PRESENCE INTENT
   - SERVER MEMBERS INTENT
   - MESSAGE CONTENT INTENT

詳細請參閱[註冊 Discord Bot]({{ '/zh-TW/register-discord-bot/' | relative_url }})

### 為什麼需要啟用 intents？

Discord 要求機器人啟用特定 intents 才能存取某些功能。TuneZ 需要：
- **Presence Intent**：偵測使用者加入/離開語音頻道
- **Server Members Intent**：用於成員相關功能
- **Message Content Intent**：讀取指令訊息（前綴指令）

---

## 🎵 音樂播放

### 為什麼音樂無法播放？

檢查以下常見問題：

1. **不在語音頻道中**：您必須在語音頻道中才能使用音樂指令
2. **機器人不在語音頻道**：機器人需要連接和說話的權限
3. **無效的網址**：請確認 YouTube 網址正確且可存取
4. **內容被封鎖**：某些影片可能受到地區限制或已被移除

### 為什麼音訊品質不佳？

這可能是因為：
- 網路連線緩慢
- YouTube 伺服器問題
- 機器人負載過高

### 可以播放 YouTube 播放清單嗎？

可以！使用 `/play` 或 `/add` 時，您可以貼上 YouTube 播放清單網址。

### TuneZ 支援 Spotify/Apple Music 嗎？

目前 TuneZ 僅直接支援 YouTube。但是您可以：
- 找到歌曲的 YouTube 連結
- 使用 YouTube 網址建立自訂播放清單

---

## 🔁 循環與播放清單

### 循環模式有什麼不同？

| 模式 | 說明 |
|------|------|
| `none` | 不循環 - 播放清單播放一次 |
| `single` | 循環目前的歌曲 |
| `list` | 循環整個播放清單 |

### 我可以從播放清單中移除歌曲嗎？

可以！使用 `/remove [編號]`，其中編號是歌曲在播放清單中的位置（可用 `/queue` 查看）。

### 播放清單播放完畢後會發生什麼？

當播放清單中的所有歌曲都播放完畢後，機器人會自動離開語音頻道。

---

## 🎨 自訂功能

### 可以使用自己的表情符號嗎？

可以！將您的自訂表情符號圖片放在：
- **Windows**：`C:\Users\USERNAME\AppData\Roaming\Easy Music Bot\data\emojis`
- **其他環境**：`./data/emojis/`

然後使用 `/reload_emojis custom` 來載入。

<div class="callout callout-info">
  <strong>📝 檔案命名：</strong>圖片檔名（不含副檔名）必須與 `assets/emojis/` 中的表情符號名稱相符。例如：`list.gif` → `list.png`
</div>

### 有哪些表情符號可以自訂？

可自訂的表情符號包括：
- `play`、`pause`、`stop`
- `next`、`previous`
- `volume`、`refresh`
- `loop`、`list`
- 等等...

---

## 🛡️ 隱私與安全

### 我的資料安全嗎？

- **自架主機**：您的資料會留在您自己的伺服器上
- **自訂播放清單**：儲存在本機的 `data/` 資料夾中
- **URL 快取**：用於加快播放速度的臨時儲存

### 誰可以使用機器人？

只有已安裝機器人的伺服器上的使用者才能使用它。您的個人資料除了 Discord API 外不會傳送到任何地方。

### 關於 Bot Token？

- 千萬不要分享您的 Bot Token
- 如果外洩，請立即從 Discord 開發者入口網站重新產生
- Token 只允許控制您的機器人，無法存取您的 Discord 帳號

---

## 🐛 疑難排解

### 機器人無法啟動

1. 檢查 `.env` 中的 `DISCORD_TOKEN` 是否正確
2. 確認所有 intents 都已啟用
3. 查看主控台中的錯誤訊息

### 機器人已加入語音頻道但沒有聲音

1. 檢查機器人是否有「連接」和「說話」權限
2. 確認 FFmpeg 已安裝（音訊解碼所需）
3. 嘗試使用 `/volume` 增加音量

### 指令沒有作用

1. 確認您使用的是正確的格式（`/指令` 或 `$指令`）
2. 檢查您是否需要在語音頻道中
3. 嘗試重新啟動機器人

### 顯示「Something went wrong」錯誤

這通常表示：
- YouTube 封鎖了請求（請嘗試其他影片）
- 網路問題（請檢查您的連線）
- 機器人受到 rate-limit（請稍後再試）

---

## 💬 取得幫助

### 我可以在哪裡獲得支援？

- **GitHub Issues**：[回報錯誤](https://github.com/NotKeKe/TuneZ-Discord-Bot/issues)

### 如何回報錯誤？

請在 GitHub 上開啟 issue，包含：
1. 您的作業系統
2. 您如何安裝 TuneZ（exe/docker/uv）
3. 準確的錯誤訊息
4. 重現問題的步驟

### 可以請求新功能嗎？

可以！在 GitHub Issues 上開啟功能請求。我們非常感謝所有建議！

---

## 📄 授權

見 [授權]({{ '/zh-TW/#license' | relative_url }})