---
layout: default
title: 常见问题
lang: zh-CN
permalink: /zh-CN/faq/
breadcrumb:
  - title: 主页
    url: /zh-CN/
  - title: 常见问题
    url: /zh-CN/faq/
---

# 常见问题

关于 TuneZ 的常见问题和解答。

---

## ❓ 基本问题

### 什么是 TuneZ？

TuneZ 是一个基于 Python 的 Discord 音乐机器人，可以让您，在 Discord 语音频道中播放 YouTube 音乐。它具有播放列表管理、循环模式和自定义播放列表等功能，开箱即用。

### TuneZ 与其他音乐机器人有什么不同？

- **开箱即用**：最少设定即可运作
- **自架主机**：您可以控制自己的机器人和数据
- **自定义表情符号**：内置精美的动画表情符号，可自由定制
- **多语言支持**：支持英文、繁体中文和简体中文

### 使用 TuneZ 需要付费吗？

不需要，TuneZ 完全免费且开源，采用 Apache License 2.0 授权。

---

## 🔧 安装与设定

### 执行 TuneZ 需要什么？

- Discord Bot Token（可从 Discord 开发者入口网站取得），具体参考[注册 Discord Bot]({{ '/zh-CN/register-discord-bot/' | relative_url }})
- 以下任一环境：
  - Windows 电脑（使用 .exe）
  - 已安装 Docker（使用 Docker）
  - Python 3.10+（使用 uv）

### 我没有 Discord Bot Token，要如何取得？

1. 前往 [Discord 开发者入口网站](https://discord.com/developers/applications)
2. 点击「New Application」并命名
3. 在左侧边栏点击「Bot」
4. 点击「Add Bot」并确认
5. 复制您的 Token（如需重置，点击「Reset Token」）
6. 在「Privileged Gateway Intents」下启用：
   - PRESENCE INTENT
   - SERVER MEMBERS INTENT
   - MESSAGE CONTENT INTENT

详细信息请参阅[注册 Discord Bot]({{ '/zh-CN/register-discord-bot/' | relative_url }})

### 为什么需要启用 intents？

Discord 要求机器人启用特定 intents 才能存取某些功能。TuneZ 需要：
- **Presence Intent**：侦测使用者加入/离开语音频道
- **Server Members Intent**：用于成员相关功能
- **Message Content Intent**：读取指令讯息（prefix 指令）

---

## 🎵 音乐播放

### 为什么音乐无法播放？

检查以下常见问题：

1. **不在语音频道中**：您必须在语音频道中才能使用音乐指令
2. **机器人不在语音频道**：机器人需要连接和说话的权限
3. **无效的网址**：请确认 YouTube 网址正确且可存取
4. **内容被封锁**：某些影片可能受到地区限制或已被移除

### 为什么音讯品质不佳？

这可能是因为：
- 网络连线缓慢
- YouTube 伺服器问题
- 机器人负载过高

### 可以播放 YouTube 播放列表吗？

可以！使用 `/play` 或 `/add` 时，您可以贴上 YouTube 播放列表网址。

### TuneZ 支持 Spotify/Apple Music 吗？

目前 TuneZ 仅直接支持 YouTube。但是您可以：
- 找到歌曲的 YouTube 连结
- 使用 YouTube 网址建立自定义播放列表

---

## 🔁 循环与播放列表

### 循环模式有什么不同？

| 模式 | 说明 |
|------|------|
| `none` | 不循环 - 播放列表播放一次 |
| `single` | 循环目前的歌曲 |
| `list` | 循环整个播放列表 |

### 我可以从播放列表中移除歌曲吗？

可以！使用 `/remove [编号]`，其中编号是歌曲在播放列表中的位置（可用 `/queue` 查看）。

### 播放列表播放完毕后会发生什么？

当播放列表中的所有歌曲都播放完毕后，机器人会自动离开语音频道。

---

## 🎨 自订功能

### 可以使用自己的表情符号吗？

可以！将您的自定义表情符号图片放在：
- **Windows**：`C:\Users\USERNAME\AppData\Roaming\Easy Music Bot\data\emojis`
- **其他环境**：`./data/emojis/`

然后使用 `/reload_emojis custom` 来载入。

<div class="callout callout-info">
  <strong>📝 文件命名：</strong>图片档名（不含副档名）必须与 `assets/emojis/` 中的表情符号名称相符。例如：`list.gif` → `list.png`
</div>

### 有哪些表情符号可以自定义？

可自定义的表情符号包括：
- `play`、`pause`、`stop`
- `next`、`previous`
- `volume`、`refresh`
- `loop`、`list`
- 等等...

---

## 🛡️ 隐私与安全

### 我的数据安全吗？

- **自架主机**：您的数据会留在您自己的伺服器上
- **自定义播放列表**：储存在本机的 `data/` 文件夹中
- **URL 快取**：用于加快播放速度的临时储存

### 谁可以使用机器人？

只有已安装机器人的伺服器上的使用者才能使用它。您的个人资料除了 Discord API 外不会传送到任何地方。

### 关于 Bot Token？

- 千万不要分享您的 Bot Token
- 如果外泄，请立即从 Discord 开发者入口网站重新产生
- Token 只允许控制您的机器人，无法存取您的 Discord 帐号

---

## 🐛 疑难排解

### 机器人无法启动

1. 检查 `.env` 中的 `DISCORD_TOKEN` 是否正确
2. 确认所有 intents 都已启用
3. 查看主控台中的错误讯息

### 机器人已加入语音频道但没有声音

1. 检查机器人是否有「连接」和「说话」权限
2. 确认 FFmpeg 已安装（音讯解码所需）
3. 尝试使用 `/volume` 增加音量

### 指令没有作用

1. 确认您使用的是正确的格式（`/指令` 或 `$指令`）
2. 检查您是否需要在语音频道中
3. 尝试重新启动机器人

### 显示「Something went wrong」错误

这通常表示：
- YouTube 封锁了请求（请尝试其他影片）
- 网络问题（请检查您的连线）
- 机器人受到 rate-limit（请稍后再试）

---

## 💬 取得帮助

### 我可以在哪里获得支持？

- **GitHub Issues**：[回报错误](https://github.com/NotKeKe/TuneZ-Discord-Bot/issues)

### 如何回报错误？

请在 GitHub 上开启 issue，包含：
1. 您的作业系统
2. 您如何安装 TuneZ（exe/docker/uv）
3. 准确的错误讯息
4. 重现问题的步骤

### 可以请求新功能吗？

可以！在 GitHub Issues 上开启功能请求。我们非常感谢所有建议！

---

## 📄 授权

见 [授权]({{ '/zh-CN/#license' | relative_url }})
