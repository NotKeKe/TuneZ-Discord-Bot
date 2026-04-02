---
layout: default
title: Custom Playlists
lang: en
permalink: /en/custom-playlist/
breadcrumb:
  - title: Home
    url: /en/
  - title: Custom Playlists
    url: /en/custom-playlist/
---

# Custom Playlists

Create and manage your own playlists, play anytime, anywhere!

<div class="callout callout-info">
  <strong>💡 Note:</strong> Custom playlists are permanently stored. Unlike regular playlists, they are saved and can be used across different sessions.
</div>

---

## 📚 Available Commands

### /play_custom_list

Play a saved custom playlist.

| Format | Description |
|--------|-------------|
| `/play_custom_list [list_name]` | Play playlist |
| `$play_custom_list [list_name]` | Same as above |

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `list_name` | string | Your playlist name |

**Examples:**
```
/play_custom_list Favorites
/play_custom_list Chill Music
```

<div class="callout callout-warning">
  <strong>⚠️ Note:</strong> If the bot is currently playing music, you must stop it first before playing a custom playlist.
</div>

---

### /add_custom_list

Add songs to a custom playlist.

| Format | Description |
|--------|-------------|
| `/add_custom_list [url] [list_name]` | Add song to playlist |

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `url` | string | YouTube URL of the song |
| `list_name` | string | Playlist name (will be created automatically if it doesn't exist)|

**Examples:**
```
/add_custom_list https://www.youtube.com/watch?v=dQw4w9WgXcQ Favorites
/add_custom_list https://youtu.be/abc123 Favorites
```

<div class="callout callout-info">
  <strong>💡 Tip:</strong> If the playlist name doesn't exist, it will be created automatically!
</div>

---

### /show_custom_list

View all songs in a playlist.

| Format | Description |
|--------|-------------|
| `/show_custom_list [list_name]` | Show playlist |

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `list_name` | string | Your playlist name |

**Examples:**
```
/show_custom_list Favorites
```

---

### /delete_custom_list

Delete an entire playlist.

| Format | Description |
|--------|-------------|
| `/delete_custom_list [list_name]` | Delete playlist |
| `$delete_custom_list [list_name]` | Same as above |
| `$del_custom_list [list_name]` | Shortcut |

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `list_name` | string | Playlist name to delete |

<div class="callout callout-danger">
  <strong>⚠️ Warning:</strong> This will permanently delete the entire playlist and all its songs. You will be asked to confirm.
</div>

---

### /remove_one_from_custom_list

Permanently remove a single song from a playlist.

| Format | Description |
|--------|-------------|
| `/remove_one_from_custom_list [list_name] [number]` | Remove song |
| `$remove_one_from_custom_list [list_name] [number]` | Same as above |
| `$rm_one_custom_list [list_name] [number]` | Shortcut |

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `list_name` | string | Playlist name |
| `index` | integer | Song number (starting from 1)|

**Examples:**
```
/remove_one_from_custom_list Favorites 1
```

---

## 📖 Quick Tutorial

### Create Your First Playlist

1. **Create a new playlist:**
   ```
   /add_custom_list https://www.youtube.com/watch?v=song1 My Playlist
   /add_custom_list https://www.youtube.com/watch?v=song2 My Playlist
   /add_custom_list https://www.youtube.com/watch?v=song3 My Playlist
   ```

2. **View your playlist:**
   ```
   /show_custom_list My Playlist
   ```

3. **Play your playlist:**
   ```
   /play_custom_list My Playlist
   ```

### Manage Your Playlists

**Add more songs:**
```
/add_custom_list https://www.youtube.com/watch?v=song4 My Playlist
```

**Remove a song:**
```
/remove_one_from_custom_list My Playlist 2
```

**Delete a playlist:**
```
/delete_custom_list My Playlist
```

---

## 📊 Command Overview

| Command | Description |
|---------|-------------|
| `/play_custom_list [name]` | Play custom playlist |
| `/add_custom_list [url] [name]` | Add song to playlist |
| `/show_custom_list [name]` | Show playlist contents |
| `/delete_custom_list [name]` | Delete entire playlist |
| `/remove_one_from_custom_list [name] [number]` | Remove one song |

---

## 📚 Related Links

- [Command List](/en/commands/) - All available commands
- [Installation Guide](/en/installation/) - How to set up TuneZ
