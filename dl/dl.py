#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "yt-dlp>=2026.2.4",
# ]
# ///

from pprint import pp
import yt_dlp

FMT_VIDEO = "bestvideo"
FMT_MUSIC = "/bestaudio"


class BestVideoFormat:
    pass


class BestAudioFormat:
    pass


class WorstAudioFormat:
    pass


class Downloader:
    def __init__(self, url: str):
        self.url = url

    def download(self):
        print(f"Downloading {self.url}")


class YTDLP(Downloader):
    def __init__(self, url: str = None):
        self.url = url

    def download(self):
        print(f"Downloading {self.url}")

    @classmethod
    def list_extractors(cls):
        return yt_dlp.extractor.list_extractors()

    @classmethod
    def print_extractors(cls):
        for ie in cls.list_extractors():
            print(ie.IE_NAME, ie.IE_DESC, ie.SEARCH_KEY, ie.ie_key())

    @classmethod
    def get_extractor_from_name(cls, name: str = "Youtube"):
        # Youtube -> YoutubeIE
        return yt_dlp.extractor.get_extractor(name)

    @classmethod
    def get_extractor_from_url(cls, url: str):
        for ie in cls.list_extractors():
            if ie.suitable(url):
                if ie.IE_NAME != "generic":
                    return ie


def cli():
    import argparse
    parser = argparse.ArgumentParser(description="Media Downloader")
    parser.add_argument("--url", help="Media URL")
    parser.add_argument("-L", "--list_extractors", action="store_true", help="List extractors")
    return parser.parse_args()


URL_YT_VIDEO = "https://www.youtube.com/watch?v=WO2b03Zdu4Q"  # youtube
URL_YT_VIDEO_SHORT = "https://youtu.be/WO2b03Zdu4Q"  # youtube
URL_YT_PLAYLIST = "https://www.youtube.com/playlist?list=PLFgquLnL7fKm-hXZHv1k_Q5L-xhDZZ_Nq"  # youtube:tab
URL_YTM_MUSIC = "https://music.youtube.com/watch?v=54AN2Ikljfo"  # youtube
URL_YTM_PLAYLIST = "https://music.youtube.com/playlist?list=PL2hncBlSs9hfkDdWQu2EnzlnjnC276Hmo"  # youtube:tab
URL_BL_VIDEO = "https://www.bilibili.com/video/BV1E9fDBxEB2/"  # BiliBili
URL_X_VIDEO = "https://x.com/Jackma199512/status/2019944297257382382?s=20"  # twitter

URLS = [
    URL_YT_VIDEO,
    URL_YT_VIDEO_SHORT,
    URL_YT_PLAYLIST,
    URL_YTM_MUSIC,
    URL_YTM_PLAYLIST,
    URL_BL_VIDEO,
    URL_X_VIDEO,
]


def main() -> None:
    args = cli()
    dl = YTDLP()
    if args.list_extractors:
        dl.print_extractors()
        return
    for url in URLS:
        dl = YTDLP()
        ie = dl.get_extractor_from_url(url)
        print(url, ie.IE_NAME, ie.IE_DESC, ie.SEARCH_KEY, ie.ie_key())
        print(ie.is_single_video(url))
        ie.url_result(url)



if __name__ == "__main__":
    main()
