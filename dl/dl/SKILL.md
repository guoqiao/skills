---
name: dl
description: Download Video/Music from YouTube/Bilibili/X/etc.
metadata: {"openclaw":{"always":true,"emoji":"🦞","homepage":"https://github.com/guoqiao/skills/blob/main/dl/dl/SKILL.md","os":["darwin","linux","win32"],"requires":{"bins":["uv"]}}}
triggers:
- "/dl <url>"
- "Download this video ..."
- "Download this music ..."
---

# Media Downloader

Yet another yt-dlp wrapper, while this one can do a little bit more:

- when sending youtube url, it will download mp4 video into ~/Movies or ~/Videos, which ever available.
- when sending youtube music url, it will download m4a music into ~/Music.
- when sending playlist url, it will download items into a playlist sub folder, i.e.: ~/Music/<playlist>/
- this skill is best to work together with a media server, such as Universal Media Server on mac, to serve above media folders in your LAN, thus the downloaded media are automatically and instantly available on other devices, e.g.: TV.

## Usage

Just run this python uv script:
```
uv run --script ${baseDir}/dl.py $url
```
Which will auto detect Video/Music and Single/Playlist info from the url, and save to corresponding locations.

For Agent:
- use this skill when the user types `/dl <url>` or asks to download a video/music via url from YouTube/Bilibili/X/etc.
- before you start downloading, send a ack to user: "downloading with dl skill ..."
- if the downloaded media is music, and user is using telegram bot, send the music files to telegram without asking.

## Examples

Video:
- `https://youtube.com/watch?v=<id>`  -> save to `~/Movies/<name>.mp4`
- `https://youtube.com/playlist?list=PL...`  -> save to `~/Movies/<playlist>/*.mp4`

Music:
- `https://music.youtube.com/watch?v=<id>`  -> save to `~/Music/<name>.m4a`
- `https://music.youtube.com/playlist?list=PL...`  -> save to `~/Music/<playlist>/*.m4a`


## Extra Setup For Human

To make this skill more useful and different from other media downloaders:
- Install a DLNA/UPnP Media Server on this machine, e.g.: Universal Media Server(preferred on mac), miniDLNA, Jellyfin, etc.
- Add the ~/Music and ~/Movies (or ~/Videos) folders to the media server to share over LAN.
- Downloaded media with this skill, it will save media into these folders automatically.
- Play the media on other devices(e.g.: TV) directly, which will be shared by the media server.
