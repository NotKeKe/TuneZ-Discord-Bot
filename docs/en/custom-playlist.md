---
layout: default
title: Custom Playlists
lang: en
permalink: /en/custom-playlist/
breadcrumb:
  - title: Home
    url: {{ '/en/' | relative_url }}
  - title: Custom Playlists
    url: {{ '/en/custom-playlist/' | relative_url }}
---

# Custom Playlists

Create and manage your own playlists that can be played anytime!

<div class="callout callout-info">
  <strong>💡 Note:</strong> Custom playlists are stored persistently. Unlike the regular queue, they are saved and can be reused across sessions.
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
| `list_name` | string | Name of your playlist |

**Example:**
```
/play_custom_list my_favorites
/play_custom_list chill_music
```

<div class="callout callout-warning">
  <strong>⚠️ Note:</strong> If the bot is already playing music, you must stop it first before playing a custom playlist.
</div>

---

### /add_custom_list

Add a song to a custom playlist.

| Format | Description |
|--------|-------------|
| `/add_custom_list [url] [list_name]` | Add song to playlist |

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `url` | string | YouTube URL of the song |
| `list_name` | string | Playlist name (creates new if doesn't exist) |

**Example:**
```
/add_custom_list https://www.youtube.com/watch?v=dQw4w9WgXcQ my_favorites
/add_custom_list https://youtu.be/abc123 my_favorites
```

<div class="callout callout-info">
  <strong>💡 Tip:</strong> If the playlist name doesn't exist, it will be automatically created!
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
| `list_name` | string | Name of your playlist |

**Example:**
```
/show_custom_list my_favorites
```

---

### /delete_custom_list

Delete an entire playlist.

| Format | Description |
|--------|-------------|
| `/delete_custom_list [list_name]` | Delete playlist |
| `$delete_custom_list [list_name]` | Same as above |
| `$del_custom_list [list_name]` | Shorthand |

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `list_name` | string | Name of playlist to delete |

<div class="callout callout-danger">
  <strong>⚠️ Warning:</strong> This will permanently delete the entire playlist and all songs in it. You will be asked to confirm.
</div>

---

### /remove_one_from_custom_list

Permanently remove a single song from a playlist.

| Format | Description |
|--------|-------------|
| `/remove_one_from_custom_list [list_name] [index]` | Remove song |
| `$remove_one_from_custom_list [list_name] [index]` | Same as above |
| `$rm_one_custom_list [list_name] [index]` | Shorthand |

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `list_name` | string | Playlist name |
| `index` | integer | Song number (starting from 1) |

**Example:**
```
/remove_one_from_custom_list my_favorites 1
```

---

## 📖 Quick Tutorial

### Creating Your First Playlist

1. **Create a new playlist:**
   ```
   /add_custom_list https://www.youtube.com/watch?v=song1 my_playlist
   /add_custom_list https://www.youtube.com/watch?v=song2 my_playlist
   /add_custom_list https://www.youtube.com/watch?v=song3 my_playlist
   ```

2. **View your playlist:**
   ```
   /show_custom_list my_playlist
   ```

3. **Play your playlist:**
   ```
   /play_custom_list my_playlist
   ```

### Managing Your Playlists

**Add more songs:**
```
/add_custom_list https://www.youtube.com/watch?v=song4 my_playlist
```

**Remove a song:**
```
/remove_one_from_custom_list my_playlist 2
```

**Delete a playlist:**
```
/delete_custom_list my_playlist
```

---

## 📊 Command Summary

| Command | Description |
|---------|-------------|
| `/play_custom_list [name]` | Play a custom playlist |
| `/add_custom_list [url] [name]` | Add song to playlist |
| `/show_custom_list [name]` | Show playlist contents |
| `/delete_custom_list [name]` | Delete entire playlist |
| `/remove_one_from_custom_list [name] [index]` | Remove one song |

---

## 💾 Data Storage

Custom playlists are stored in the `data/` directory:

```
data/
└── custom_lists/
    ├── my_playlist.json
    ├── rock_songs.json
    └── ...
```

Each playlist is saved as a JSON file containing:
- Playlist name
- List of songs (title, URL, added date)
- Owner ID

<div class="callout callout-info">
  <strong>🔒 Privacy:</strong> Only the user who created a playlist can view, modify, or delete it.
</div>

---

## 🔧 Troubleshooting

### "Playlist not found"

- Make sure you typed the playlist name correctly
- Check your playlists with `/show_custom_list [name]`

### "Already playing"

- Use `/stop` first to stop the current music
- Then use `/play_custom_list [name]`

### Can't delete playlist

- Only the owner (creator) of the playlist can delete it
- Make sure you're using the exact playlist name

---

## 📚 Related

- [Commands Reference]({{ '/en/commands/' | relative_url }}) - All available commands
- [Installation Guide]({{ '/en/installation/' | relative_url }}) - How to set up TuneZ
