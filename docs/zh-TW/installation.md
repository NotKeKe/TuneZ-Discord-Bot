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
  <strong>⚠️ 前置需求：</strong>在繼續之前，您需要有一個 Discord Bot Token。如果您還沒有，請先查看<a href="{{ '/zh-TW/register-discord-bot/' | relative_url }}">註冊 Discord Bot</a>指南。
</div>

---

## 📋 前置需求

在安裝 TuneZ 之前，請確認您有以下條件：

1. **Discord Bot Token** - 在 [Discord 開發者入口網站](https://discord.com/developers/applications) 建立機器人
2. **Python 3.10+**（使用 uv）
3. **Docker 和 Docker Compose**（使用 Docker）
4. **FFmpeg**（Windows exe 和 Docker 通常已包含）

---

## 🚀 安裝方式

### 方法一：Windows (.exe) ⭐ 推薦新手使用

在 Windows 上最簡單的開始方式。

#### 步驟：

1. **下載最新版本**

   前往 [Releases](https://github.com/NotKeKe/easy-discord-music-bot/releases) 下載 `.exe` 檔案。

2. **執行安裝檔**

   雙擊 `windows.exe` 執行。它會於下一步的目錄中，放入必要的資源。

3. **設定機器人**

   導航到 Roaming 目錄：
   ```
   C:\Users\您的使用者名稱\AppData\Roaming\TuneZ_Discord_Bot
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
   <br>
   或者使用 `/help` 來取得指令幫助！

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

6. **查看日誌 (可選)**

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

   或查看 uv 官方的[安裝教學](https://docs.astral.sh/uv/getting-started/installation/)：
   ```
   https://docs.astral.sh/uv/getting-started/installation/
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

## ⚙️ 設定

### 環境變數

| 變數 | 必填 | 描述 |
|------|------|------|
| `DISCORD_TOKEN` | 是 | 您的 Discord 機器人 token |
| `OWNER_ID` | 否 | 您的 Discord 使用者 ID（用於擁有者專屬指令）|

---

## 📚 下一步

現在您已經安裝好 TuneZ了，請查看：

- [指令列表]({{ '/zh-TW/commands/' | relative_url }}) - 學習所有可用指令
- [自訂播放清單]({{ '/zh-TW/custom-playlist/' | relative_url }}) - 建立您自己的播放清單
- [常見問題]({{ '/zh-TW/faq/' | relative_url }}) - 常見問題和解答
