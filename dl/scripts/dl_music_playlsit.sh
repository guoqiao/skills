#!/bin/bash

set -ueo pipefail

url=${1}
music_dir=${2:-$HOME/Music}

uvx yt-dlp@latest --js-runtime node --remote-components ejs:github \
    -f "bestaudio/best" --extract-audio --audio-format=m4a --audio-quality=0 --max-filesize=30M \
    -P "${music_dir}" \
    -o "%(playlist_title)s/%(title).240B.%(ext)s" --max-downloads=30 \
    ${url}
