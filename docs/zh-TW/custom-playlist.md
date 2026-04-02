---
layout: default
title: 自訂播放清單
lang: zh-TW
permalink: /zh-TW/custom-playlist/
breadcrumb:
  - title: 主頁
    url: /zh-TW/
  - title: 自訂播放清單
    url: /zh-TW/custom-playlist/
---

# 自訂播放清單

建立和管理您自己的播放清單，隨時隨地播放！

<div class="callout callout-info">
  <strong>💡 說明：</strong>自訂播放清單會被永久儲存。與一般播放清單不同，它們會被保存，可以在不同會話中使用。
</div>

---

## 📚 可用指令

### /play_custom_list

播放已儲存的自訂播放清單。

| 格式 | 說明 |
|------|------|
| `/play_custom_list [清單名稱]` | 播放播放清單 |
| `$play_custom_list [清單名稱]` | 同上 |

**參數：**

| 參數 | 類型 | 說明 |
|------|------|------|
| `list_name` | 字串 | 您的播放清單名稱 |

**範例：**
```
/play_custom_list 我的最愛
/play_custom_list 輕鬆音樂
```

<div class="callout callout-warning">
  <strong>⚠️ 注意：</strong>如果機器人正在播放音樂，您必須先停止才能播放自訂播放清單。
</div>

---

### /add_custom_list

將歌曲加入到自訂播放清單。

| 格式 | 說明 |
|------|------|
| `/add_custom_list [網址] [清單名稱]` | 將歌曲加入播放清單 |

**參數：**

| 參數 | 類型 | 說明 |
|------|------|------|
| `url` | 字串 | 歌曲的 YouTube 網址 |
| `list_name` | 字串 | 播放清單名稱（如果不存在會自動建立）|

**範例：**
```
/add_custom_list https://www.youtube.com/watch?v=dQw4w9WgXcQ 我的最愛
/add_custom_list https://youtu.be/abc123 我的最愛
```

<div class="callout callout-info">
  <strong>💡 提示：</strong>如果播放清單名稱不存在，它會被自動建立！
</div>

---

### /show_custom_list

查看播放清單中的所有歌曲。

| 格式 | 說明 |
|------|------|
| `/show_custom_list [清單名稱]` | 顯示播放清單 |

**參數：**

| 參數 | 類型 | 說明 |
|------|------|------|
| `list_name` | 字串 | 您的播放清單名稱 |

**範例：**
```
/show_custom_list 我的最愛
```

---

### /delete_custom_list

刪除整個播放清單。

| 格式 | 說明 |
|------|------|
| `/delete_custom_list [清單名稱]` | 刪除播放清單 |
| `$delete_custom_list [清單名稱]` | 同上 |
| `$del_custom_list [清單名稱]` | 簡寫 |

**參數：**

| 參數 | 類型 | 說明 |
|------|------|------|
| `list_name` | 字串 | 要刪除的播放清單名稱 |

<div class="callout callout-danger">
  <strong>⚠️ 警告：</strong>這將永久刪除整個播放清單及其所有歌曲。系統會要求您確認。
</div>

---

### /remove_one_from_custom_list

從播放清單中永久移除一首歌曲。

| 格式 | 說明 |
|------|------|
| `/remove_one_from_custom_list [清單名稱] [編號]` | 移除歌曲 |
| `$remove_one_from_custom_list [清單名稱] [編號]` | 同上 |
| `$rm_one_custom_list [清單名稱] [編號]` | 簡寫 |

**參數：**

| 參數 | 類型 | 說明 |
|------|------|------|
| `list_name` | 字串 | 播放清單名稱 |
| `index` | 整數 | 歌曲編號（從 1 開始）|

**範例：**
```
/remove_one_from_custom_list 我的最愛 1
```

---

## 📖 快速教學

### 建立您的第一個播放清單

1. **建立新的播放清單：**
   ```
   /add_custom_list https://www.youtube.com/watch?v=song1 我的播放清單
   /add_custom_list https://www.youtube.com/watch?v=song2 我的播放清單
   /add_custom_list https://www.youtube.com/watch?v=song3 我的播放清單
   ```

2. **查看您的播放清單：**
   ```
   /show_custom_list 我的播放清單
   ```

3. **播放您的播放清單：**
   ```
   /play_custom_list 我的播放清單
   ```

### 管理您的播放清單

**新增更多歌曲：**
```
/add_custom_list https://www.youtube.com/watch?v=song4 我的播放清單
```

**移除一首歌曲：**
```
/remove_one_from_custom_list 我的播放清單 2
```

**刪除播放清單：**
```
/delete_custom_list 我的播放清單
```

---

## 📊 指令總覽

| 指令 | 說明 |
|------|------|
| `/play_custom_list [名稱]` | 播放自訂播放清單 |
| `/add_custom_list [網址] [名稱]` | 將歌曲加入播放清單 |
| `/show_custom_list [名稱]` | 顯示播放清單內容 |
| `/delete_custom_list [名稱]` | 刪除整個播放清單 |
| `/remove_one_from_custom_list [名稱] [編號]` | 移除一首歌曲 |

---

## 📚 相關連結

- [指令列表](/zh-TW/commands/) - 所有可用指令
- [安裝指南](/zh-TW/installation/) - 如何設定 TuneZ
