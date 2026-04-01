---
layout: default
title: 指令列表
lang: zh-CN
permalink: /zh-CN/commands/
breadcrumb:
  - title: 首页
    url: /zh-CN/
  - title: 指令列表
    url: /zh-CN/commands/
---

# 指令列表

TuneZ 所有可用指令的完整列表。

<div class="callout callout-info">
  <strong>💡 说明：</strong>所有指令都可以使用斜线指令（`/`）或前缀（`$`）格式。范例中会显示两种格式。
</div>

---

## 📖 前言

<details>
<summary><strong>为什么要做这个？</strong></summary>

前阵子有个朋友跟我要了[音汐](https://github.com/NotKeKe/Discord-Bot-YinXi)，我后来看了[YEE式机器龙](https://yeecord.com/)的[帖子](https://yeecord.com/blog/thats-why-i-gave-up-on-music)后才知道，原来现在的音乐机器人已经困难成这样了。

又因为我其实原本就有音汐了，我就想着我如果把他关于音乐的代码专门分出来做音乐机器人，~~会不会火~~。

何况现在 yt-dlp 如果一直从同一个 ip 发送请求的话，也很容易出现 403(没有权限)或者其他错误的请求。~~(这大概也是为什么音乐机器人越来越少的原因，毕竟稳定的来源确实挺难找的)~~

但如果每个使用者都只是根据自己的需求去自建 discord bot，是不是就可以解决这个问题？

所以说我做了这个 TuneZ。
</details>

---

## 🎵 音乐播放

### /play

播放音乐或將歌曲加入播放列表。

| 格式 | 说明 |
|------|------|
| `/play [关键字]` | 播放音乐或加入播放列表 |
| `$play [关键字]` | 同上 |
| `$p [关键字]` | 简写 |

**参数：**

| 参数 | 类型 | 说明 |
|------|------|------|
| `query` | 字串 | 歌曲名称、YouTube 网址或播放列表网址 |

**范例：**
```
/play 给你满满
/play https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

<div class="callout callout-info">
  <strong>💡 提示：</strong>当歌曲正在播放时，使用 `/play` 会自动加入播放列表，而不是开始新的播放器。
</div>

---

### /add

將歌曲加入播放列表，但不开始播放。

| 格式 | 说明 |
|------|------|
| `/add [关键字]` | 加入歌曲到播放列表 |
| `$add [关键字]` | 同上 |

**参数：**

| 参数 | 类型 | 说明 |
|------|------|------|
| `query` | 字串 | 歌曲名称或 YouTube 网址 |

---

### /skip

跳过当前的歌曲。

| 格式 | 说明 |
|------|------|
| `/skip` | 跳到下一首歌曲 |
| `$skip` | 同上 |
| `$s` | 简写 |

---

### /back

回到上一首歌曲。

| 格式 | 说明 |
|------|------|
| `/back` | 播放上一首歌曲 |
| `$back` | 同上 |

---

### /pause

暂停当前的播放。

| 格式 | 说明 |
|------|------|
| `/pause` | 暂停音乐 |
| `$pause` | 同上 |
| `$ps` | 简写 |

---

### /resume

继续已暂停的播放。

| 格式 | 说明 |
|------|------|
| `/resume` | 继续播放音乐 |
| `$resume` | 同上 |
| `$rs` | 简写 |

---

### /stop

停止播放并离开语音频道。

| 格式 | 说明 |
|------|------|
| `/stop` | 停止并断开连接 |
| `$stop` | 同上 |

---

### /loop

设定或切换循环模式。

| 格式 | 说明 |
|------|------|
| `/loop [模式]` | 设定循环模式 |
| `$loop [模式]` | 同上 |

**循环模式：**

| 模式 | 说明 |
|------|------|
| `none` | 不循环（预设）|
| `single` | 循环当前的歌曲 |
| `list` | 循环整个播放列表 |

---

### /nowplaying

显示当前正在播放的歌曲。

| 格式 | 说明 |
|------|------|
| `/nowplaying` | 显示当前的歌曲 |
| `$nowplaying` | 同上 |
| `$np` | 简写 |
| `$now` | 简写 |

---

### /queue

显示当前的播放列表。

| 格式 | 说明 |
|------|------|
| `/queue` | 显示播放列表 |
| `$queue` | 同上 |
| `$q` | 简写 |

---

### /remove

从播放列表中移除特定歌曲。

| 格式 | 说明 |
|------|------|
| `/remove [编号]` | 依编号移除歌曲 |
| `$remove [编号]` | 同上 |
| `$rm [编号]` | 简写 |

**参数：**

| 参数 | 类型 | 说明 |
|------|------|------|
| `number` | 整数 | 歌曲在播放清单中的位置（可用 `/queue` 查看）|

---

### /clear

清除播放列表中的所有歌曲。

| 格式 | 说明 |
|------|------|
| `/clear` | 清除播放列表 |
| `$clear` | 同上 |
| `$cq` | 简写 |

<div class="callout callout-warning">
  <strong>⚠️ 注意：</strong>输入此指令后，您必须点击 ✅ 按钮确认。
</div>

---

### /leave

离开语音频道（等同于 `/stop`）。

| 格式 | 说明 |
|------|------|
| `/leave` | 离开频道 |
| `$leave` | 同上 |

---

### /volume

调整音量或显示音量控制。

| 格式 | 说明 |
|------|------|
| `/volume [0-200]` | 设定音量 |
| `$volume [0-200]` | 同上 |

**参数：**

| 参数 | 类型 | 说明 |
|------|------|------|
| `volume` | 整数 | 音量等级（0-200，预设：100）|

---

## 🎛️ 互动按钮

播放音乐时，您可以使用互动按钮：

| 按钮 | 功能 |
|------|------|
| ⏮️ Previous | 播放上一首 |
| ⏯️ Pause/Resume | 切换播放/暂停 |
| ⏭️ Next | 跳到下一首 |
| ⏹️ Stop | 停止并离开 |
| 🔁 Loop | 切换循环模式 |
| 📋 Queue | 显示播放列表 |
| 🔄 Refresh | 刷新歌曲资讯 |
| 🔊 Volume | 显示音量控制 |

---

## 📝 自订播放列表

详见[自订播放列表指南](/zh-CN/custom-playlist/)。

| 指令 | 说明 |
|------|------|
| `/play_custom_list` | 播放已储存的播放列表 |
| `/add_custom_list` | 将歌曲加入播放列表 |
| `/show_custom_list` | 查看播放列表歌曲 |
| `/delete_custom_list` | 删除播放列表 |
| `/remove_one_from_custom_list` | 永久移除一首歌曲 |

---

## 🌟 特色功能

### 自带浅蓝色动画 emojis

TuneZ 内置精美的浅蓝色动画表情符号，让您的 Discord 体验更美观！

### 可自订 emojis

您可以使用自己的表情符号来替换预设的：

<strong>❗注意图片档案名（不含副档名）要与 `assets/emojis/` 里面的档案名一样❗</strong>

- 在 Windows 当中，进到 `C:\Users\USERNAME\AppData\Roaming\Easy Music Bot\data\emojis` 可以自己放图片上去
- 在其他环境下，可在 `./data/emojis/` 中上传自订图片
- 最后在 Discord 频道里面使用 `/reload_emojis` 来重载 emojis

---

## 📊 指令总览表

| 指令 | 别名 | 说明 |
|------|------|------|
| `/play` | `$p` | 播放音乐 |
| `/add` | - | 加入播放列表 |
| `/skip` | `$s` | 跳过歌曲 |
| `/back` | - | 上一首歌曲 |
| `/pause` | `$ps` | 暂停 |
| `/resume` | `$rs` | 继续 |
| `/stop` | - | 停止并离开 |
| `/loop` | - | 循环模式 |
| `/nowplaying` | `$np`, `$now` | 当前的歌曲 |
| `/queue` | `$q` | 显示播放列表 |
| `/remove` | `$rm` | 移除歌曲 |
| `/clear` | `$cq` | 清除播放列表 |
| `/leave` | - | 离开频道 |
| `/volume` | - | 调整音量 |
| `/play_custom_list` | - | 播放播放列表 |
| `/add_custom_list` | - | 加入播放列表 |
| `/show_custom_list` | - | 显示播放列表 |
| `/delete_custom_list` | - | 删除播放列表 |
| `/emoji` | - | 显示表情符号 |
| `/reload_emojis` | - | 重载表情符号 |
