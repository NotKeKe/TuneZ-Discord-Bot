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

## 📖 前言
<details>
    <summary>為什麼要做這個?</summary>
    <ul>
        <li>
            前陣子有個朋友跟我要了<a href="https://github.com/NotKeKe/Discord-Bot-YinXi">音汐</a>，我後來看了<a href="https://yeecord.com/">YEE式機器龍</a>的<a href="https://yeecord.com/blog/thats-why-i-gave-up-on-music">貼文</a>後才知道，原來現在的音樂機器人已經困難成這樣了
        </li>
        <li>
            又因為我其實原本就有音汐了，我就想著 我如果把他關於音樂的代碼專門分出來 做音樂機器人，<del>會不會火</del>
        </li>
        <li>
            何況現在 yt-dlp 如果一直從同一個 ip 發送請求的話，也很容易出現 403(沒有權限)或者其他錯誤的請求 <del>(這大概也是為什麼音樂機器人越來越少的原因，畢竟穩定的來源確實滿難找的)</del><br>
            但如果每個使用者都只是根據自己的需求 去自架 discord bot，是不是就可以解決這個問題
        </li>
        <li>
            所以說我就做了這個 TuneZ
        </li>
    </ul>
</details>
<details>
    <summary>為什麼叫 TuneZ</summary>
    <ul>
        <li>
            其實原因超簡單
        </li>
        <li>
            我先隨便讓Copilot幫我想個名字，出現了 Tune。 <br>
            後來想想，大約2000年左右的人都會被稱作 Z 世代 <br>
            所以又出現了 Z <br>
            節合起來就變成 <strong>TuneZ</strong> 了
        </li>
    </ul>
</details>
<details>
    <summary>會不會有風險?</summary>
    <ul>
        <li>
            答案其實也很簡單 自己使用就不會有
        </li>
        <li>
            這種東西通常自己 或者讓朋友用一下都不會出啥事
        </li>
        <li>
            除非你選擇把他拿去營利 <br>
            那就不能怪我了:) <br>
            我沒考慮負責
        </li>
    </ul>
</details>

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
    <div class="feature-icon">📋</div>
    <h3>自訂播放清單</h3>
    <p>可以自己透過單一 YouTube 連結，自訂名稱並創建專屬播放清單。</p>
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

### 方法二：自架機器人 (推薦)

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

- [創建 Discord Bot]({{ '/zh-TW/register-discord-bot/' | relative_url }}) - 如何創建一個 Discord Bot
- [安裝指南]({{ '/zh-TW/installation/' | relative_url }}) - 如何設定 TuneZ
- [指令列表]({{ '/zh-TW/commands/' | relative_url }}) - 所有指令的完整列表
- [自訂播放清單]({{ '/zh-TW/custom-playlist/' | relative_url }}) - 建立和管理播放清單
- [常見問題]({{ '/zh-TW/faq/' | relative_url }}) - 疑難解答

---

## 💬 支援

- **GitHub Issues**：[回報錯誤或請求功能](https://github.com/NotKeKe/TuneZ-Discord-Bot/issues)
  - 無論是程式大佬、技術小白，遇到任何問題，或是希望可以新增功能，都可以來這裡提交 Issue

---

<div id=license></div>

## 📄 授權

TuneZ 採用 Apache License 2.0 授權。您可以：
- ✅ 將專案代碼用於個人或商業目的
- ✅ 修改和自訂
- ✅ 分發

您不能：
- ❌ 讓作者承擔責任
- ❌ 使用該名稱進行代言

詳見 [LICENSE](https://github.com/NotKeKe/TuneZ-Discord-Bot/blob/main/LICENSE)。

<div class="callout callout-danger">
  <strong>❗ 本專案作者不受理或承擔任何使用者因使用該專案，而造成的法律後果或侵權行為。</strong>
</div>

---

<div class="callout callout-info">
  <strong>⭐ 記得給我一顆 Star！</strong><br>
  這是我的動力來源啊！
</div>
