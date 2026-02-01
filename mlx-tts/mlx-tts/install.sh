#!/bin/bash

set -ueo pipefail

# use brew to install ffmpeg if not exists
command -v ffmpeg || brew install ffmpeg

# use brew to install uv if not exists
command -v uv || brew install uv

# use uv to install mlx-audio.tts.generate if not exists
# install mlx_audio.tts.generate as cli tool
command -v mlx_audio.tts.generate || uv tool install --force --python 3.12 "mlx-audio[tts]" --prerelease=allow
