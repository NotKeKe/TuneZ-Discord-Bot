---
layout: default
title: 指令列表
lang: zh-TW
permalink: /zh-TW/commands/
breadcrumb:
  - title: 主頁
    url: /zh-TW/
  - title: 指令列表
    url: /zh-TW/commands/
---

# 指令列表

TuneZ 所有可用指令的完整列表。

<div class="callout callout-info">
  <strong>💡 說明：</strong>所有指令都可以使用斜線指令（`/`）或前綴（`$`）格式。範例中會顯示兩種格式。
</div>

---

## 📖 前言

<details>
<summary><strong>為什麼要做這個？</strong></summary>

前陣子有個朋友跟我要了[音汐](https://github.com/NotKeKe/Discord-Bot-YinXi)，我後來看了[YEE式機器龍](https://yeecord.com/)的[貼文](https://yeecord.com/blog/thats-why-i-gave-up-on-music)後才知道，原來現在的音樂機器人已經困難成這樣了。

又因為我其實原本就有音汐了，我就想著我如果把他關於音樂的代碼專門分出來做音樂機器人，~~會不會火~~。

何況現在 yt-dlp 如果一直從同一個 ip 發送請求的話，也很容易出現 403(沒有權限)或者其他錯誤的請求。~~(這大概也是為什麼音樂機器人越來越少的原因，畢竟穩定的來源確實滿難找的)~~

但如果每個使用者都只是根據自己的需求去自架 discord bot，是不是就可以解決這個問題？

所以說我就做了這個 TuneZ。
</details>

---

## 🎵 音樂播放

### /play

播放音樂或將歌曲加入播放清單。

| 格式 | 說明 |
|------|------|
| `/play [關鍵字]` | 播放音樂或加入播放清單 |
| `$play [關鍵字]` | 同上 |
| `$p [關鍵字]` | 簡寫 |

**參數：**
| 參數 | 類型 | 說明 |
|------|------|------|
| `query` | 字串 | 歌曲名稱、YouTube 網址或播放清單網址 |

**範例：**
```
/play 給你默默
/play https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

<div class="callout callout-info">
  <strong>💡 提示：</strong>當歌曲正在播放時，使用 `/play` 會自動加入播放清單，而不是開始新的播放器。
</div>

---

### /add

將歌曲加入播放清單，但不開始播放。

| 格式 | 說明 |
|------|------|
| `/add [關鍵字]` | 加入歌曲到播放清單 |
| `$add [關鍵字]` | 同上 |

**參數：**
| 參數 | 類型 | 說明 |
|------|------|------|
| `query` | 字串 | 歌曲名稱或 YouTube 網址 |

---

### /skip

跳過目前的歌曲。

| 格式 | 說明 |
|------|------|
| `/skip` | 跳到下一首歌曲 |
| `$skip` | 同上 |
| `$s` | 簡寫 |

---

### /back

回到上一首歌曲。

| 格式 | 說明 |
|------|------|
| `/back` | 播放上一首歌曲 |
| `$back` | 同上 |

---

### /pause

暫停目前的播放。

| 格式 | 說明 |
|------|------|
| `/pause` | 暫停音樂 |
| `$pause` | 同上 |
| `$ps` | 簡寫 |

---

### /resume

繼續已暫停的播放。

| 格式 | 說明 |
|------|------|
| `/resume` | 繼續播放音樂 |
| `$resume` | 同上 |
| `$rs` | 簡寫 |

---

### /stop

停止播放並離開語音頻道。

| 格式 | 說明 |
|------|------|
| `/stop` | 停止並斷開連接 |
| `$stop` | 同上 |

---

### /loop

設定或切換循環模式。

| 格式 | 說明 |
|------|------|
| `/loop [模式]` | 設定循環模式 |
| `$loop [模式]` | 同上 |

**參數：**
| 參數 | 類型 | 說明 |
|------|------|------|
| `mode` | 字串 | 循環模式：`none`、`single` 或 `list` |

**循環模式：**
| 模式 | 說明 |
|------|------|
| `none` | 不循環（預設）|
| `single` | 循環目前的歌曲 |
| `list` | 循環整個播放清單 |

**範例：**
```
/loop single    # 循環目前的歌曲
/loop list      # 循環整個播放清單
/loop           # 循環切換各模式
```

---

### /nowplaying

顯示目前正在播放的歌曲。

| 格式 | 說明 |
|------|------|
| `/nowplaying` | 顯示目前的歌曲 |
| `$nowplaying` | 同上 |
| `$np` | 簡寫 |
| `$now` | 簡寫 |

---

### /queue

顯示目前的播放清單。

| 格式 | 說明 |
|------|------|
| `/queue` | 顯示播放清單 |
| `$queue` | 同上 |
| `$q` | 簡寫 |

---

### /remove

從播放清單中移除特定歌曲。

| 格式 | 說明 |
|------|------|
| `/remove [編號]` | 依編號移除歌曲 |
| `$remove [編號]` | 同上 |
| `$rm [編號]` | 簡寫 |

**參數：**
| 參數 | 類型 | 說明 |
|------|------|------|
| `number` | 整數 | 歌曲在播放清單中的位置（可用 `/queue` 查看）|

**範例：**
```
/queue        # 查看播放清單，歌曲會被編號 1, 2, 3...
/remove 2     # 移除第 2 首歌曲
```

---

### /clear

清除播放清單中的所有歌曲。

| 格式 | 說明 |
|------|------|
| `/clear` | 清除播放清單 |
| `$clear` | 同上 |
| `$cq` | 簡寫 |

<div class="callout callout-warning">
  <strong>⚠️ 注意：</strong>輸入此指令後，您必須點擊 ✅ 按鈕確認。
</div>

---

### /leave

離開語音頻道（等同於 `/stop`）。

| 格式 | 說明 |
|------|------|
| `/leave` | 離開頻道 |
| `$leave` | 同上 |

---

### /volume

調整音量或顯示音量控制。

| 格式 | 說明 |
|------|------|
| `/volume [0-200]` | 設定音量 |
| `$volume [0-200]` | 同上 |

**參數：**
| 參數 | 類型 | 說明 |
|------|------|------|
| `volume` | 整數 | 音量等級（0-200，預設：100）|

**範例：**
```
/volume        # 顯示音量控制按鈕
/volume 50     # 設定音量為 50%
/volume 150    # 設定音量為 150%
```

---

## 🎛️ 互動按鈕

播放音樂時，您可以使用互動按鈕：

| 按鈕 | 功能 |
|------|------|
| ⏮️ Previous | 播放上一首 |
| ⏯️ Pause/Resume | 切換播放/暫停 |
| ⏭️ Next | 跳到下一首 |
| ⏹️ Stop | 停止並離開 |
| 🔁 Loop | 切換循環模式 |
| 📋 Queue | 顯示播放清單 |
| 🔄 Refresh | 刷新歌曲資訊 |
| 🔊 Volume | 顯示音量控制 |

---

## 📝 自訂播放清單

詳見[自訂播放清單指南](/zh-TW/custom-playlist/)。

| 指令 | 說明 |
|------|------|
| `/play_custom_list` | 播放已儲存的播放清單 |
| `/add_custom_list` | 將歌曲加入播放清單 |
| `/show_custom_list` | 查看播放清單歌曲 |
| `/delete_custom_list` | 刪除播放清單 |
| `/remove_one_from_custom_list` | 永久移除一首歌曲 |

---

## 🛠️ 工具指令

### /help

顯示基本幫助資訊。

| 格式 | 說明 |
|------|------|
| `/help` | 顯示幫助 |

---

### /emoji

顯示 TuneZ 內建的表情符號。

| 格式 | 說明 |
|------|------|
| `/emoji [名稱]` | 依名稱顯示表情符號 |
| `$emoji [名稱]` | 同上 |

**參數：**
| 參數 | 類型 | 說明 |
|------|------|------|
| `name` | 字串 | 表情符號名稱（例如 `next`、`stop`、`refresh`）|

**範例：**
```
/emoji next      # 顯示 "next" 表情符號
/emoji pause     # 顯示 "pause" 表情符號
```

---

### /reload_emojis

重載表情符號資源（僅擁有者可用）。

| 格式 | 說明 |
|------|------|
| `/reload_emojis [類型]` | 重載表情符號 |
| `$reload_emojis [類型]` | 同上 |

**參數：**
| 參數 | 類型 | 說明 |
|------|------|------|
| `type` | 字串 | `all`、`default` 或 `custom` |

<div class="callout callout-info">
  <strong>🔧 自訂表情符號：</strong>將您的自訂表情符號圖片放在 `data/emojis/` 資料夾（或 Windows 上的 `C:\Users\USERNAME\AppData\Roaming\Easy Music Bot\data\emojis`）。然後使用 `/reload_emojis custom` 來載入。
</div>

---

## 🌟 特色功能

### 自帶淺藍色動畫 emojis

TuneZ 內建精美的淺藍色動畫表情符號，讓您的 Discord 體驗更美觀！

### 可自訂 emojis

您可以使用自己的表情符號來替換預設的：

<strong>❗注意圖片檔名（不含副檔名）要與 `assets/emojis/` 裡面的檔名一樣❗</strong>

**範例：** `list.gif` → `list.png`

- 在 Windows 當中，進到 `C:\Users\USERNAME\AppData\Roaming\Easy Music Bot\data\emojis` 可以自己放圖片上去
- 在其他環境下，可在 `./data/emojis/` 中上傳自訂圖片
- 最後在 Discord 頻道裡面使用 `/reload_emojis` 來重載 emojis

---

## 📊 指令總覽表

| 指令 | 別名 | 說明 |
|------|------|------|
| `/play` | `$p` | 播放音樂 |
| `/add` | - | 加入播放清單 |
| `/skip` | `$s` | 跳過歌曲 |
| `/back` | - | 上一首歌曲 |
| `/pause` | `$ps` | 暫停 |
| `/resume` | `$rs` | 繼續 |
| `/stop` | - | 停止並離開 |
| `/loop` | - | 循環模式 |
| `/nowplaying` | `$np`, `$now` | 目前的歌曲 |
| `/queue` | `$q` | 顯示播放清單 |
| `/remove` | `$rm` | 移除歌曲 |
| `/clear` | `$cq` | 清除播放清單 |
| `/leave` | - | 離開頻道 |
| `/volume` | - | 調整音量 |
| `/play_custom_list` | - | 播放播放清單 |
| `/add_custom_list` | - | 加入播放清單 |
| `/show_custom_list` | - | 顯示播放清單 |
| `/delete_custom_list` | - | 刪除播放清單 |
| `/emoji` | - | 顯示表情符號 |
| `/reload_emojis` | - | 重載表情符號 |
