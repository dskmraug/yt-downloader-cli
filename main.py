#!/usr/bin/env python3
"""YouTube CLI Downloader — download a single video or its audio via yt-dlp."""

import sys
from pathlib import Path

from yt_dlp import YoutubeDL

DOWNLOAD_DIR = Path("downloads")


def build_options(download_type: str) -> dict:
    """Build yt-dlp options for 'video' or 'audio' download."""
    options = {
        "outtmpl": str(DOWNLOAD_DIR / "%(title)s.%(ext)s"),
        "noplaylist": True,
        "restrictfilenames": True,
    }

    if download_type == "audio":
        options.update({
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        })
    else:
        options.update({
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
        })

    return options


def download(url: str, download_type: str = "video") -> bool:
    """Download a single YouTube URL. Returns True on success."""
    DOWNLOAD_DIR.mkdir(exist_ok=True)

    try:
        with YoutubeDL(build_options(download_type)) as ydl:
            print(f"\n--- ダウンロード開始: {url} ---")
            ydl.download([url])
            print("--- 完了しました！ ---")
        return True
    except Exception as e:
        print(f"\n[エラー] ダウンロードに失敗しました: {e}")
        return False


def prompt_for_input() -> tuple[str, str]:
    url = input("動画のURLを入力してください: ").strip()
    if not url:
        print("URLが入力されていません。終了します。")
        sys.exit(1)

    choice = input("モードを選択してください (1: 動画 / 2: 音声のみ): ").strip()
    mode = "audio" if choice == "2" else "video"
    return url, mode


def main() -> None:
    print("=== YouTube CLI Downloader ===")
    url, mode = prompt_for_input()
    success = download(url, mode)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
