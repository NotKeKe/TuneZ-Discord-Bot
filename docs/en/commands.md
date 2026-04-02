---
layout: default
title: Command List
lang: en
permalink: /en/commands/
breadcrumb:
  - title: Home
    url: /en/
  - title: Command List
    url: /en/commands/
---

# Command List

Complete list of all available TuneZ commands.

<div class="callout callout-info">
  <strong>💡 Note:</strong>
  <ul>
    <li>All commands can be used with either slash commands (`/`) or prefix (`$`) format. Both formats are shown in examples.</li>
    <li>Most commands have Chinese translations.</li>
  </ul>
</div>

---

## 📖 Terminology

### 🎵 Playlist
- **Playlist**: Refers to the queue created when you start playing with `/play` and add more songs with `/play` or `/add`.
  - This playlist is **not preserved** after leaving the voice channel.
- **Custom Playlist**: Refers to the playlists created with `/add_custom_list`.
  - These playlists are **permanently stored** in the local database.

---

## 🎵 Music Playback

### /play

Play music or add songs to the playlist.

| Format | Description |
|--------|-------------|
| `/play [query]` | Play music or add to playlist |
| `$play [query]` | Same as above |
| `$p [query]` | Shortcut |

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `query` | string | Song name, YouTube URL, or playlist URL |

**Examples:**
```
/play 不该
/play https://www.youtube.com/watch?v=MDc1mjrIsPM
```

<div class="callout callout-info">
  <strong>💡 Tip:</strong> When a song is already playing, using `/play` will automatically add to the playlist instead of starting a new player.
</div>

---

### /add

Add songs to the playlist without starting playback.

| Format | Description |
|--------|-------------|
| `/add [query]` | Add song to playlist |
| `$add [query]` | Same as above |

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `query` | string | Song name or YouTube URL |

---

### /skip

Skip the current song.

| Format | Description |
|--------|-------------|
| `/skip` | Skip to next song |
| `$skip` | Same as above |
| `$s` | Shortcut |

---

### /back

Play the previous song.

| Format | Description |
|--------|-------------|
| `/back` | Play previous song |
| `$back` | Same as above |

---

### /pause

Pause current playback.

| Format | Description |
|--------|-------------|
| `/pause` | Pause music |
| `$pause` | Same as above |
| `$ps` | Shortcut |

---

### /resume

Resume paused playback.

| Format | Description |
|--------|-------------|
| `/resume` | Resume music playback |
| `$resume` | Same as above |
| `$rs` | Shortcut |

---

### /stop

Stop playback and leave the voice channel.

| Format | Description |
|--------|-------------|
| `/stop` | Stop and disconnect |
| `$stop` | Same as above |

---

### /loop

Set or toggle loop mode.

| Format | Description |
|--------|-------------|
| `/loop [mode]` | Set loop mode |
| `$loop [mode]` | Same as above |

**Parameters:**

| Parameter | Type | Optional | Description |
|-----------|------|----------|-------------|
| `mode` | string | Yes | Loop mode: `none`, `single`, or `list` |

---

### /nowplaying

Show the currently playing song.

| Format | Description |
|--------|-------------|
| `/nowplaying` | Show current song |
| `$nowplaying` | Same as above |
| `$np` | Shortcut |
| `$now` | Shortcut |

---

### /queue

Display the current playlist.

| Format | Description |
|--------|-------------|
| `/queue` | Show playlist |
| `$queue` | Same as above |
| `$q` | Shortcut |

---

### /remove

Remove a specific song from the playlist.

| Format | Description |
|--------|-------------|
| `/remove [number]` | Remove song by number |
| `$remove [number]` | Same as above |
| `$rm [number]` | Shortcut |

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `number` | integer | Position of song in playlist (use `/queue` to check)|

**Examples:**
```
/queue        # View playlist, songs are numbered 1, 2, 3...
/remove 2     # Remove song #2
```

---

### /clear

Clear all songs from the playlist.

| Format | Description |
|--------|-------------|
| `/clear` | Clear playlist |
| `$clear` | Same as above |
| `$cq` | Shortcut |

<div class="callout callout-warning">
  <strong>⚠️ Note:</strong> After entering this command, you must click the ✅ button to confirm.
</div>

---

### /leave

Leave the voice channel (same as `/stop`).

| Format | Description |
|--------|-------------|
| `/leave` | Leave channel |
| `$leave` | Same as above |

---

### /volume

Adjust volume or show volume controls.

| Format | Description |
|--------|-------------|
| `/volume [0-200]` | Set volume |
| `$volume [0-200]` | Same as above |

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `volume` | integer | Volume level (0-200, default: 100)|

**Examples:**
```
/volume        # Show volume control buttons
/volume 50     # Set volume to 50%
/volume 150    # Set volume to 150%
```

---

## 🎛️ Interactive Buttons

When playing music, you can use interactive buttons:

| Button | Function |
|--------|----------|
| ⏮️ Previous | Play previous song |
| ⏯️ Pause/Resume | Toggle play/pause |
| ⏭️ Next | Skip to next song |
| ⏹️ Stop | Stop and leave |
| 🔁 Loop | Toggle loop mode |
| 📋 Queue | Show playlist |
| 🔄 Refresh | Refresh song info |
| 🔊 Volume | Show volume controls |

---

## 📝 Custom Playlists

See the [Custom Playlist Guide](/en/custom-playlist/) for details.

| Command | Description |
|---------|-------------|
| `/play_custom_list` | Play saved playlist |
| `/add_custom_list` | Add song to playlist |
| `/show_custom_list` | View playlist songs |
| `/delete_custom_list` | Delete playlist |
| `/remove_one_from_custom_list` | Permanently remove one song |

---

## 🛠️ Utility Commands

### /help

Show basic help information.

| Format | Description |
|--------|-------------|
| `/help` | Show help |

---

### /emoji

Show TuneZ built-in emojis.

| Format | Description |
|--------|-------------|
| `/emoji [name]` | Show emoji by name |
| `$emoji [name]` | Same as above |

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `name` | string | Emoji name (e.g., `next`, `stop`, `refresh`)|

**Examples:**
```
/emoji next      # Show "next" emoji
/emoji pause     # Show "pause" emoji
```

---

### /reload_emojis

Reload emoji resources (owner only).

| Format | Description |
|--------|-------------|
| `/reload_emojis [type]` | Reload emojis |
| `$reload_emojis [type]` | Same as above |

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `type` | string | `all`, `default`, or `custom` |

<div class="callout callout-info">
  <strong>🔧 Custom Emojis:</strong> Place your custom emoji images in the <code>data/emojis/</code> folder (or <code>C:\Users\USERNAME\AppData\Roaming\TuneZ_Discord_Bot\data\emojis</code> on Windows). Then use <code>/reload_emojis custom</code> to load them.
</div>

---

## 📊 Command Overview

| Command | Aliases | Description |
|---------|---------|-------------|
| `/play` | `$p` | Play music |
| `/add` | - | Add to playlist |
| `/skip` | `$s` | Skip song |
| `/back` | - | Previous song |
| `/pause` | `$ps` | Pause |
| `/resume` | `$rs` | Resume |
| `/stop` | - | Stop and leave |
| `/loop` | - | Loop mode |
| `/nowplaying` | `$np`, `$now` | Current song |
| `/queue` | `$q` | Show playlist |
| `/remove` | `$rm` | Remove song |
| `/clear` | `$cq` | Clear playlist |
| `/leave` | - | Leave channel |
| `/volume` | - | Adjust volume |
| `/play_custom_list` | - | Play playlist |
| `/add_custom_list` | - | Add to playlist |
| `/show_custom_list` | - | Show playlist |
| `/delete_custom_list` | - | Delete playlist |
| `/emoji` | - | Show emojis |
| `/reload_emojis` | - | Reload emojis |
