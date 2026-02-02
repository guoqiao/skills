#!/bin/bash

set -ueo pipefail

# use brew to install uv if not exists
command -v uv || brew install uv

mkdir -p ~/.uv-global
cd ~/.uv-global

UV_PYTHON=3.14
uv python install ${UV_PYTHON}
uv init --name uv-global --python ${UV_PYTHON} > /dev/null 2>&1 || true

# install some useful packages
uv add \
    loguru python-dotenv humanize \
    arrow python-dateutil pytz \
    requests httpx beautifulsoup4 aiofiles aiohttp  websocket-client websockets \
    pillow yt-dlp web3 \
    python-markdown markitdown[all] telegramify-markdown trafilatura \
    openai anthropic google-genai