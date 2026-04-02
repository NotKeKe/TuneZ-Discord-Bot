---
layout: default
title: 安装指南
lang: zh-CN
permalink: /zh-CN/installation/
breadcrumb:
  - title: 主页
    url: /zh-CN/
  - title: 安装指南
    url: /zh-CN/installation/
---

# 安装指南

本指南将帮助您在自己的伺服器上设定 TuneZ。请选择最适合您的方法。

<div class="callout callout-warning">
  <strong>⚠️ 前置需求：</strong>在继续之前，您需要有一个 Discord Bot Token。如果您还没有，请先查看<a href="{{ '/zh-CN/register-discord-bot/' | relative_url }}">注册 Discord Bot</a>指南。
</div>

---

## 📋 前置需求

在安装 TuneZ 之前，请确认您有以下条件：

1. **Discord Bot Token** - 在 [Discord 开发者入口网站](https://discord.com/developers/applications) 建立机器人
2. **Python 3.10+**（使用 uv）
3. **Docker 和 Docker Compose**（使用 Docker）
4. **FFmpeg**（Windows exe 和 Docker 通常已包含）

---

## 🚀 安装方式

### 方法一：Windows (.exe) ⭐ 推荐新手使用

在 Windows 上最简单的开始方式。

#### 步骤：

1. **下载最新版本**

   前往 [Releases](https://github.com/NotKeKe/easy-discord-music-bot/releases) 下载 `.exe` 档案。

2. **执行安装档**

   双击 `windows.exe` 执行。它会于下一步的目录中，放入必要的资源。

3. **设定机器人**

   导览到 Roaming 目录：
   ```
   C:\Users\您的使用者名称\AppData\Roaming\TuneZ_Discord_Bot
   ```

4. **编辑 `.env` 档案**

   使用任何文字编辑器开启 `.env`，并加入您的 Discord Bot Token：

   ```env
   DISCORD_TOKEN=您的机器人token
   OWNER_ID=您的Discord使用者ID
   ```

   <div class="callout callout-info">
     <strong>💡 提示：</strong>您可以将 `OWNER_ID` 留空。它只用于表情符号重载指令。
   </div>

5. **再次执行机器人**

   再次双击 `windows.exe`。您应该会看到机器人启动了！

6. **测试一下**

   加入语音频道并使用 `/play` 开始播放音乐！
   <br>
   或者使用 `/help` 来取得指令帮助！

---

### 方法二：Docker

推荐给熟悉 Docker 的使用者。

#### 步骤：

1. **克隆专案**

   ```bash
   git clone https://github.com/NotKeKe/TuneZ-Discord-Bot.git
   cd TuneZ-Discord-Bot
   ```

2. **建立 `.env` 档案**

   ```bash
   cp .env.example .env
   ```

3. **编辑 `.env` 档案**

   ```env
   DISCORD_TOKEN=您的机器人token
   OWNER_ID=您的Discord使用者ID
   ```

4. **建立资料目录**

   ```bash
   mkdir -p data logs
   ```

   - `data/` - 储存自定义播放列表、URL 快取等
   - `logs/` - 储存机器人日志用于除错

5. **启动机器人**

   ```bash
   docker compose up -d
   ```

6. **查看日志 (可选)**

   ```bash
   docker compose logs -f
   ```

<div class="callout callout-success">
  <strong>✅ 成功！</strong>机器人应该已经启动并运行了！
</div>

---

### 方法三：uv (Python)

适合喜欢直接执行 Python 的开发者。

#### 前置需求：

- Python 3.10 或更高版本
- [uv](https://github.com/astral-sh/uv) 套件管理器

#### 安装方式：

1. **安装 uv**

   使用 pip：
   ```bash
   pip install uv
   ```

   或使用安装脚本：
   ```bash
   # Windows
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # macOS / Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

   或查看 uv 官方的[安装教学](https://docs.astral.sh/uv/getting-started/installation/)：
   ```
   https://docs.astral.sh/uv/getting-started/installation/
   ```

2. **克隆专案**

   ```bash
   git clone https://github.com/NotKeKe/TuneZ-Discord-Bot.git
   cd TuneZ-Discord-Bot
   ```

3. **建立 `.env` 档案**

   ```bash
   cp .env.example .env
   ```

4. **编辑 `.env` 档案**

   ```env
   DISCORD_TOKEN=您的机器人token
   OWNER_ID=您的Discord使用者ID
   ```

5. **同步依赖**

   ```bash
   uv sync
   ```

6. **执行机器人**

   ```bash
   uv run main.py
   ```

---

## ⚙️ 设定

### 环境变数

| 变数 | 必填 | 描述 |
|------|------|------|
| `DISCORD_TOKEN` | 是 | 您的 Discord 机器人 token |
| `OWNER_ID` | 否 | 您的 Discord 使用者 ID（用于拥有者专属指令）|

---

## 📚 下一步

现在您已经安装好 TuneZ了，请查看：

- [指令列表]({{ '/zh-CN/commands/' | relative_url }}) - 学习所有可用指令
- [自定义播放列表]({{ '/zh-CN/custom-playlist/' | relative_url }}) - 建立您自己的播放列表
- [常见问题]({{ '/zh-CN/faq/' | relative_url }}) - 常见问题和解答
