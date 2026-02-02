---
name: hn-extract
description: Extract a Hacker News story (article + comments) into clean Markdown for quick reading or LLM input.
metadata:  {"openclaw":{"always":true,"emoji":"🦞","homepage":"https://github.com/guoqiao/skills/blob/main/hn-extract/hn-extract/SKILL.md","os":["darwin","linux","win32"],"tags":["hn","hackernews","comments","extract","markdown","python","uv","scraper","rss","reader","summarize"],"requires":{"bins":["uv"]}}}
---

# HackerNews Extract

Pull a HackerNews post (story + nested comments), scrape the linked article, and produce a single Markdown/text document.

## What it does
- Accepts an HackerNews id, url, or a saved Algolia JSON file.
- Scrapes the linked article content with `trafilatura`, cleans HTML, and formats it.
- Fetches the story metadata and comment tree from `https://hn.algolia.com/api/v1/items/<id>`.
- Outputs a readable combined markdown file with original article, threaded comments, and key metadata.

## Requirements

- `uv` installed and in PATH.

## Install

No install beyond having `uv`.
Dependencies will be installed automatically by `uv` into to a dedicated venv when run this script.

## Usage

```bash
# run as uv script
uv run --script ${baseDir}/hn-extract.py <hn-id|hn-url|path/to/item.json> [-o path/to/output.md]

# Examples
uv run --script ${baseDir}/hn-extract.py 46861313 -o /tmp/output.md
uv run --script ${baseDir}/hn-extract.py "https://news.ycombinator.com/item?id=46861313"
uv run --script ${baseDir}/hn-extract.py data/item.json
```

- Omit `-o` to print to stdout.
- Directories for `-o` are created automatically.

## Notes
- Retries are enabled for HTTP fetches.
- Comments are indented by thread depth.
- Article fetch uses `trafilatura.fetch_url` with liberal SSL handling;
- Sites requires authentication or blocks scraping may still fail.
