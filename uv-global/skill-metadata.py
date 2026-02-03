#!/usr/bin/env python
import json
import argparse
from pathlib import Path

name = Path(__file__).parent.name
homepage = f"https://github.com/guoqiao/skills/blob/main/{name}/{name}/SKILL.md"

# https://docs.openclaw.ai/tools/skills#gating-load-time-filters
metadata = {
  "openclaw": {
    "always": True, # always include the skill (skip other gates)
    "emoji": "🦞", # optional emoji used by the macOS Skills UI
    "homepage": homepage, # optional URL
    "os": ["darwin", "linux"],
    "tags": ["python", "uv", "global", "venv"],
    "requires": {
      # each must exist in $PATH
      # "bins": [
      # ],
      # at list one must exist in $PATH
      "anyBins": [
        "brew",
        "uv",
      ],
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


def main():
    parser = argparse.ArgumentParser(prog='Agent Skill Metadata Generator')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    tags = metadata['openclaw']['tags']
    homepage = metadata['openclaw']['homepage']
    json_fmt = json_pretty if args.verbose else json_1liner
    print(f"\nmetadata: {json_fmt(metadata)}\n", )
    print(f"\ntags: {','.join(tags)}\n")
    print(f"\nhomepage: {homepage}\n")


if __name__ == "__main__":
    main()

