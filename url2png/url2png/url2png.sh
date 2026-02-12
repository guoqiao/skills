#!/usr/bin/env bash

set -ue -o pipefail

url="${1:-https://simonwillison.net/2026/Feb/10/showboat-and-rodney}"

outdir=$(mktemp -d)
mkdir -p ${outdir}
# cd into outdir, let shot-scraper save with proper name
cd ${outdir}

unset UV_ENV_FILE
uvx --no-env-file shot-scraper install --browser chromium || true
# take long screenshot for iPhone by default
uvx --no-env-file shot-scraper shot "${url}" \
    --browser chromium \
    --width 390 \
    --retina \
    --wait 5000 \
    --timeout 30000 \
    --silent

find ${outdir} -maxdepth 1 -type f -name "*.png"
