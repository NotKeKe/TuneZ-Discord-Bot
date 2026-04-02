---
layout: default
title: Frequently Asked Questions
lang: en
permalink: /en/faq/
breadcrumb:
  - title: Home
    url: /en/
  - title: FAQ
    url: /en/faq/
---

# Frequently Asked Questions

Common questions and answers about TuneZ.

---

## ❓ Basic Questions

### What is TuneZ?

TuneZ is a Python-based Discord music bot that lets you play YouTube music in Discord voice channels. It features playlist management, loop modes, and custom playlists out of the box.

### What makes TuneZ different from other music bots?

- **Out of the box**: Works with minimal configuration
- **Self-hosted**: You control your own bot and data
- **Custom emojis**: Built-in beautiful animated emojis that you can customize
- **Multi-language support**: Supports English, Traditional Chinese, and Simplified Chinese

### Do I need to pay to use TuneZ?

No, TuneZ is completely free and open source, licensed under Apache License 2.0.

---

## 🔧 Installation and Setup

### What do I need to run TuneZ?

- A Discord Bot Token (obtainable from the Discord Developer Portal), see [Register Discord Bot]({{ '/en/register-discord-bot/' | relative_url }})
- One of the following environments:
  - Windows PC (using .exe)
  - Docker installed (using Docker)
  - Python 3.10+ (using uv)

### I don't have a Discord Bot Token. How do I get one?

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Click "Bot" in the left sidebar
4. Click "Add Bot" and confirm
5. Copy your Token (click "Reset Token" if you need to regenerate)
6. Enable these under "Privileged Gateway Intents":
   - PRESENCE INTENT
   - SERVER MEMBERS INTENT
   - MESSAGE CONTENT INTENT

See [Register Discord Bot]({{ '/en/register-discord-bot/' | relative_url }}) for more details.

### Why do I need to enable intents?

Discord requires bots to enable specific intents to access certain features. TuneZ needs:
- **Presence Intent**: Detect when users join/leave voice channels
- **Server Members Intent**: For member-related features
- **Message Content Intent**: Read command messages (prefix commands)

---

## 🎵 Music Playback

### Why isn't music playing?

Check these common issues:

1. **Not in a voice channel**: You must be in a voice channel to use music commands
2. **Bot not in voice channel**: The bot needs Connect and Speak permissions
3. **Invalid URL**: Make sure the YouTube URL is correct and accessible
4. **Content blocked**: Some videos may be region-restricted or removed

### Why is the audio quality poor?

This could be due to:
- Slow network connection
- YouTube server issues
- High bot load

### Can I play YouTube playlists?

Yes! When using `/play` or `/add`, you can paste a YouTube playlist URL.

### Does TuneZ support Spotify/Apple Music?

Currently, TuneZ only directly supports YouTube. However, you can:
- Find the YouTube link for the song
- Create custom playlists using YouTube URLs

---

## 🔁 Loop and Playlist

### What's the difference between loop modes?

| Mode | Description |
|------|-------------|
| `none` | No loop - playlist plays once |
| `single` | Loop current song |
| `list` | Loop entire playlist |

### Can I remove songs from the playlist?

Yes! Use `/remove [number]`, where number is the song's position in the playlist (use `/queue` to check).

### What happens when the playlist finishes?

When all songs in the playlist have finished playing, the bot will automatically leave the voice channel.

---

## 🎨 Customization

### Can I use my own emojis?

Yes! Place your custom emoji images in:
- **Windows**: `C:\Users\USERNAME\AppData\Roaming\Easy Music Bot\data\emojis`
- **Other environments**: `./data/emojis/`

Then use `/reload_emojis custom` to load them.

<div class="callout callout-info">
  <strong>📝 File naming:</strong> The filename (without extension) must match the emoji name in `assets/emojis/`. For example: `list.gif` → `list.png`
</div>

### What emojis can I customize?

Customizable emojis include:
- `play`, `pause`, `stop`
- `next`, `previous`
- `volume`, `refresh`
- `loop`, `list`
- And more...

---

## 🛡️ Privacy and Security

### Is my data safe?

- **Self-hosted**: Your data stays on your own server
- **Custom playlists**: Stored in the local `data/` folder
- **URL cache**: Temporary storage for faster playback

### Who can use the bot?

Only users on servers where the bot is installed can use it. Your personal data is not sent anywhere except to the Discord API.

### What about the Bot Token?

- Never share your Bot Token
- If leaked, regenerate it immediately from the Discord Developer Portal
- The Token only allows controlling your bot, it cannot access your Discord account

---

## 🐛 Troubleshooting

### Bot won't start

1. Check if `DISCORD_TOKEN` in `.env` is correct
2. Make sure all intents are enabled
3. Check error messages in the console

### Bot joined voice channel but no sound

1. Check if the bot has "Connect" and "Speak" permissions
2. Make sure FFmpeg is installed (required for audio decoding)
3. Try increasing volume with `/volume`

### Commands don't work

1. Make sure you're using the correct format (`/command` or `$command`)
2. Check if you need to be in a voice channel
3. Try restarting the bot

### "Something went wrong" error appears

This usually means:
- YouTube blocked the request (try a different video)
- Network issues (check your connection)
- Bot is rate-limited (try again later)

---

## 💬 Getting Help

### Where can I get support?

- **GitHub Issues**: [Report bugs](https://github.com/NotKeKe/TuneZ-Discord-Bot/issues)

### How do I report a bug?

Open an issue on GitHub with:
1. Your operating system
2. How you installed TuneZ (exe/docker/uv)
3. The exact error message
4. Steps to reproduce the problem

### Can I request new features?

Yes! Open a feature request on GitHub Issues. We appreciate all suggestions!

---

## 📄 License

See [License]({{ '/en/#license' | relative_url }})
