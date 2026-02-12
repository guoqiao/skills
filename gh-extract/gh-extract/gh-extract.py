#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "furl>=2.1.4",
#     "loguru>=0.7.3",
#     "requests>=2.32.5",
#     "urllib3>=2.6.3",
# ]
# ///

"""
Extract content from a GitHub url.

Given a GitHub url, convert to raw url, save to a file.
"""

import argparse
import json
import sys
import tempfile
import subprocess
from pathlib import Path

import requests
from furl import furl
from urllib3 import Retry
from loguru import logger


def fmt_json(data) -> dict:
    return json.dumps(data, indent=2, ensure_ascii=False)


def tee_json(data):
    print(fmt_json(data))
    return data


def get_request_session(retry_total=3):
    """Get a request session with automatic retry."""
    retries = Retry(total=retry_total)
    adapter = requests.adapters.HTTPAdapter(max_retries=retries)
    session = requests.Session()
    session.mount("https://", adapter)
    return session


request_session = get_request_session(retry_total=3)


def is_url_alive(url: str) -> bool:
    """Check if a url is valid."""
    return request_session.head(url).ok


class GitHubExtractor:
    """Extractor content from a GitHub url."""

    def get_raw_url(self, url: str) -> str:
        # given a github url, return the raw url
        f = furl(url)
        if f.host.lower() != "github.com":
            logger.error(f"Host is not GitHub: {url}")
            return ""
        # /user/repo or /user/repo/blob/path/to/file
        path = f.path
        segs = path.segments
        n = len(segs)
        if n < 2:
            logger.error(f"Segments are less than 2: {url}")
            return ""
        user, repo = segs[:2]
        if n == 2:
            logger.debug(f"Getting doc from repo url: {url}")
            # get README.md/SKILL.md/README.txt
            for file in ["README.md", "SKILL.md", "README.txt"]:
                for branch in ["main", "master", "dev"]:
                    raw_url = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/{file}"
                    logger.debug(f"Trying raw url: {raw_url}")
                    if is_url_alive(raw_url):
                        return raw_url
        assert n >= 3

        if segs[2].lower() == "tree":
            logger.debug(f"Getting doc from repo tree url: {url}")
            # url to a folder
            # ex: https://github.com/guoqiao/skills/tree/main/hn-extract/hn-extract
            treepath = "/".join(segs[3:])
            for filename in ["README.md", "SKILL.md", "README.txt"]:
                raw_url = f"https://raw.githubusercontent.com/{user}/{repo}/{treepath}/{filename}"
                logger.debug(f"Trying raw url: {raw_url}")
                if is_url_alive(raw_url):
                    return raw_url

        if segs[2].lower() == "blob":
            logger.debug(f"Getting file from repo blob url: {url}")
            # url to a file
            # ex: https://github.com/guoqiao/skills/blob/main/hn-extract/hn-extract/hn-extract.py
            filepath = "/".join(segs[3:])
            raw_url = f"https://raw.githubusercontent.com/{user}/{repo}/{filepath}"
            if is_url_alive(raw_url):
                return raw_url

        return ""

    def fetch_raw_url(self, raw_url: str) -> Path:
        if not raw_url:
            logger.error("raw url is empty")
            return None

        tmpdir = Path(tempfile.mkdtemp(prefix="gh-extract-"))
        tmpdir.mkdir(parents=True, exist_ok=True)
        # work in tmpdir, let wget decide the file name
        subprocess.run(["wget", "--quiet", raw_url], cwd=tmpdir)
        for path in tmpdir.glob("*"):
            # return the first file
            if path.is_file():
                return path


    def extract(self, url: str) -> Path:
        return self.fetch_raw_url(self.get_raw_url(url))


def extract(url: str) -> Path:
    return GitHubExtractor().extract(url)


def cli():
    parser = argparse.ArgumentParser(
        prog="GitHub Extractor",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("url", type=str, help="GitHub url")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose/debug mode")
    return parser.parse_args()


def main():
    args = cli()

    logger.remove()
    logger.add(sys.stderr, level=args.verbose and "DEBUG" or "INFO")

    path = extract(args.url)

    if args.verbose:
        print(path.read_text())

    # final output is the file path
    print(path)


if __name__ == "__main__":
    main()
