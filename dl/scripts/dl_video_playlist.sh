#!/bin/bash

set -ueo pipefail

url=${1}
video_dir=${2:-$HOME/Movies}

uvx yt-dlp@latest --js-runtime node --remote-components ejs:github \
    -f "bestvideo[vcodec^=avc1]+bestaudio/best" --merge-output-format=mp4 --max-filesize=2000M \
    -P "${video_dir}" \
    -o "%(playlist_title)s/%(title).240B.%(ext)s" --max-downloads=30 \
    ${url}
