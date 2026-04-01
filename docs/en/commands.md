---
layout: default
title: Commands
lang: en
permalink: /en/commands/
breadcrumb:
  - title: Home
    url: /en/
  - title: Commands
    url: /en/commands/
---

# Command Reference

Complete list of all available commands in TuneZ.

<div class="callout callout-info">
  <strong>💡 Note:</strong> All commands can be used with either the slash command (`/`) or the prefix (`$`) format. Examples show both formats.
</div>

---

## 🎵 Music Playback

### /play

Play music or add a song to the queue.

| Format | Description |
|--------|-------------|
| `/play [query]` | Play music or add to queue |
| `$play [query]` | Same as above |
| `$p [query]` | Shorthand |

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `query` | string | Song name, YouTube URL, or playlist URL |

**Example:**
```
/play never gonna give you up
/play https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

<div class="callout callout-info">
  <strong>💡 Tip:</strong> When a song is already playing, using `/play` will automatically add to the queue instead of starting a new player.
</div>

---

### /add

Add a song to the queue without starting playback.

| Format | Description |
|--------|-------------|
| `/add [query]` | Add song to queue |
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
| `$s` | Shorthand |

---

### /back

Go back to the previous song.

| Format | Description |
|--------|-------------|
| `/back` | Play previous song |
| `$back` | Same as above |

---

### /pause

Pause the current playback.

| Format | Description |
|--------|-------------|
| `/pause` | Pause music |
| `$pause` | Same as above |
| `$ps` | Shorthand |

---

### /resume

Resume paused playback.

| Format | Description |
|--------|-------------|
| `/resume` | Resume music |
| `$resume` | Same as above |
| `$rs` | Shorthand |

---

### /stop

Stop playback and leave the voice channel.

| Format | Description |
|--------|-------------|
| `/stop` | Stop and disconnect |
| `$stop` | Same as above |

---

### /loop

Set or toggle the loop mode.

| Format | Description |
|--------|-------------|
| `/loop [mode]` | Set loop mode |
| `$loop [mode]` | Same as above |

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `mode` | string | Loop mode: `none`, `single`, or `list` |

**Loop Modes:**
| Mode | Description |
|------|-------------|
| `none` | No looping (default) |
| `single` | Loop the current song |
| `list` | Loop the entire queue |

**Example:**
```
/loop single    # Loop current song
/loop list      # Loop entire playlist
/loop           # Toggle through modes
```

---

### /nowplaying

Show the currently playing song.

| Format | Description |
|--------|-------------|
| `/nowplaying` | Show current song |
| `$nowplaying` | Same as above |
| `$np` | Shorthand |
| `$now` | Shorthand |

---

### /queue

Display the current queue/playlist.

| Format | Description |
|--------|-------------|
| `/queue` | Show queue |
| `$queue` | Same as above |
| `$q` | Shorthand |

---

### /remove

Remove a specific song from the queue.

| Format | Description |
|--------|-------------|
| `/remove [number]` | Remove song by number |
| `$remove [number]` | Same as above |
| `$rm [number]` | Shorthand |

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `number` | integer | Song position in queue (see `/queue`) |

**Example:**
```
/queue        # See the queue, songs are numbered 1, 2, 3...
/remove 2     # Remove the 2nd song
```

---

### /clear

Clear all songs from the queue.

| Format | Description |
|--------|-------------|
| `/clear` | Clear queue |
| `$clear` | Same as above |
| `$cq` | Shorthand |

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

Adjust the volume or show volume controls.

| Format | Description |
|--------|-------------|
| `/volume [0-200]` | Set volume |
| `$volume [0-200]` | Same as above |

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `volume` | integer | Volume level (0-200, default: 100) |

**Example:**
```
/volume        # Show volume control buttons
/volume 50     # Set volume to 50%
/volume 150    # Set volume to 150%
```

---

## 🎛️ Interactive Buttons

When playing music, you can use the interactive buttons:

| Button | Function |
|--------|----------|
| ⏮️ Previous | Play previous song |
| ⏯️ Pause/Resume | Toggle playback |
| ⏭️ Next | Skip to next song |
| ⏹️ Stop | Stop and leave |
| 🔁 Loop | Toggle loop mode |
| 📋 Queue | Show queue |
| 🔄 Refresh | Refresh song info |
| 🔊 Volume | Show volume controls |

---

## 📝 Custom Playlists

See the [Custom Playlist Guide]({{ '/en/custom-playlist/' | relative_url }}) for detailed information.

| Command | Description |
|---------|-------------|
| `/play_custom_list` | Play a saved playlist |
| `/add_custom_list` | Add song to playlist |
| `/show_custom_list` | View playlist songs |
| `/delete_custom_list` | Delete a playlist |
| `/remove_one_from_custom_list` | Remove one song permanently |

---

## 🛠️ Utility Commands

### /help

Show basic help information.

| Format | Description |
|--------|-------------|
| `/help` | Show help |

---

### /emoji

Display TuneZ built-in emojis.

| Format | Description |
|--------|-------------|
| `/emoji [name]` | Show emoji by name |
| `$emoji [name]` | Same as above |

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `name` | string | Emoji name (e.g., `next`, `stop`, `refresh`) |

**Example:**
```
/emoji next      # Show the "next" emoji
/emoji pause     # Show the "pause" emoji
```

---

### /reload_emojis

Reload emoji assets (owner only).

| Format | Description |
|--------|-------------|
| `/reload_emojis [type]` | Reload emojis |
| `$reload_emojis [type]` | Same as above |

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `type` | string | `all`, `default`, or `custom` |

<div class="callout callout-info">
  <strong>🔧 Custom Emoji Setup:</strong> Place your custom emoji images in the `data/emojis/` folder (or `C:\Users\USERNAME\AppData\Roaming\Easy Music Bot\data\emojis` on Windows). Then use `/reload_emojis custom` to load them.
</div>

---

## 📊 Command Summary Table

| Command | Aliases | Description |
|---------|---------|-------------|
| `/play` | `$p` | Play music |
| `/add` | - | Add to queue |
| `/skip` | `$s` | Skip song |
| `/back` | - | Previous song |
| `/pause` | `$ps` | Pause |
| `/resume` | `$rs` | Resume |
| `/stop` | - | Stop & leave |
| `/loop` | - | Loop mode |
| `/nowplaying` | `$np`, `$now` | Current song |
| `/queue` | `$q` | Show queue |
| `/remove` | `$rm` | Remove song |
| `/clear` | `$cq` | Clear queue |
| `/leave` | - | Leave channel |
| `/volume` | - | Adjust volume |
| `/play_custom_list` | - | Play playlist |
| `/add_custom_list` | - | Add to playlist |
| `/show_custom_list` | - | Show playlist |
| `/delete_custom_list` | - | Delete playlist |
| `/emoji` | - | Show emoji |
| `/reload_emojis` | - | Reload emojis |
