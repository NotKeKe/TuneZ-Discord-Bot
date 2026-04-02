---
layout: default
title: 主页
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

## 📖 前言
<details>
    <summary>为什么做这个？</summary>
    <ul>
        <li>
            前阵子有个朋友跟我要了<a href="https://github.com/NotKeKe/Discord-Bot-YinXi">音汐</a>，我后来看了<a href="https://yeecord.com/">YEE式机器龙</a>的<a href="https://yeecord.com/blog/thats-why-i-gave-up-on-music">文章</a>后才知道，原来现在的音乐机器人已经困难成这样了
        </li>
        <li>
            又因为我其实原本就有音汐了，我就想着 我如果把他关于音乐的代码专门分出来 做音乐机器人，<del>会不会火</del>
        </li>
        <li>
           何况现在 yt-dlp 如果一直从同一个 ip 发送请求的话，也很容易出现 403(没有权限)或者其他错误的请求 <del>(这大概也是为什么音乐机器人越来越少的原因，毕竟稳定的来源确实满难找的)</del><br>
            但如果每个使用者都只是根据自己的需求 去自架 discord bot，是不是就可以解决这个问题
        </li>
        <li>
            所以说我就做了这个 TuneZ
        </li>
    </ul>
</details>
<details>
    <summary>为什么叫 TuneZ</summary>
    <ul>
        <li>
            其实原因超简单
        </li>
        <li>
            我先随便让Copilot帮我想个名字，出现了 Tune。 <br>
            后来想想，大约2000年左右的人都会被称作 Z 世代 <br>
            所以又出现了 Z <br>
            节合起来就变成 <strong>TuneZ</strong> 了
        </li>
    </ul>
</details>
<details>
    <summary>会不会有风险？</summary>
    <ul>
        <li>
            答案其实也很简单 自己使用就不会有
        </li>
        <li>
            这种东西通常自己 或者让朋友用一下都不会出啥事
        </li>
        <li>
            除非你选择把他拿去营利 <br>
            那就不能怪我了:) <br>
            我没考虑负责
        </li>
    </ul>
</details>

## ✨ 特色

<div class="feature-grid">
  <div class="feature-card">
    <div class="feature-icon">🎵</div>
    <h3>音乐播放</h3>
    <p>从 YouTube 播放高品质音讯串流，播放流畅。</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">📋</div>
    <h3>播放列表管理</h3>
    <p>完整控制播放列表，包括新增、移除、跳过、清空等功能。</p>
  </div>

  <div class="feature-card">
    <div class="feature-icon">📋</div>
    <h3>自定义播放列表</h3>
    <p>可以自己透过单一 YouTube 连结，自订名称并创建专属播放列表。</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🔁</div>
    <h3>循环模式</h3>
    <p>多种循环选项：无循环、单曲循环、播放列表循环。</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🎨</div>
    <h3>自定义表情符号</h3>
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

如果您只是想要一个 Discord 音乐机器人，可以直接邀请[音汐](https://github.com/NotKeKe/Discord-Bot-YinXi)到您的伺服器。

[![邀请机器人](https://img.shields.io/badge/邀请-音汐-5865F2?style=for-the-badge)](https://discord.com/oauth2/authorize?client_id=990798785489825813)

### 方法二：自架机器人 (推荐)

想要更多控制权和功能？自己架设 TuneZ：

1. **Windows**：从 [Releases](https://github.com/NotKeKe/easy-discord-music-bot/releases) 下载 `.exe` 档案
2. **Docker**：`docker compose up -d`
3. **Python**：`uv run main.py`

查看[安装指南]({{ '/zh-CN/installation/' | relative_url }})获取详细说明。

---

## 🎮 Demo 展示

![Demo]({{ '/assets/demo.png' | relative_url }})

*TuneZ 有支持中文，只是因为 Discord 默认语言是英文，所以显示英文。*

---

## 🛠️ 可用指令

| 指令 | 描述 |
|------|------|
| `/play [关键字]` | 播放音乐或加入播放列表 |
| `/skip` | 跳过目前歌曲 |
| `/pause` | 暂停播放 |
| `/resume` | 继续播放 |
| `/queue` | 查看播放列表 |
| `/loop [模式]` | 设定循环模式（无/单曲/列表）|
| `/volume [0-200]` | 调整音量 |
| `/stop` | 停止播放并离开语音频道 |

[查看所有指令 →]({{ '/zh-CN/commands/' | relative_url }})

---

## 📚 文件

- [创建 Discord Bot]({{ '/zh-CN/register-discord-bot/' | relative_url }}) - 如何创建一个 Discord Bot
- [安装指南]({{ '/zh-CN/installation/' | relative_url }}) - 如何设定 TuneZ
- [指令列表]({{ '/zh-CN/commands/' | relative_url }}) - 所有指令的完整列表
- [自定义播放列表]({{ '/zh-CN/custom-playlist/' | relative_url }}) - 建立和管理播放列表
- [常见问题]({{ '/zh-CN/faq/' | relative_url }}) - 疑难解答

---

## 💬 支持

- **GitHub Issues**：[回报错误或请求功能](https://github.com/NotKeKe/TuneZ-Discord-Bot/issues)
  - 无论是程式大佬、技术小白，遇到任何问题，或是希望可以新增功能，都可以来这里提交 Issue

---

<div id=license></div>

## 📄 授权

TuneZ 采用 Apache License 2.0 授权。您可以：
- ✅ 将专案代码用于个人或商业目的
- ✅ 修改和自订
- ✅ 分发

您不能：
- ❌ 让作者承担责任
- ❌ 使用该名称进行代言

详见 [LICENSE](https://github.com/NotKeKe/TuneZ-Discord-Bot/blob/main/LICENSE)。

<div class="callout callout-danger">
  <strong>❗ 本专案作者不受理或承担任何使用者因使用该专案，而造成的法律后果或侵权行为。</strong>
</div>

---

<div class="callout callout-info">
  <strong>⭐ 记得给我一颗 Star！</strong><br>
  这是我的动力来源啊！
</div>
