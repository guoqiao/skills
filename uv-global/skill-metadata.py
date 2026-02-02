#!/usr/bin/env python
import json
import argparse

# https://docs.openclaw.ai/tools/skills#gating-load-time-filters
metadata = {
  "openclaw": {
    "always": True, # always include the skill (skip other gates)
    "emoji": "🦞", # optional emoji used by the macOS Skills UI
    "homepage": "https://github.com/guoqiao/skills/blob/main/uv-global/uv-global/SKILL.md", # optional URL
    "os": ["darwin", "linux"],
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


def main():
    parser = argparse.ArgumentParser(prog='Agent Skill Metadata Generator')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    if args.verbose:
        # generate pretty json for human to check
        s = json.dumps(metadata, ensure_ascii=False, indent=2)
    else:
      # generate 1-liner json to use in SKILL.md as metadata
        s = json.dumps(metadata, ensure_ascii=False, separators=(',',':'))
    print(s)


if __name__ == "__main__":
    main()

