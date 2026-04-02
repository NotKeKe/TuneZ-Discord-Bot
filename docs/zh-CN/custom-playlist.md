---
layout: default
title: 自定义播放列表
lang: zh-CN
permalink: /zh-CN/custom-playlist/
breadcrumb:
  - title: 主页
    url: /zh-CN/
  - title: 自定义播放列表
    url: /zh-CN/custom-playlist/
---

# 自定义播放列表

建立和管理您自己的播放列表，随时随地播放！

<div class="callout callout-info">
  <strong>💡 说明：</strong>自定义播放列表会被永久储存。与一般播放列表不同，它们会被保存，可以在不同会话中使用。
</div>

---

## 📚 可用指令

### /play_custom_list

播放已储存的自定义播放列表。

| 格式 | 说明 |
|------|------|
| `/play_custom_list [列表名称]` | 播放播放列表 |
| `$play_custom_list [列表名称]` | 同上 |

**参数：**

| 参数 | 类型 | 说明 |
|------|------|------|
| `list_name` | 字符串 | 您的播放列表名称 |

**范例：**
```
/play_custom_list 我的最爱
/play_custom_list 轻松音乐
```

<div class="callout callout-warning">
  <strong>⚠️ 注意：</strong>如果机器人正在播放音乐，您必须先停止才能播放自定义播放列表。
</div>

---

### /add_custom_list

将歌曲加入到自定义播放列表。

| 格式 | 说明 |
|------|------|
| `/add_custom_list [网址] [列表名称]` | 将歌曲加入播放列表 |

**参数：**

| 参数 | 类型 | 说明 |
|------|------|------|
| `url` | 字符串 | 歌曲的 YouTube 网址 |
| `list_name` | 字符串 | 播放列表名称（如果不存在会自动建立）|

**范例：**
```
/add_custom_list https://www.youtube.com/watch?v=dQw4w9WgXcQ 我的最爱
/add_custom_list https://youtu.be/abc123 我的最爱
```

<div class="callout callout-info">
  <strong>💡 提示：</strong>如果播放列表名称不存在，它会被自动建立！
</div>

---

### /show_custom_list

查看播放列表中的所有歌曲。

| 格式 | 说明 |
|------|------|
| `/show_custom_list [列表名称]` | 显示播放列表 |

**参数：**

| 参数 | 类型 | 说明 |
|------|------|------|
| `list_name` | 字符串 | 您的播放列表名称 |

**范例：**
```
/show_custom_list 我的最爱
```

---

### /delete_custom_list

删除整个播放列表。

| 格式 | 说明 |
|------|------|
| `/delete_custom_list [列表名称]` | 删除播放列表 |
| `$delete_custom_list [列表名称]` | 同上 |
| `$del_custom_list [列表名称]` | 简写 |

**参数：**

| 参数 | 类型 | 说明 |
|------|------|------|
| `list_name` | 字符串 | 要删除的播放列表名称 |

<div class="callout callout-danger">
  <strong>⚠️ 警告：</strong>这将永久删除整个播放列表及其所有歌曲。系统会要求您确认。
</div>

---

### /remove_one_from_custom_list

从播放列表中永久移除一首歌曲。

| 格式 | 说明 |
|------|------|
| `/remove_one_from_custom_list [列表名称] [编号]` | 移除歌曲 |
| `$remove_one_from_custom_list [列表名称] [编号]` | 同上 |
| `$rm_one_custom_list [列表名称] [编号]` | 简写 |

**参数：**

| 参数 | 类型 | 说明 |
|------|------|------|
| `list_name` | 字符串 | 播放列表名称 |
| `index` | 整数 | 歌曲编号（从 1 开始）|

**范例：**
```
/remove_one_from_custom_list 我的最爱 1
```

---

## 📖 快速教程

### 建立您的第一个播放列表

1. **建立新的播放列表：**
   ```
   /add_custom_list https://www.youtube.com/watch?v=song1 我的播放列表
   /add_custom_list https://www.youtube.com/watch?v=song2 我的播放列表
   /add_custom_list https://www.youtube.com/watch?v=song3 我的播放列表
   ```

2. **查看您的播放列表：**
   ```
   /show_custom_list 我的播放列表
   ```

3. **播放您的播放列表：**
   ```
   /play_custom_list 我的播放列表
   ```

### 管理您的播放列表

**新增更多歌曲：**
```
/add_custom_list https://www.youtube.com/watch?v=song4 我的播放列表
```

**移除一首歌曲：**
```
/remove_one_from_custom_list 我的播放列表 2
```

**删除播放列表：**
```
/delete_custom_list 我的播放列表
```

---

## 📊 指令总览

| 指令 | 说明 |
|------|------|
| `/play_custom_list [名称]` | 播放自定义播放列表 |
| `/add_custom_list [网址] [名称]` | 将歌曲加入播放列表 |
| `/show_custom_list [名称]` | 显示播放列表内容 |
| `/delete_custom_list [名称]` | 删除整个播放列表 |
| `/remove_one_from_custom_list [名称] [编号]` | 移除一首歌曲 |

---

## 📚 相关连结

- [指令列表](/zh-CN/commands/) - 所有可用指令
- [安装指南](/zh-CN/installation/) - 如何设定 TuneZ
