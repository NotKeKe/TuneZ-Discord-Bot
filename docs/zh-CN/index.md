---
layout: default
title: 首页
lang: zh-CN
permalink: /zh-CN/
---

# TuneZ Discord 音乐机器人

<p align="center">
  <img src="{{ '/assets/icon.png' | relative_url }}" alt="TuneZ Logo" width="150" height="150">
</p>

<p align="center">
  一个基于 Python，每个需要在 Discord 播放音乐的人都可以<strong>开箱即用</strong>的 Discord 音乐机器人。
</p>

<p align="center">
  <a href="https://github.com/NotKeKe/TuneZ-Discord-Bot/stargazers">
    <img src="https://img.shields.io/github/stars/NotKeKe/TuneZ-Discord-Bot?style=social" alt="Stars">
  </a>
  <a href="https://github.com/NotKeKe/TuneZ-Discord-Bot/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-Apache%20License%202.0-yellow" alt="License">
  </a>
  <a href="https://discord.com/oauth2/authorize?client_id=990798785489825813">
    <img src="https://img.shields.io/badge/邀请-Discord-5865F2?style=flat" alt="Discord">
  </a>
</p>

---

## ✨ 特色

<div class="feature-grid">
  <div class="feature-card">
    <div class="feature-icon">🎵</div>
    <h3>音乐播放</h3>
    <p>从 YouTube 播放高品质音频流，播放流畅。</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">📋</div>
    <h3>播放列表管理</h3>
    <p>完整控制播放列表，包括新增、移除、跳过、清空等功能。</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🔁</div>
    <h3>循环模式</h3>
    <p>多种循环选项：无循环、单曲循环、播放列表循环。</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🎨</div>
    <h3>自订表情符号</h3>
    <p>内置精美的浅蓝色动画表情符号，也可以自定义！</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🌐</div>
    <h3>多语言支持</h3>
    <p>支持英文、繁体中文、简体中文。</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🚀</div>
    <h3>简单易上手</h3>
    <p>开箱即用！支持 Windows exe、Docker、Python 等多种方式。</p>
  </div>
</div>

---

## 📖 快速开始

### 方法一：邀请机器人

如果您只是想要一个 Discord 音乐机器人，可以直接邀请[音汐](https://github.com/NotKeKe/Discord-Bot-YinXi)到您的服务器。

[![邀请机器人](https://img.shields.io/badge/邀请-音汐-5865F2?style=for-the-badge)](https://discord.com/oauth2/authorize?client_id=990798785489825813)

### 方法二：自建机器人

想要更多控制权和功能？自己架设 TuneZ：

1. **Windows**：从 [Releases](https://github.com/NotKeKe/easy-discord-music-bot/releases) 下载 `.exe` 文件
2. **Docker**：`docker compose up -d`
3. **Python**：`uv run main.py`

查看[安装指南](/zh-CN/installation/)获取详细说明。

---

## 🎮 Demo 展示

![Demo]({{ '/assets/demo.png' | relative_url }})

*TuneZ 有支持中文，只是因为 Discord 默认语言是英文，所以显示英文。*

---

## 🛠️ 可用指令

| 指令 | 描述 |
|------|------|
| `/play [关键字]` | 播放音乐或加入播放列表 |
| `/skip` | 跳过当前歌曲 |
| `/pause` | 暂停播放 |
| `/resume` | 继续播放 |
| `/queue` | 查看播放列表 |
| `/loop [模式]` | 设置循环模式（无/单曲/列表）|
| `/volume [0-200]` | 调整音量 |
| `/stop` | 停止播放并离开语音频道 |

[查看所有指令 →](/zh-CN/commands/)

---

## 📚 文档

- [安装指南](/zh-CN/installation/) - 如何设定 TuneZ
- [指令列表](/zh-CN/commands/) - 所有指令的完整列表
- [自订播放列表](/zh-CN/custom-playlist/) - 建立和管理播放列表
- [常见问题](/zh-CN/faq/) - 疑难解答

---

## 💬 支持

- **GitHub Issues**：[回报错误或请求功能](https://github.com/NotKeKe/TuneZ-Discord-Bot/issues)
- **Discord**：加入我们的社群获取帮助

---

## 📄 授权

本项目采用 Apache License 2.0 授权 - 详见 [LICENSE](https://github.com/NotKeKe/TuneZ-Discord-Bot/blob/main/LICENSE) 文件。

---

<div class="callout callout-info">
  <strong>⭐ 记得给我一颗 Star！</strong><br>
  这是我的动力来源啊！
</div>
