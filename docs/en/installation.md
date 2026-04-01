---
layout: default
title: Installation
lang: en
permalink: /en/installation/
breadcrumb:
  - title: Home
    url: /en/
  - title: Installation
    url: /en/installation/
---

# Installation Guide

This guide will help you set up TuneZ on your own server. Choose the method that best suits your needs.

<div class="callout callout-warning">
  <strong>⚠️ Prerequisites:</strong> You need to have a Discord Bot token before proceeding. If you don't have one, follow the <a href="{{ '/en/register-discord-bot/' | relative_url }}">Register Discord Bot</a> guide first.
</div>

---

## 📋 Prerequisites

Before installing TuneZ, make sure you have:

1. **Discord Bot Token** - Create a bot application at [Discord Developer Portal](https://discord.com/developers/applications)
2. **Python 3.10+** (for uv method)
3. **Docker & Docker Compose** (for Docker method)
4. **FFmpeg** (usually included in Windows .exe and Docker)

---

## 🚀 Installation Methods

### Method 1: Windows (.exe) ⭐ Recommended for beginners

The easiest way to get started on Windows.

#### Steps:

1. **Download the latest release**

   Go to [Releases](https://github.com/NotKeKe/easy-discord-music-bot/releases) and download the `.exe` file.

2. **Run the executable**

   Double-click `windows.exe` to run it. It will automatically extract necessary resources.

3. **Configure the bot**

   Navigate to the Roaming directory:
   ```
   C:\Users\YOUR_USERNAME\AppData\Roaming\Easy Music Bot
   ```

4. **Edit the `.env` file**

   Open `.env` with any text editor and add your Discord Bot Token:

   ```env
   DISCORD_TOKEN=your_bot_token_here
   OWNER_ID=your_discord_user_id
   ```

   <div class="callout callout-info">
     <strong>💡 Tip:</strong> You can leave `OWNER_ID` blank. It's only used for emoji reloading commands.
   </div>

5. **Run the bot again**

   Double-click `windows.exe` again. You should see the bot starting up!

6. **Test it**

   Join a voice channel and use `/play` to start playing music.

---

### Method 2: Docker

Recommended for users who are familiar with Docker.

#### Steps:

1. **Clone the repository**

   ```bash
   git clone https://github.com/NotKeKe/TuneZ-Discord-Bot.git
   cd TuneZ-Discord-Bot
   ```

2. **Create the `.env` file**

   ```bash
   cp .env.example .env
   ```

3. **Edit the `.env` file**

   ```env
   DISCORD_TOKEN=your_bot_token_here
   OWNER_ID=your_discord_user_id
   ```

4. **Create data directories**

   ```bash
   mkdir -p data logs
   ```

   - `data/` - Stores custom playlists, URL cache, etc.
   - `logs/` - Stores bot logs for debugging

5. **Start the bot**

   ```bash
   docker compose up -d
   ```

6. **Check logs**

   ```bash
   docker compose logs -f
   ```

<div class="callout callout-success">
  <strong>✅ Success!</strong> The bot should be up and running!
</div>

---

### Method 3: uv (Python)

For developers who prefer running Python directly.

#### Prerequisites:

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) package manager

#### Installation:

1. **Install uv**

   Using pip:
   ```bash
   pip install uv
   ```

   Or using the installer:
   ```bash
   # Windows
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # macOS / Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone the repository**

   ```bash
   git clone https://github.com/NotKeKe/TuneZ-Discord-Bot.git
   cd TuneZ-Discord-Bot
   ```

3. **Create the `.env` file**

   ```bash
   cp .env.example .env
   ```

4. **Edit the `.env` file**

   ```env
   DISCORD_TOKEN=your_bot_token_here
   OWNER_ID=your_discord_user_id
   ```

5. **Sync dependencies**

   ```bash
   uv sync
   ```

6. **Run the bot**

   ```bash
   uv run main.py
   ```

---

## 🔧 Create Discord Bot

If you don't have a Discord Bot yet, follow these steps:

### 1. Create a New Application

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **"New Application"**
3. Give your application a name (e.g., "TuneZ")
4. Click **"Create"**

### 2. Create a Bot

1. In the left sidebar, click **"Bot"**
2. Click **"Add Bot"**
3. Click **"Yes, do it!"**

### 3. Get Your Token

1. Under the **Token** section, click **"Reset Token"**
2. Copy and save your token (you won't be able to see it again!)

<div class="callout callout-danger">
  <strong>🔒 Important:</strong> Never share your bot token! If someone gets it, they can control your bot.
</div>

### 4. Enable Required Intents

1. Scroll down to the **Privileged Gateway Intents** section
2. Enable:
   - ✅ **PRESENCE INTENT**
   - ✅ **SERVER MEMBERS INTENT**
   - ✅ **MESSAGE CONTENT INTENT**

### 5. Generate Invite Link

1. Go to **OAuth2 > URL Generator**
2. Select the following scopes:
   - ✅ `bot`
   - ✅ `applications.commands`
3. Select bot permissions:
   - ✅ Send Messages
   - ✅ Read Message History
   - ✅ Connect (to voice channels)
   - ✅ Speak (in voice channels)
   - ✅ Use Slash Commands

4. Copy the generated URL and open it in your browser

5. Select the server you want to add the bot to

---

## ⚙️ Configuration

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `DISCORD_TOKEN` | Yes | Your Discord bot token |
| `OWNER_ID` | No | Your Discord user ID (for owner-only commands) |

### Data Storage

After running the bot, a `data/` folder will be created with:

- `custom_lists/` - Custom playlist storage
- `url_cache/` - YouTube URL cache

---

## 🐛 Troubleshooting

### Bot won't start?

1. Check if your `DISCORD_TOKEN` is correct
2. Make sure you have all required intents enabled
3. Check the logs for error messages

### Voice connection issues?

1. Make sure the bot has permission to connect and speak in your voice channel
2. Check if FFmpeg is installed (required for audio playback)

### Music not playing?

1. Make sure you're in a voice channel
2. Check if YouTube URL is accessible
3. Try using a different query (song name instead of URL)

---

## 📚 What's Next?

Now that you have TuneZ installed, check out:

- [Commands Reference]({{ '/en/commands/' | relative_url }}) - Learn all available commands
- [Custom Playlists]({{ '/en/custom-playlist/' | relative_url }}) - Create your own playlists
- [FAQ]({{ '/en/faq/' | relative_url }}) - Common questions and answers
