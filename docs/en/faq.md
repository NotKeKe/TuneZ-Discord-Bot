---
layout: default
title: FAQ
lang: en
permalink: /en/faq/
breadcrumb:
  - title: Home
    url: {{ '/en/' | relative_url }}
  - title: FAQ
    url: {{ '/en/faq/' | relative_url }}
---

# Frequently Asked Questions

Common questions and answers about TuneZ.

---

## ❓ General Questions

### What is TuneZ?

TuneZ is a Python-based Discord music bot that works out-of-the-box. It allows you to play music from YouTube in your Discord voice channels with features like queue management, loop modes, and custom playlists.

### How is TuneZ different from other music bots?

- **Out-of-the-box**: Works immediately with minimal configuration
- **Self-hosting**: You control your own bot and data
- **Custom emojis**: Comes with beautiful animated emojis, customizable
- **Multi-language**: Supports English, Traditional Chinese, and Simplified Chinese

### Do I need to pay to use TuneZ?

No, TuneZ is completely free and open source under the Apache License 2.0.

---

## 🔧 Installation & Setup

### What do I need to run TuneZ?

- A Discord Bot token (free from Discord Developer Portal)
- One of the following:
  - Windows computer (for .exe method)
  - Docker installed (for Docker method)
  - Python 3.10+ (for uv method)

### I don't have a Discord Bot token. How do I get one?

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and name it
3. Go to "Bot" in the left sidebar
4. Click "Add Bot" and confirm
5. Copy your token (click "Reset Token" if needed)
6. Enable these intents under "Privileged Gateway Intents":
   - PRESENCE INTENT
   - SERVER MEMBERS INTENT
   - MESSAGE CONTENT INTENT

### Why do I need to enable intents?

Discord requires bots to have specific intents enabled to access certain features. TuneZ needs:
- **Presence Intent**: To detect when users join/leave voice channels
- **Server Members Intent**: For member-related functionality
- **Message Content Intent**: To read command messages (prefix commands)

---

## 🎵 Music Playback

### Why won't music play?

Check these common issues:

1. **Not in voice channel**: You must be in a voice channel to use music commands
2. **Bot not in voice channel**: The bot needs permission to join and speak
3. **Invalid URL**: Make sure the YouTube URL is correct and accessible
4. **Blocked content**: Some videos may be region-locked or removed

### Why does the audio quality seem poor?

This can happen due to:
- Slow internet connection
- YouTube server issues
- High load on the bot

### Can I play playlists from YouTube?

Yes! You can paste a YouTube playlist URL when using `/play` or `/add`.

### Does TuneZ support Spotify/Apple Music?

Currently, TuneZ only supports YouTube directly. However, you can:
- Find YouTube links for songs
- Create custom playlists with YouTube URLs

---

## 🔁 Loop & Queue

### What's the difference between loop modes?

| Mode | Description |
|------|-------------|
| `none` | No looping - plays through queue once |
| `single` | Loops the current song forever |
| `list` | Loops the entire queue |

### Can I remove a song from the queue?

Yes! Use `/remove [number]` where number is the song's position in the queue (shown by `/queue`).

### What happens when the queue ends?

When all songs in the queue have been played, the bot will automatically leave the voice channel.

---

## 🎨 Customization

### Can I use my own emojis?

Yes! Place your custom emoji images in:
- **Windows**: `C:\Users\USERNAME\AppData\Roaming\Easy Music Bot\data\emojis`
- **Other**: `./data/emojis/`

Then use `/reload_emojis custom` to load them.

<div class="callout callout-info">
  <strong>📝 File naming:</strong> Image filenames (without extension) must match the emoji names in `assets/emojis/`. Example: `list.gif` → `list.png`
</div>

### What emoji names can I customize?

The customizable emojis include:
- `play`, `pause`, `stop`
- `next`, `previous`
- `volume`, `refresh`
- `loop`, `list`
- And more...

---

## 🛡️ Privacy & Security

### Is my data safe?

- **Self-hosting**: Your data stays on your own server
- **Custom playlists**: Stored locally in the `data/` folder
- **URL cache**: Temporary storage for faster playback

### Who can use the bot?

Only users in servers where the bot is installed can use it. Your personal data is never sent anywhere except Discord's API.

### What about the bot token?

- Never share your bot token
- If compromised, regenerate it immediately from Discord Developer Portal
- The token only allows control of your bot, not access to your Discord account

---

## 🐛 Troubleshooting

### Bot won't start

1. Check if `DISCORD_TOKEN` in `.env` is correct
2. Make sure all intents are enabled
3. Check for error messages in the console

### Bot joined voice channel but no sound

1. Check if bot has "Connect" and "Speak" permissions
2. Make sure FFmpeg is installed (required for audio decoding)
3. Try increasing the volume with `/volume`

### Commands don't work

1. Make sure you're using the correct format (`/command` or `$command`)
2. Check if you need to be in a voice channel
3. Try restarting the bot

### "Something went wrong" error

This usually means:
- YouTube blocked the request (try a different video)
- Network issues (check your connection)
- Bot is rate-limited (wait and try again)

---

## 💬 Getting Help

### Where can I get support?

- **GitHub Issues**: [Report bugs](https://github.com/NotKeKe/TuneZ-Discord-Bot/issues)
- **Documentation**: Check this website for guides

### How do I report a bug?

Please open an issue on GitHub with:
1. Your operating system
2. How you installed TuneZ (exe/docker/uv)
3. The exact error message
4. Steps to reproduce the issue

### Can I request features?

Yes! Open a feature request on GitHub Issues. We appreciate all suggestions!

---

## 📄 License

TuneZ is licensed under Apache License 2.0. You can:
- ✅ Use it for personal or commercial purposes
- ✅ Modify and customize it
- ✅ Distribute it

You cannot:
- ❌ Hold the author liable
- ❌ Use the name for endorsement

See [LICENSE](https://github.com/NotKeKe/TuneZ-Discord-Bot/blob/main/LICENSE) for details.
