---
name: mlx-tts
description: Text-To-Speech with MLX (Apple Silicon) and opensource models (default QWen3-TTS) locally.
version: 0.0.1
author: guoqiao
metadata: {"openclaw":{"always":true,"emoji":"🦞","homepage":"https://github.com/guoqiao/skills/blob/main/mlx-tts/mlx-tts/SKILL.md","os":["darwin"],"requires":{"bins":["brew"]}}}
triggers:
- "/mlx-tts <text>"
- "TTS ..."
- "Convert text to audio ..."
---

# MLX Text to Speech

Text-To-Speech with MLX (Apple Silicon) and opensource models (default QWen3-TTS) locally.

Free and Fast. No api key required. No server required.

## Requirements

- `mlx`: macOS with Apple Silicon
- `brew`: used to install deps if not available

## Installation

```bash
bash ${baseDir}/install.sh
```
This script will use `brew` to install these cli tools if not available:
- `uv`: install python package and run python script
- `mlx_audio`: do the real job

## Usage

To generate audio from text, run this script:

```bash
bash ${baseDir}/mlx-stt.sh <audio_file_path>
```
generated audio path will be printed to stdout.
