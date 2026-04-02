---
layout: default
title: Installation Guide
lang: en
permalink: /en/installation/
breadcrumb:
  - title: Home
    url: /en/
  - title: Installation Guide
    url: /en/installation/
---

# Installation Guide

This guide will help you set up TuneZ on your own server. Choose the method that best suits you.

<div class="callout callout-warning">
  <strong>⚠️ Prerequisites:</strong> Before continuing, you need a Discord Bot Token. If you don't have one yet, please first check the <a href="{{ '/en/register-discord-bot/' | relative_url }}">Register Discord Bot</a> guide.
</div>

---

## 📋 Prerequisites

Before installing TuneZ, make sure you have:

1. **Discord Bot Token** - Create a bot at [Discord Developer Portal](https://discord.com/developers/applications)
2. **Python 3.10+** (if using uv)
3. **Docker and Docker Compose** (if using Docker)
4. **FFmpeg** (usually included with Windows exe and Docker)

---

## 🚀 Installation Methods

### Method One: Windows (.exe) ⭐ Recommended for beginners

The easiest way to get started on Windows.

#### Steps:

1. **Download the latest version**

   Go to [Releases](https://github.com/NotKeKe/easy-discord-music-bot/releases) and download the `.exe` file.

2. **Run the installer**

   Double-click `windows.exe` to run it. It will place necessary resources in the directory for the next step.

3. **Configure the bot**

   Navigate to the Roaming directory:
   ```
   C:\Users\YourUsername\AppData\Roaming\TuneZ_Discord_Bot
   ```

4. **Edit the `.env` file**

   Open `.env` with any text editor and add your Discord Bot Token:

   ```env
   DISCORD_TOKEN=your_bot_token
   OWNER_ID=your_discord_user_id
   ```

   <div class="callout callout-info">
     <strong>💡 Tip:</strong> You can leave `OWNER_ID` empty. It's only used for the emoji reload command.
   </div>

5. **Run the bot again**

   Double-click `windows.exe` again. You should see the bot start up!

6. **Test it out**

   Join a voice channel and use `/play` to start playing music!
   <br>
   Or use `/help` to get command help!

---

### Method Two: Docker

Recommended for users familiar with Docker.

#### Steps:

1. **Clone the project**

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
   DISCORD_TOKEN=your_bot_token
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

6. **View logs (optional)**

   ```bash
   docker compose logs -f
   ```

<div class="callout callout-success">
  <strong>✅ Success!</strong> The bot should now be up and running!
</div>

---

### Method Three: uv (Python)

For developers who prefer to run Python directly.

#### Prerequisites:

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) package manager

#### Installation:

1. **Install uv**

   Using pip:
   ```bash
   pip install uv
   ```

   Or using the install script:
   ```bash
   # Windows
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # macOS / Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

   Or see the official uv [installation guide](https://docs.astral.sh/uv/getting-started/installation/):
   ```
   https://docs.astral.sh/uv/getting-started/installation/
   ```

2. **Clone the project**

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
   DISCORD_TOKEN=your_bot_token
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

## ⚙️ Configuration

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `DISCORD_TOKEN` | Yes | Your Discord bot token |
| `OWNER_ID` | No | Your Discord user ID (for owner-only commands) |

---

## 📚 Next Steps

Now that you have TuneZ installed, check out:

- [Command List]({{ '/en/commands/' | relative_url }}) - Learn all available commands
- [Custom Playlists]({{ '/en/custom-playlist/' | relative_url }}) - Create your own playlists
- [FAQ]({{ '/en/faq/' | relative_url }}) - Common questions and answers
