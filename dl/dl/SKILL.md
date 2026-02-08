---
name: dl
description: Download media, smart and to the point.
metadata: {"openclaw":{"always":true,"emoji":"🦞","homepage":"https://github.com/guoqiao/skills/blob/main/dl/dl/SKILL.md","os":["darwin","linux","win32"],"requires":{"bins":["uv"]}}}
---

# Media Downloader

Download media with yt-dlp, with sane options, to expected locations.

# Usage

Download Single Video:
```
uvx yt-dlp --js-runtime node --remote-components ejs:github \
    -f "bestvideo[vcodec^=avc1]+bestaudio/best" --merge-output-format=mp4 --max-filesize=2000M \
    -P "$HOME/Movies" \
    -o "%(title).240B.%(ext)s" --no-playlist \
    ${url}
```

Download Video Playlist:
```
uvx yt-dlp --js-runtime node --remote-components ejs:github \
    -f "bestvideo[vcodec^=avc1]+bestaudio/best" --merge-output-format=mp4 --max-filesize=2000M \
    -P "$HOME/Movies" \
    -o "%(playlist_title)s/%(title).240B.%(ext)s" --max-downloads=30 \
    ${url}
```

Download Single Music:
```
uvx yt-dlp --js-runtime node --remote-components ejs:github \
    -f "bestaudio/best" --extract-audio --audio-format=m4a --audio-quality=0 --max-filesize=30M \
    -P "$HOME/Music" \
    -o "%(title).240B.%(ext)s" --no-playlist \
    ${url}
```

Download Music Playlist:
```
uvx yt-dlp --js-runtime node --remote-components ejs:github \
    -f "bestaudio/best" --extract-audio --audio-format=m4a --audio-quality=0 --max-filesize=30M \
    -P "$HOME/Music" \
    -o "%(playlist_title)s/%(title).240B.%(ext)s" --max-downloads=30 \
    ${url}
```