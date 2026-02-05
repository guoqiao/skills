#!/usr/bin/env python
import json
import argparse
from pathlib import Path

name = Path(__file__).parent.name
homepage = f"https://github.com/guoqiao/skills/blob/main/{name}/{name}/SKILL.md"

# https://docs.openclaw.ai/tools/skills#gating-load-time-filters
metadata = {
  "openclaw": {
    "always": True,  # always include the skill (skip other gates)
    "emoji": "🦞",  # optional emoji used by the macOS Skills UI
    "homepage": homepage,  # optional URL
    "os": ["darwin"],
    "tags": [
      "latest",
      "asr", "stt", "speech-to-text",
      "tts", "text-to-speech",
      "mlx", "audio", "mlx-audio",
      "glm", "glm-asr", "glm-asr-nano-2512", "glm-asr-nano-2512-8bit",
      "macOS", "MacBook", "Mac mini", "Apple Silicon",
      "server", "local", "openai", "api", "compatible", "openai-compatible", "transcription",
    ],
    "requires": {
      # each must exist in $PATH
      "bins": [
        "brew",
      ],
      # at list one must exist in $PATH
      # "anyBins": [
        # "brew",
        # "uv",
        # "ffmpeg",
        # "mlx_audio.stt.generate",
      # ],
      # env vars must exist or be provided in config
      # "env": [
      # ],
      # list of openclaw.json paths must be true
      # "config": [
      # ]
    },
    # env var name associated with skills.entries.<name>.apiKey
    # "primaryEnv": "GEMINI_API_KEY",
    # optional array of installer specs used by the macOS Skills UI
    # "install": [
        #"brew",
        #"node",
        #"go",
        #"uv",
        #"download",
    # ]
  }
}


def json_pretty(data):
    return json.dumps(data, ensure_ascii=False, indent=2)


def json_1liner(data):
    return json.dumps(data, ensure_ascii=False, separators=(',', ':'))


def main():
    parser = argparse.ArgumentParser(prog='OpenClaw Skill Metadata Generator')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    json_fmt = json_pretty if args.verbose else json_1liner
    tags = metadata['openclaw']['tags']
    homepage = metadata['openclaw']['homepage']
    print(f"\nmetadata: {json_fmt(metadata)}\n", )
    print(f"\ntags: {','.join(tags)}\n")
    print(f"\nhomepage: {homepage}\n")
    print("\nimport: https://clawhub.ai/import\n")


if __name__ == "__main__":
    main()
