---
layout: default
title: 主頁
lang: zh-TW
permalink: /zh-TW/
---

# TuneZ Discord 音樂機器人

<p align="center">
  <img src="{{ '/assets/icon.png' | relative_url }}" alt="TuneZ Logo" width="150" height="150">
</p>

<p align="center">
  一個基於 Python，每個需要在 Discord 播放音樂的人都可以<strong>開箱即用</strong>的 Discord 音樂機器人。
</p>

<p align="center">
  <a href="https://github.com/NotKeKe/TuneZ-Discord-Bot/stargazers">
    <img src="https://img.shields.io/github/stars/NotKeKe/TuneZ-Discord-Bot?style=social" alt="Stars">
  </a>
  <a href="https://github.com/NotKeKe/TuneZ-Discord-Bot/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-Apache%20License%202.0-yellow" alt="License">
  </a>
  <a href="https://discord.com/oauth2/authorize?client_id=990798785489825813">
    <img src="https://img.shields.io/badge/邀請-Discord-5865F2?style=flat" alt="Discord">
  </a>
</p>

---

## ✨ 特色

<div class="feature-grid">
  <div class="feature-card">
    <div class="feature-icon">🎵</div>
    <h3>音樂播放</h3>
    <p>從 YouTube 播放高品質音訊串流，播放流暢。</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">📋</div>
    <h3>播放清單管理</h3>
    <p>完整控制播放清單，包括新增、移除、跳過、清空等功能。</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🔁</div>
    <h3>循環模式</h3>
    <p>多種循環選項：無循環、單曲循環、播放清單循環。</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🎨</div>
    <h3>自訂表情符號</h3>
    <p>內建精美的淺藍色動畫表情符號，也可以自訂！</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🌐</div>
    <h3>多語言支援</h3>
    <p>支援英文、繁體中文、簡體中文。</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🚀</div>
    <h3>簡單易上手</h3>
    <p>開箱即用！支援 Windows exe、Docker、Python 等多種方式。</p>
  </div>
</div>

---

## 📖 快速開始

### 方法一：邀請機器人

如果您只是想要一個 Discord 音樂機器人，可以直接邀請[音汐](https://github.com/NotKeKe/Discord-Bot-YinXi)到您的伺服器。

[![邀請機器人](https://img.shields.io/badge/邀請-音汐-5865F2?style=for-the-badge)](https://discord.com/oauth2/authorize?client_id=990798785489825813)

### 方法二：自架機器人

想要更多控制權和功能？自己架設 TuneZ：

1. **Windows**：從 [Releases](https://github.com/NotKeKe/easy-discord-music-bot/releases) 下載 `.exe` 檔案
2. **Docker**：`docker compose up -d`
3. **Python**：`uv run main.py`

查看[安裝指南]({{ '/zh-TW/installation/' | relative_url }})獲取詳細說明。

---

## 🎮 Demo 展示

![Demo]({{ '/assets/demo.png' | relative_url }})

*TuneZ 有支援中文，只是因為 Discord 預設語言是英文，所以顯示英文。*

---

## 🛠️ 可用指令

| 指令 | 描述 |
|------|------|
| `/play [關鍵字]` | 播放音樂或加入播放清單 |
| `/skip` | 跳過目前歌曲 |
| `/pause` | 暫停播放 |
| `/resume` | 繼續播放 |
| `/queue` | 查看播放清單 |
| `/loop [模式]` | 設定循環模式（無/單曲/清單）|
| `/volume [0-200]` | 調整音量 |
| `/stop` | 停止播放並離開語音頻道 |

[查看所有指令 →]({{ '/zh-TW/commands/' | relative_url }})

---

## 📚 文件

- [安裝指南]({{ '/zh-TW/installation/' | relative_url }}) - 如何設定 TuneZ
- [指令列表]({{ '/zh-TW/commands/' | relative_url }}) - 所有指令的完整列表
- [自訂播放清單]({{ '/zh-TW/custom-playlist/' | relative_url }}) - 建立和管理播放清單
- [常見問題]({{ '/zh-TW/faq/' | relative_url }}) - 疑難解答

---

## 💬 支援

- **GitHub Issues**：[回報錯誤或請求功能](https://github.com/NotKeKe/TuneZ-Discord-Bot/issues)
- **Discord**：加入我們的社群獲取幫助

---

## 📄 授權

本專案採用 Apache License 2.0 授權 - 詳見 [LICENSE](https://github.com/NotKeKe/TuneZ-Discord-Bot/blob/main/LICENSE) 檔案。

---

<div class="callout callout-info">
  <strong>⭐ 記得給我一顆 Star！</strong><br>
  這是我的動力來源啊！
</div>
