---
layout: default
title: TuneZ Discord Bot
lang: en
permalink: /
---

# TuneZ Discord Bot

<p align="center">
  <img src="{{ '/assets/icon.png' | relative_url }}" alt="TuneZ Logo" width="150" height="150">
</p>

<p align="center">
  A Python-based Discord bot that works <strong>out-of-the-box</strong> for anyone who needs to play music on Discord.
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

## ✨ Features

<div class="feature-grid">
  <div class="feature-card">
    <div class="feature-icon">🎵</div>
    <h3>Music Playback</h3>
    <p>Play music from YouTube with high quality audio streaming and smooth playback.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">📋</div>
    <h3>Queue Management</h3>
    <p>Full control over your playlist with add, remove, skip, clear, and reorder functions.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🔁</div>
    <h3>Loop Modes</h3>
    <p>Multiple loop options: none, single track, or entire playlist.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🎨</div>
    <h3>Custom Emojis</h3>
    <p>Beautiful animated light blue emojis included. Customize with your own!</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🌐</div>
    <h3>Multi-language</h3>
    <p>Supports English, Traditional Chinese, and Simplified Chinese.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🚀</div>
    <h3>Easy Setup</h3>
    <p>Works out-of-the-box. Windows .exe, Docker, or Python - your choice!</p>
  </div>
</div>

---

## 📖 Quick Start

### Option 1: Invite the Bot

If you just want a Discord music bot, you can directly invite [YinXi](https://github.com/NotKeKe/Discord-Bot-YinXi) to your server.

[![Invite Bot](https://img.shields.io/badge/Invite-YinXi-5865F2?style=for-the-badge)](https://discord.com/oauth2/authorize?client_id=990798785489825813)

### Option 2: Self-hosting

For more control and features, host TuneZ yourself:

1. **Windows**: Download the `.exe` from [Releases](https://github.com/NotKeKe/easy-discord-music-bot/releases)
2. **Docker**: `docker compose up -d`
3. **Python**: `uv run main.py`

See [Installation Guide]({{ '/en/installation/' | relative_url }}) for detailed instructions.

---

## 🎮 Demo

![Demo]({{ '/assets/demo.png' | relative_url }})

---

## 🛠️ Available Commands

| Command | Description |
|---------|-------------|
| `/play [query]` | Play music or add to queue |
| `/skip` | Skip the current song |
| `/pause` | Pause playback |
| `/resume` | Resume playback |
| `/queue` | View the current playlist |
| `/loop [mode]` | Set loop mode (none/single/list) |
| `/volume [0-200]` | Adjust volume |
| `/stop` | Stop and leave the voice channel |

[View all commands →]({{ '/en/commands/' | relative_url }})

---

## 📚 Documentation

- [Installation Guide]({{ '/en/installation/' | relative_url }}) - How to set up TuneZ
- [Command Reference]({{ '/en/commands/' | relative_url }}) - Full list of all commands
- [Custom Playlists]({{ '/en/custom-playlist/' | relative_url }}) - Create and manage playlists
- [FAQ]({{ '/en/faq/' | relative_url }}) - Frequently asked questions

---

## 💬 Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/NotKeKe/TuneZ-Discord-Bot/issues)

---

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](https://github.com/NotKeKe/TuneZ-Discord-Bot/blob/main/LICENSE) file for details.

---

<div class="callout callout-info">
  <strong>⭐ Remember to give us a Star!</strong><br>
  It's our source of motivation!
</div>
