#! /usr/bin/env python3
import os
import json
import sys
import textwrap
import subprocess
import shlex
from pathlib import Path

# bird cli with auth
CLI_PATH = Path(os.getenv("BIRD_CLI_PATH", "~/bin/birded")).expanduser().resolve()


def log(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def fmt_json(data) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False)


def tee_json(data, file=sys.stderr) -> str:
    print(fmt_json(data), file=file)
    return data


def run_cmd(cmd, check=True, **kwargs):
    cmd = [str(arg) for arg in cmd if arg]
    cmdline = shlex.join(cmd)
    log(f"running cmd: {cmdline}")
    return subprocess.run(cmd, check=check, **kwargs)



def get_cmd_output(cmd, fmt="txt", **kwargs):
    output = run_cmd(cmd, check=True, capture_output=True, text=True, **kwargs).stdout.strip()
    if fmt == "json":
        return json.loads(output)
    return output


def get_tweet_text(tweet_id: str) -> str:
    return get_cmd_output([CLI_PATH, "read", tweet_id])


def get_tweet_json(tweet_id: str) -> str:
    return get_cmd_output([CLI_PATH, "read", tweet_id, "--json"], fmt="json")


def get_thread_text(tweet_id: str) -> list[str]:
    return get_cmd_output([CLI_PATH, "thread", tweet_id])


def get_thread_json(tweet_id: str) -> list[str]:
    return get_cmd_output([CLI_PATH, "thread", tweet_id, "--json"], fmt="json")


def get_article(thread_json: list[str]) -> dict:
    """
    "article": {
      "title": "2026年，我眼中的中国经济",
      "previewText": "最近一段时间，一边忙工作，一边断断续续听了油管上一些大V和中V讲中国经济的节目，包括但不限于不明白播客对李厚辰和 Victor Shih"
    }
    """
    if thread_json:
        if isinstance(thread_json, list):
            if len(thread_json) > 0:
                return thread_json[0].get("article", {})


def get_media_list(thread_json: list[str]) -> dict:
    if thread_json:
        if isinstance(thread_json, list):
            if len(thread_json) > 0:
                return thread_json[0].get("media") or []


def get_video_url(thread_json: list[str]) -> str:
    media_list = get_media_list(thread_json)
    for media in media_list:
        if media.get("type", "").lower() == "video":
            return media.get("videoUrl", "")


def is_video(thread_json: list[str]) -> bool:
    return get_video_url(thread_json)


def has_video(thread_json: list[str]) -> bool:
    return get_video_url(thread_json)


def get_article_title(thread_json: dict) -> str:
    return get_article(thread_json).get("title", "")


def is_article(thread_json: list[str]) -> bool:
    return get_article(thread_json)


def fmt_tweet_json_to_text(data, include_quoted_tweet: bool = False) -> list[str]:
    text = data.get("text", "")
    if not text:
        return ""

    username = data.get("author", {}).get("username", "unknown")
    quoted_tweet = data.get("quotedTweet", {})

    lines = [f"@{username}: {text}"]

    if include_quoted_tweet:
        quoted_tweet_text = quoted_tweet.get("text", "")
        if quoted_tweet_text:
            quoted_tweet_str = fmt_tweet_json_to_text(quoted_tweet)
            lines.append('\n' + textwrap.indent(quoted_tweet_str, "  > ") + '\n')

    return "\n".join(lines)


def fmt_thread_json_to_text(data) -> str:
    all_lines = []
    for tweet in data:
        all_lines.append(fmt_tweet_json_to_text(tweet))
    return "\n\n".join(all_lines)


def get_thread_text_minimal(tweet_id: str, verbose: bool = False) -> str:
    # the original thread text format includes too many metadata, like urls and time
    # this one customize it with minimal content
    data = get_thread_json(tweet_id)
    if verbose:
        tee_json(data)
    return fmt_thread_json_to_text(data)


# alias
get_thread = get_thread_text_minimal


def cli():
    import argparse
    parser = argparse.ArgumentParser(description="Twitter Thread")
    parser.add_argument("tweet_id", help="Tweet ID or URI")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    parser.add_argument("-j", "--json", action="store_true", help="Output as JSON")
    parser.add_argument("-m", "--minimal", action="store_true", help="Output with minimal content")
    return parser.parse_args()


if __name__ == "__main__":
    args = cli()
    if args.json:
        data = get_thread_json(args.tweet_id)
        tee_json(data, file=sys.stdout)
    else:
        if args.minimal:
            print(get_thread_text_minimal(args.tweet_id, verbose=args.verbose))
        else:
            print(get_thread_text(args.tweet_id))