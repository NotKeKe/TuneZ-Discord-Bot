---
layout: default
title: Home
lang: en
permalink: /en/
---

# TuneZ Discord Music Bot

<p align="center">
  <img src="{{ '/assets/icon.png' | relative_url }}" alt="TuneZ Logo" width="150" height="150">
</p>

<p align="center">
  A Python-based Discord music bot that is <strong>ready to use out of the box</strong> for everyone who wants to play music on Discord.
</p>

<p align="center">
  <a href="https://github.com/NotKeKe/TuneZ-Discord-Bot/stargazers">
    <img src="https://img.shields.io/github/stars/NotKeKe/TuneZ-Discord-Bot?style=social" alt="Stars">
  </a>
  <a href="https://github.com/NotKeKe/TuneZ-Discord-Bot/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-Apache%20License%202.0-yellow" alt="License">
  </a>
  <a href="https://discord.com/oauth2/authorize?client_id=990798785489825813">
    <img src="https://img.shields.io/badge/Invite-Discord-5865F2?style=flat" alt="Discord">
  </a>
</p>

---

## 📖 Preface
<details>
    <summary>Why was this made?</summary>
    <ul>
        <li>
            A friend asked me for <a href="https://github.com/NotKeKe/Discord-Bot-YinXi">YinXi</a> not long ago. Later, after reading <a href="https://yeecord.com/">YEE式机器龙</a>'s <a href="https://yeecord.com/blog/thats-why-i-gave-up-on-music">post</a>, I realized how difficult music bots have become nowadays.
        </li>
        <li>
            Since I already had YinXi, I thought: what if I extracted the music-related code and made a dedicated music bot? <del>Would it become popular?</del>
        </li>
        <li>
            Plus, yt-dlp can easily get 403 (permission denied) or other errors if requests keep coming from the same IP. <del>(This is probably why music bots are becoming rarer - stable sources are genuinely hard to find.)</del><br>
            But if every user just self-hosts their Discord bot according to their own needs, maybe this problem could be solved?
        </li>
        <li>
            So I made TuneZ
        </li>
    </ul>
</details>
<details>
    <summary>Why is it called TuneZ?</summary>
    <ul>
        <li>
            Actually, the reason is super simple
        </li>
        <li>
            First, I randomly asked Copilot to help me think of a name, and it came up with "Tune". <br>
            Later, I realized that people born around 2000 are called Generation Z <br>
            So then came the "Z" <br>
            Put together, it becomes <strong>TuneZ</strong>
        </li>
    </ul>
</details>
<details>
    <summary>Are there any risks?</summary>
    <ul>
        <li>
            The answer is actually quite simple - using it yourself means no risks
        </li>
        <li>
            Usually, using it yourself or letting friends try it out won't cause any issues
        </li>
        <li>
            Unless you decide to use it for profit <br>
            Then I can't be held responsible :) <br>
            I won't take any responsibility
        </li>
    </ul>
</details>

## ✨ Features

<div class="feature-grid">
  <div class="feature-card">
    <div class="feature-icon">🎵</div>
    <h3>Music Playback</h3>
    <p>Play high-quality audio streams from YouTube with smooth playback.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">📋</div>
    <h3>Playlist Management</h3>
    <p>Full control over playlists, including add, remove, skip, clear, and more.</p>
  </div>

  <div class="feature-card">
    <div class="feature-icon">📋</div>
    <h3>Custom Playlists</h3>
    <p>Create your own playlists with custom names using single YouTube links.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🔁</div>
    <h3>Loop Modes</h3>
    <p>Multiple loop options: none, single track, or playlist loop.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🎨</div>
    <h3>Custom Emojis</h3>
    <p>Built-in beautiful light blue animated emojis, customizable too!</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🌐</div>
    <h3>Multi-language Support</h3>
    <p>Supports English, Traditional Chinese, and Simplified Chinese.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🚀</div>
    <h3>Easy to Get Started</h3>
    <p>Out of the box! Supports Windows exe, Docker, Python, and more.</p>
  </div>
</div>

---

## 📖 Quick Start

### Method One: Invite the Bot

If you just want a Discord music bot, you can directly invite [YinXi](https://github.com/NotKeKe/Discord-Bot-YinXi) to your server.

[![Invite Bot](https://img.shields.io/badge/Invite-YinXi-5865F2?style=for-the-badge)](https://discord.com/oauth2/authorize?client_id=990798785489825813)

### Method Two: Self-host the Bot (Recommended)

Want more control and features? Host TuneZ yourself:

1. **Windows**: Download the `.exe` file from [Releases](https://github.com/NotKeKe/easy-discord-music-bot/releases)
2. **Docker**: `docker compose up -d`
3. **Python**: `uv run main.py`

See the [Installation Guide]({{ '/en/installation/' | relative_url }}) for detailed instructions.

---

## 🎮 Demo

![Demo]({{ '/assets/demo.png' | relative_url }})

*TuneZ supports Chinese; it just shows English because Discord's default language is English.*

---

## 🛠️ Available Commands

| Command | Description |
|---------|-------------|
| `/play [query]` | Play music or add to playlist |
| `/skip` | Skip current song |
| `/pause` | Pause playback |
| `/resume` | Resume playback |
| `/queue` | View playlist |
| `/loop [mode]` | Set loop mode (none/single/list) |
| `/volume [0-200]` | Adjust volume |
| `/stop` | Stop playback and leave voice channel |

[View all commands →]({{ '/en/commands/' | relative_url }})

---

## 📚 Documentation

- [Create Discord Bot]({{ '/en/register-discord-bot/' | relative_url }}) - How to create a Discord Bot
- [Installation Guide]({{ '/en/installation/' | relative_url }}) - How to set up TuneZ
- [Command List]({{ '/en/commands/' | relative_url }}) - Complete list of all commands
- [Custom Playlists]({{ '/en/custom-playlist/' | relative_url }}) - Create and manage playlists
- [FAQ]({{ '/en/faq/' | relative_url }}) - Troubleshooting

---

## 💬 Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/NotKeKe/TuneZ-Discord-Bot/issues)
  - Whether you're a coding expert or a beginner, feel free to submit Issues for any problems or feature requests

---

<div id=license></div>

## 📄 License

TuneZ is licensed under Apache License 2.0. You can:
- ✅ Use the project code for personal or commercial purposes
- ✅ Modify and customize
- ✅ Distribute

You cannot:
- ❌ Hold the author responsible
- ❌ Use the name for endorsements

See [LICENSE](https://github.com/NotKeKe/TuneZ-Discord-Bot/blob/main/LICENSE).

<div class="callout callout-danger">
  <strong>❗ The author of this project does not accept or take responsibility for any legal consequences or infringement caused by users using this project.</strong>
</div>

---

<div class="callout callout-info">
  <strong>⭐ Remember to give me a Star!</strong><br>
  This is my source of motivation!
</div>
