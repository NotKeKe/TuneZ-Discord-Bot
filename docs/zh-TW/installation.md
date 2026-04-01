---
layout: default
title: 安裝指南
lang: zh-TW
permalink: /zh-TW/installation/
breadcrumb:
  - title: 主頁
    url: /zh-TW/
  - title: 安裝指南
    url: /zh-TW/installation/
---

# 安裝指南

本指南將幫助您在自己的伺服器上設定 TuneZ。請選擇最適合您的方法。

<div class="callout callout-warning">
  <strong>⚠️ 前置需求：</strong>在繼續之前，您需要有一個 Discord Bot Token。如果您還沒有，請先查看<a href="{{ '/zh-TW/installation/' | relative_url }}#創建-discord-bot">創建 Discord Bot</a>章節。
</div>

---

## 📋 前置需求

在安裝 TuneZ 之前，請確認您有以下條件：

1. **Discord Bot Token** - 在 [Discord 開發者入口網站](https://discord.com/developers/applications) 建立機器人應用程式
2. **Python 3.10+**（使用 uv 方法）
3. **Docker 和 Docker Compose**（使用 Docker 方法）
4. **FFmpeg**（Windows exe 和 Docker 方法通常已包含）

---

## 🚀 安裝方式

### 方法一：Windows (.exe) ⭐ 推薦新手使用

在 Windows 上最簡單的開始方式。

#### 步驟：

1. **下載最新版本**

   前往 [Releases](https://github.com/NotKeKe/easy-discord-music-bot/releases) 下載 `.exe` 檔案。

2. **執行安裝檔**

   雙擊 `windows.exe` 執行。它會自動解壓縮必要的資源。

3. **設定機器人**

   導航到 Roaming 目錄：
   ```
   C:\Users\您的使用者名稱\AppData\Roaming\Easy Music Bot
   ```

4. **編輯 `.env` 檔案**

   使用任何文字編輯器開啟 `.env`，並加入您的 Discord Bot Token：

   ```env
   DISCORD_TOKEN=您的機器人token
   OWNER_ID=您的Discord使用者ID
   ```

   <div class="callout callout-info">
     <strong>💡 提示：</strong>您可以將 `OWNER_ID` 留空。它只用於表情符號重載指令。
   </div>

5. **再次執行機器人**

   再次雙擊 `windows.exe`。您應該會看到機器人啟動了！

6. **測試一下**

   加入語音頻道並使用 `/play` 開始播放音樂！

---

### 方法二：Docker

推薦給熟悉 Docker 的使用者。

#### 步驟：

1. **克隆專案**

   ```bash
   git clone https://github.com/NotKeKe/TuneZ-Discord-Bot.git
   cd TuneZ-Discord-Bot
   ```

2. **建立 `.env` 檔案**

   ```bash
   cp .env.example .env
   ```

3. **編輯 `.env` 檔案**

   ```env
   DISCORD_TOKEN=您的機器人token
   OWNER_ID=您的Discord使用者ID
   ```

4. **建立資料目錄**

   ```bash
   mkdir -p data logs
   ```

   - `data/` - 儲存自訂播放清單、URL 快取等
   - `logs/` - 儲存機器人日誌用於除錯

5. **啟動機器人**

   ```bash
   docker compose up -d
   ```

6. **查看日誌**

   ```bash
   docker compose logs -f
   ```

<div class="callout callout-success">
  <strong>✅ 成功！</strong>機器人應該已經啟動並運行了！
</div>

---

### 方法三：uv (Python)

適合喜歡直接執行 Python 的開發者。

#### 前置需求：

- Python 3.10 或更高版本
- [uv](https://github.com/astral-sh/uv) 套件管理器

#### 安裝方式：

1. **安裝 uv**

   使用 pip：
   ```bash
   pip install uv
   ```

   或使用安裝腳本：
   ```bash
   # Windows
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # macOS / Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **克隆專案**

   ```bash
   git clone https://github.com/NotKeKe/TuneZ-Discord-Bot.git
   cd TuneZ-Discord-Bot
   ```

3. **建立 `.env` 檔案**

   ```bash
   cp .env.example .env
   ```

4. **編輯 `.env` 檔案**

   ```env
   DISCORD_TOKEN=您的機器人token
   OWNER_ID=您的Discord使用者ID
   ```

5. **同步依賴**

   ```bash
   uv sync
   ```

6. **執行機器人**

   ```bash
   uv run main.py
   ```

---

## 🔧 創建 Discord Bot

如果您還沒有 Discord Bot，請按照以下步驟建立：

### 1. 建立新應用程式

1. 前往 [Discord 開發者入口網站](https://discord.com/developers/applications)
2. 點擊 **"New Application"**
3. 為您的應用程式命名（例如 "TuneZ"）
4. 點擊 **"Create"**

### 2. 建立機器人

1. 在左側邊欄點擊 **"Bot"**
2. 點擊 **"Add Bot"**
3. 點擊 **"Yes, do it!"**

### 3. 取得您的 Token

1. 在 **Token** 區塊下，點擊 **"Reset Token"**
2. 複製並保存您的 token（您將無法再次查看！）

<div class="callout callout-danger">
  <strong>🔒 重要：</strong>千萬不要分享您的機器人 token！如果有人取得它，他們可以控制您的機器人。
</div>

### 4. 啟用必要的 Intents

1. 向下滾動到 **Privileged Gateway Intents** 區塊
2. 啟用以下選項：
   - ✅ **PRESENCE INTENT**
   - ✅ **SERVER MEMBERS INTENT**
   - ✅ **MESSAGE CONTENT INTENT**

### 5. 產生邀請連結

1. 前往 **OAuth2 > URL Generator**
2. 選擇以下 scopes：
   - ✅ `bot`
   - ✅ `applications.commands`
3. 選擇機器人權限：
   - ✅ 發送訊息
   - ✅ 讀取訊息歷史
   - ✅ 連接（至語音頻道）
   - ✅ 說話（在語音頻道中）
   - ✅ 使用斜線指令

4. 複製產生的 URL 並在瀏覽器中開啟

5. 選擇您想要添加機器人的伺服器

---

## ⚙️ 設定

### 環境變數

| 變數 | 必填 | 描述 |
|------|------|------|
| `DISCORD_TOKEN` | 是 | 您的 Discord 機器人 token |
| `OWNER_ID` | 否 | 您的 Discord 使用者 ID（用於擁有者專屬指令）|

### 資料儲存

執行機器人後，會建立 `data/` 資料夾，包含：

- `custom_lists/` - 自訂播放清單儲存
- `url_cache/` - YouTube URL 快取

---

## 🐛 疑難排解

### 機器人無法啟動？

1. 檢查您的 `DISCORD_TOKEN` 是否正確
2. 確認您已啟用所有必要的 intents
3. 查看日誌中的錯誤訊息

### 語音連接問題？

1. 確認機器人有連接和說話的權限
2. 檢查 FFmpeg 是否已安裝（音訊播放所需）

### 音樂無法播放？

1. 確認您在語音頻道中
2. 檢查 YouTube URL 是否可存取
3. 嘗試使用不同的關鍵字（歌曲名稱而非 URL）

---

## 📚 下一步

現在您已經安裝好 TuneZ了，請查看：

- [指令列表]({{ '/zh-TW/commands/' | relative_url }}) - 學習所有可用指令
- [自訂播放清單]({{ '/zh-TW/custom-playlist/' | relative_url }}) - 建立您自己的播放清單
- [常見問題]({{ '/zh-TW/faq/' | relative_url }}) - 常見問題和解答
