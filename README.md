# yt-downloader

シンプルな YouTube CLI ダウンローダー。[yt-dlp](https://github.com/yt-dlp/yt-dlp) を使って、動画（MP4）または音声のみ（MP3）をダウンロードします。

## 必要環境

- Python 3.9 以上
- 音声抽出（MP3変換）には [ffmpeg](https://ffmpeg.org/) が必要です

## セットアップ

```bash
pip install -r requirements.txt
```

## 使い方

```bash
python main.py
```

実行するとプロンプトが表示されるので、URL とダウンロードモードを入力してください。

```
=== YouTube CLI Downloader ===
動画のURLを入力してください: https://www.youtube.com/watch?v=xxxxxxxxxxx
モードを選択してください (1: 動画 / 2: 音声のみ): 1
```

ダウンロードしたファイルは `downloads/` ディレクトリに保存されます。
