---
layout: default
title: 安装指南
lang: zh-CN
permalink: /zh-CN/installation/
breadcrumb:
  - title: 首页
    url: {{ '/zh-CN/' | relative_url }}
  - title: 安装指南
    url: {{ '/zh-CN/installation/' | relative_url }}
---

# 安装指南

本指南将帮助您在自己的服务器上设定 TuneZ。请选择最适合您的方法。

<div class="callout callout-warning">
  <strong>⚠️ 前置需求：</strong>在继续之前，您需要有一个 Discord Bot Token。如果您还没有，请先查看<a href="{{ '/zh-CN/installation/' | relative_url }}#创建-discord-bot">创建 Discord Bot</a>章节。
</div>

---

## 📋 前置需求

在安装 TuneZ 之前，请确认您有以下条件：

1. **Discord Bot Token** - 在 [Discord 开发者入口网站](https://discord.com/developers/applications) 建立机器人应用程式
2. **Python 3.10+**（使用 uv 方法）
3. **Docker 和 Docker Compose**（使用 Docker 方法）
4. **FFmpeg**（Windows exe 和 Docker 方法通常已包含）

---

## 🚀 安装方式

### 方法一：Windows (.exe) ⭐ 推荐新手使用

在 Windows 上最简单的方式。

#### 步骤：

1. **下载最新版本**

   前往 [Releases](https://github.com/NotKeKe/easy-discord-music-bot/releases) 下载 `.exe` 文件。

2. **执行安装档**

   双击 `windows.exe` 执行。它会自动解压必要的资源。

3. **设定机器人**

   导航到 Roaming 目录：
   ```
   C:\Users\您的使用者名称\AppData\Roaming\Easy Music Bot
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

   - `data/` - 储存自订播放列表、URL 快取等
   - `logs/` - 储存机器人日志用于除错

5. **启动机器人**

   ```bash
   docker compose up -d
   ```

6. **查看日志**

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

## 🔧 创建 Discord Bot

如果您还没有 Discord Bot，请按照以下步骤建立：

### 1. 建立新应用程式

1. 前往 [Discord 开发者入口网站](https://discord.com/developers/applications)
2. 点击「New Application」
3. 为您的应用程式命名（例如「TuneZ」）
4. 点击「Create」

### 2. 建立机器人

1. 在左侧边栏点击「Bot」
2. 点击「Add Bot」
3. 点击「Yes, do it!」

### 3. 取得您的 Token

1. 在「Token」区块下，点击「Reset Token」
2. 复制并保存您的 token（您将无法再次查看！）

<div class="callout callout-danger">
  <strong>🔒 重要：</strong>千万不要分享您的机器人 token！如果有人取得它，他们可以控制您的机器人。
</div>

### 4. 启用必要的 Intents

1. 向下滚动到「Privileged Gateway Intents」区块
2. 启用以下选项：
   - ✅ **PRESENCE INTENT**
   - ✅ **SERVER MEMBERS INTENT**
   - ✅ **MESSAGE CONTENT INTENT**

### 5. 产生邀请连结

1. 前往 **OAuth2 > URL Generator**
2. 选择以下 scopes：
   - ✅ `bot`
   - ✅ `applications.commands`
3. 选择机器人权限：
   - ✅ 发送讯息
   - ✅ 读取讯息历史
   - ✅ 连接（至语音频道）
   - ✅ 说话（在语音频道中）
   - ✅ 使用斜线指令

4. 复制产生的 URL 并在浏览器中开启

5. 选择您想要添加机器人的服务器

---

## ⚙️ 设定

### 环境变数

| 变数 | 必填 | 描述 |
|------|------|------|
| `DISCORD_TOKEN` | 是 | 您的 Discord 机器人 token |
| `OWNER_ID` | 否 | 您的 Discord 使用者 ID（用于拥有者专属指令）|

### 资料储存

执行机器人后，会建立 `data/` 资料夹，包含：

- `custom_lists/` - 自订播放列表储存
- `url_cache/` - YouTube URL 快取

---

## 🐛 疑难排解

### 机器人无法启动？

1. 检查您的 `DISCORD_TOKEN` 是否正确
2. 确认您已启用所有必要的 intents
3. 查看日志中的错误讯息

### 语音连接问题？

1. 确认机器人有连接和说话的权限
2. 检查 FFmpeg 是否已安装（音频播放所需）

### 音乐无法播放？

1. 确认您在语音频道中
2. 检查 YouTube URL 是否可存取
3. 尝试使用不同的关键字（歌曲名称而非 URL）

---

## 📚 下一步

现在您已经安装好 TuneZ 了，请查看：

- [指令列表]({{ '/zh-CN/commands/' | relative_url }}) - 学习所有可用指令
- [自订播放列表]({{ '/zh-CN/custom-playlist/' | relative_url }}) - 建立您自己的播放列表
- [常见问题]({{ '/zh-CN/faq/' | relative_url }}) - 常见问题和解答
