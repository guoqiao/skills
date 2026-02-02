---
name: uv-global
description: Create a global uv environment as python playground or workbench.
metadata: {"openclaw":{"always":true,"emoji":"🦞","homepage":"https://github.com/guoqiao/skills/blob/main/uv-global/uv-global/SKILL.md","os":["darwin","linux"],"requires":{"anyBins":["brew","uv"]}}}
---

# UV Global

Create a global uv environment as python playground or workbench at `~/.uv-global`.
Lighnting Fast, freedom to install needed dependencies for your tasks, without polluting your system.

## Requirements

- `uv` or `brew`

## Installation

```bash
bash ${baseDir}/uv-global.sh
```
This script will:
- use `brew` to install `uv` if not available
- create a global uv project at `~/.uv-global`
- create a venv with common packages in `~/.uv-global/.venv`

Ideally but optional: prepend the venv bin to your $PATH: `export PATH=~/.uv-global/.venv/bin:$PATH`

## Usage

When you are writing a python script but need to install extra dependencies:

```bash
cd ~/.uv-global

# install deps into this global env and use them in script
uv add <pkg0> <pkg1> ...
touch script.py  #  add your code here

# or, create a standalone script with deps builtin
uv init --script script.py
uv add --script script.py <pkg0> <pkg1> ...

# run your script
uv run script.py
```