# Track Analyzer

This tool is a helper to manage my digital record collection.
It is used to assign metadata information on files,
like artist and title,
for files that do not contain the corresponding information yet.
It enables to assign tags in the `COMMENT` field,
which are used to organize the track collection
in [Traktor](https://www.native-instruments.com/de/products/traktor/dj-software/traktor-pro-3/) smart playlists.

## Usage

The tool can be applied to individual files or directories, that contain audio files.
In the directory case, all audio files on the corresponding root level are extracted.

```bash
python3 main.py PATH
```

When no further arguments are passed, the GUI mode is executed.

```bash
python3 main.py
```
