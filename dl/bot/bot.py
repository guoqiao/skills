#!/usr/bin/env python3
"""Minimal Telegram download bot using the core downloader."""

import asyncio
import os
import sys
import time
from pathlib import Path
from typing import Iterable

from loguru import logger
from telethon import TelegramClient, events
from telethon.errors import RPCError

# Make dl/dl.py importable.
ROOT = Path(__file__).resolve().parent.parent / "dl"
sys.path.append(str(ROOT))

import dl  # noqa: E402

TG_API_ID = int(os.environ["TG_API_ID"])
TG_API_HASH = os.environ["TG_API_HASH"]
TG_BOT_TOKEN = os.environ["TG_BOT_TOKEN"]

MAX_UPLOAD_BYTES = 1024 * 1024 * 1024  # 1GB
MAX_FILES_TO_SEND = 5

HELP = (
    "Send me a media URL and I will download it.\n"
    "Examples: YouTube, Bilibili, Twitter/X, etc."
)


def iter_new_files(path: Path, since: float) -> Iterable[Path]:
    """Yield files in *path* modified after *since* timestamp."""
    if not path.exists():
        return []
    return (
        p
        for p in path.rglob("*")
        if p.is_file() and p.stat().st_mtime >= since
    )


async def send_files(event, files: list[Path]) -> None:
    """Send a few files, skipping ones that are too large."""
    sent_any = False
    for idx, file_path in enumerate(files):
        if idx >= MAX_FILES_TO_SEND:
            await event.respond(f"...more files in {file_path.parent}")
            break
        if file_path.stat().st_size > MAX_UPLOAD_BYTES:
            logger.info("skip large file: {}", file_path)
            continue
        try:
            await event.respond(file=str(file_path))
            sent_any = True
        except RPCError as exc:
            logger.warning("failed to send file {}: {}", file_path, exc)
    if not sent_any:
        await event.respond(f"Downloaded to {files[0].parent}")


# ---------------------------------------------------------------------------
# Event handlers (registered on the client inside main())
# ---------------------------------------------------------------------------

async def on_help(event):
    """Handle /start and /help commands."""
    logger.info("/help from {}", event.sender_id)
    await event.respond(HELP)
    raise events.StopPropagation


async def on_message(event):
    """Handle plain-text messages containing URLs."""
    text = (event.raw_text or "").strip()
    if not text or text.startswith("/"):
        return

    logger.info("message from {}: {}", event.sender_id, text[:80])

    urls = [token for token in text.split() if token.startswith("http")]
    if not urls:
        await event.respond("Please send a valid URL.")
        return

    for url in urls:
        await handle_download(event, url)


async def handle_download(event, url: str) -> None:
    """Probe and download a single URL."""
    await event.respond(f"Probing: {url}")
    loop = asyncio.get_running_loop()

    class Args:
        def __init__(self, target_url: str):
            self.url = target_url
            self.verbose = False
            self.dry_run = False
            self.music_dir = dl.MUSIC_DIR
            self.video_dir = dl.VIDEO_DIR

    try:
        plan = dl.probe(Args(url))
    except Exception as exc:  # noqa: BLE001
        await event.respond(f"Probe failed: {exc}")
        logger.exception("probe failed")
        return

    await event.respond(
        f"Downloading: {plan.url}\n"
        f"Kind: {plan.kind.value}\n"
        f"Playlist: {'yes' if plan.is_playlist else 'no'}\n"
        f"Target: {plan.target_dir}"
    )

    started_at = time.time()
    try:
        await loop.run_in_executor(None, dl.download, plan)
    except Exception as exc:  # noqa: BLE001
        await event.respond(f"Download failed: {exc}")
        logger.exception("download failed")
        return

    new_files = list(iter_new_files(plan.target_dir, started_at))
    if new_files:
        new_files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
        await send_files(event, new_files)
    else:
        await event.respond(f"Downloaded to {plan.target_dir}")


async def main() -> None:
    # Create client inside the async context so it binds to the running loop.
    bot = TelegramClient("dl-bot", TG_API_ID, TG_API_HASH)
    bot.add_event_handler(on_help, events.NewMessage(pattern=r"^/(start|help)"))
    bot.add_event_handler(on_message, events.NewMessage(incoming=True))

    await bot.start(bot_token=TG_BOT_TOKEN)
    logger.info("bot started, listening for messages...")
    await bot.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
