#!/usr/bin/env bash

set -ue -o pipefail

url="${1:-https://simonwillison.net/2026/Feb/10/showboat-and-rodney}"

outdir=${2:-$(mktemp -d)}
mkdir -p ${outdir}
# cd into outdir, let shot-scraper save with proper name
cd ${outdir}

unset UV_ENV_FILE
# uvx --no-env-file shot-scraper install --browser chromium || true
# create pdf for iPhone by default
# height 844 - 74 to rm notch
# print background is important, otherwise dark themed pages will become white and hard to read
uvx --no-env-file shot-scraper pdf "${url}" \
    --width 390px \
    --height 770px \
    --scale 1.1 \
    --print-background \
    --wait 5000 \
    --timeout 30000 \
    --silent

find ${outdir} -maxdepth 1 -type f -name "*.pdf"
