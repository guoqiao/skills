---
name: gh-extract
description: Extract content from a GitHub url.
metadata: {"openclaw":{"always":false,"emoji":"🦞","homepage":"https://clawhub.ai/guoqiao/gh-extract","os":["darwin","linux","win32"],"requires":{"bins":["uv"]}}}
triggers:
- "/gh-extract <url>"
- "Extract content form this github url"
- "Download this github file"
---

# HackerNews Extract

Extract content from a GitHub url.

Use this skill when the user types `/gh-extract` or asks to extract/summarize a GitHub url.

## What it does
- Accepts an GitHub url, could be repo/tree/blob.
- Convert the url to github raw url.
- Download the raw url and save to a temp path.
- Print the path

## Requirements

- `uv` installed and in PATH.

## Install

`uv` will install deps automatically when first run, no explicit installation needed.

## Usage

```bash
# run as uv script
uv run --script ${baseDir}/gh-extract.py <url>
```
file will be saved into a tmp dir with proper name, full path will be printed to stdout.

## Notes
- Only works for public repo.
