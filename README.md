# yt-downloader

シンプルな YouTube CLI ダウンローダー。[yt-dlp](https://github.com/yt-dlp/yt-dlp) を使って、動画（MP4）または音声のみをダウンロードします。

音声のみモードでは、既定では動画コンテナ内の音声トラックを再エンコードせずそのまま保存します（mp3等への変換は音質劣化を伴うため）。WAV保存を選択した場合のみ、無圧縮PCMへデコードします（こちらは追加の音質劣化を伴いません）。

## 必要環境

- Python 3.9 以上
- WAV形式での保存には [ffmpeg](https://ffmpeg.org/) が必要です（コンテナのまま保存する場合は不要です）

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
モードを選択してください (1: 動画 / 2: 音声のみ): 2
WAV形式で保存しますか？ (y/N): n
```

音声のみモードで `y` を入力すると WAV 形式（無圧縮）で保存されます。`N`（デフォルト）の場合は、コンテナの音声トラック（m4a/webm/opus など）をそのまま保存します。

ダウンロードしたファイルは `downloads/` ディレクトリに保存されます。
