#!/usr/bin/env python
import json
import argparse
import subprocess
import shlex
from pathlib import Path

version = '1.0.7'
name = "MLX STT"
description = "Speech-To-Text with MLX (Apple Silicon) and opensource models (default GLM-ASR-Nano-2512) locally."
author = "guoqiao"
slug = Path(__file__).parent.name
github_url = f"https://github.com/{author}/skills/blob/main/{slug}/{slug}/SKILL.md"
clawhub_url = f"https://clawhub.ai/{author}/{slug}"
homepage = clawhub_url
path = Path(__file__).with_name(slug)
tag_list = [
  "latest",
  "asr", "stt", "speech-to-text", "audio",
  "glm", "glm-asr", "glm-asr-nano-2512", "glm-asr-nano-2512-8bit",
  "macOS", "MacBook", "Mac mini", "Apple Silicon",
  "mlx", "mlx-audio",
]
tags = ','.join(tag_list)

# https://docs.openclaw.ai/tools/skills#gating-load-time-filters
metadata = {
  "openclaw": {
    "always": False,  # always include the skill (skip other gates)
    "emoji": "🦞",  # optional emoji used by the macOS Skills UI
    "homepage": homepage,  # optional URL
    "os": ["darwin"],
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
    return json.dumps(data, ensure_ascii=False, separators=(',',':'))


def run_cmd(cmd: str | list):
    if isinstance(cmd, str):
        cmdline = cmd
        shell = True
    else:
        cmd = [str(arg) for arg in cmd if arg]
        cmdline = shlex.join(cmd)
        shell = False
    print(f"running cmd: {cmdline}")
    return subprocess.run(cmd, check=True, shell=shell)


def show(verbose=False):
    json_fmt = json_pretty if verbose else json_1liner
    lines = [
      "---",
      f"name: {slug}",
      f"description: {description}",
      f"version: {version}",
      f"author: {author}",
      f"metadata: {json_fmt(metadata)}",
      "---",
    ]
    print("\n".join(lines))


def publish():
    cmd = [
        "clawhub",
        "publish",
        "--slug", slug,
        "--name", name,
        "--version", version,
        "--tags", tags,
        str(path),
    ]
    run_cmd(cmd)
    run_cmd(["git", "tag", f"{slug}-{version}"])
    run_cmd(["git", "push", "--tags"])
    print(homepage)


def main():
    parser = argparse.ArgumentParser(prog='OpenClaw Skill Metadata Generator')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-s', '--show', action='store_true')
    parser.add_argument('-p', '--publish', action='store_true')
    args = parser.parse_args()
    if args.show:
        show(verbose=args.verbose)
    elif args.publish:
        publish()



if __name__ == "__main__":
    main()

