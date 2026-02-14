#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "aiofiles>=25.1.0",
#     "loguru>=0.7.3",
#     "python-slugify>=8.0.4",
# ]
# ///
import sys
import shutil
from pathlib import Path

import slugify
from loguru import logger
import aiofiles.os


def slugify_text(text, separator="_", lowercase=False, allow_unicode=True, max_length=50):
    """
    Slugify a text.
    """
    return slugify.slugify(
        text,
        allow_unicode=allow_unicode,
        lowercase=lowercase,
        separator=separator,
        max_length=max_length,
        word_boundary=True,
        replacements=[
            ("'", ""),  # John's -> Johns, othereise will be "Jone s"
            ("|", separator),
            ("&", separator),
        ],
    )


def slugify_uri(uri: str) -> str:
    return slugify_text(uri, separator="_", lowercase=False, max_length=200)


def slugify_path(path, **kwargs):
    """
    Given a path to dir or file, slugify the stem part.

    file: /path/to/<unicode>.ext -> /path/to/<slugified>.ext
    dir: /path/to/<unicode> -> /path/to/<slugified>
    """
    path = Path(path)
    assert path.exists(), f"path does not exist: {path}"

    new_stem = slugify_text(path.stem, **kwargs)
    new_suffix = path.suffix.lower()
    new_name = f"{new_stem}{new_suffix}"
    return path.with_name(new_name)


def move(src, dst, dry_run=False):
    if src == dst:
        logger.warning(f"src dst are the same, skip move: {src}")
        return dst
    if dry_run:
        logger.info(f"[dry_run] move {src} -> {dst}")
        return src
    else:
        logger.info(f"move {src} -> {dst}")
        shutil.move(src, dst)
        return dst


async def move_async(src, dst, dry_run=False):
    if src == dst:
        logger.warning(f"src dst are the same, skip move: {src}")
        return dst

    if dry_run:
        logger.info(f"[dry_run] move async {src} -> {dst}")
        return src
    else:
        logger.info(f"move async {src} -> {dst}")
        await aiofiles.os.rename(src, dst)

    return dst


def slugify_rename(path, dry_run=False, recursive=False, **kwargs):
    """Asynchronously slugify and rename a path."""
    path = Path(path)
    new_path = slugify_path(path)
    new_path = move(path, new_path, dry_run=dry_run)

    if recursive and new_path.is_dir():
        for subpath in new_path.iterdir():
            slugify_rename(subpath, dry_run=dry_run, recursive=recursive, **kwargs)

    return new_path


async def slugify_rename_async(path, dry_run=False, recursive=False, **kwargs):
    """Asynchronously slugify and rename a path."""
    path = Path(path)
    new_path = slugify_path(path, **kwargs)
    new_path = await move_async(path, new_path, dry_run=dry_run)

    if recursive and await aiofiles.os.path.isdir(new_path):
        for subpath in await aiofiles.os.listdir(new_path):
            await slugify_rename_async(subpath, dry_run=dry_run, recursive=recursive, **kwargs)

    return new_path


def cli():
    import argparse
    parser = argparse.ArgumentParser(description="Slugify a path or text.")
    parser.add_argument("path", type=str, help="The path to slugify.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    parser.add_argument("-n", "--dry_run", action="store_true", help="Dry run")
    parser.add_argument("-r", "--recursive", action="store_true", help="Slugify a folder recursively")
    return parser.parse_args()


def main():
    args = cli()
    logger.remove()
    logger.add(sys.stderr, level="DEBUG" if args.verbose else "INFO")
    slugify_rename(args.path, recursive=args.recursive, dry_run=args.dry_run)


def main_async():
    args = cli()
    logger.remove()
    logger.add(sys.stderr, level="DEBUG" if args.verbose else "INFO")
    import asyncio
    asyncio.run(slugify_rename_async(args.path, recursive=args.recursive, dry_run=args.dry_run))


if __name__ == "__main__":
    main_async()
