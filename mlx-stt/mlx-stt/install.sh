#!/bin/bash

set -ueo pipefail

# use brew to install ffmpeg if no exists
command -v ffmpeg || brew install ffmpeg

# use brew to install uv if no exists
command -v uv || brew install uv

# use uv to install mlx-audio.stt.generate if no exists
# install mlx_audio.stt.generate as cli tool
command -v mlx_audio.stt.generate || uv tool install --force mlx-audio --prerelease=allow
