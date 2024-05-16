"""
This tool can be used to assign ID3 metadata to audio files,
which is a common operation when managing my Traktor DJ tracks library.
"""

import os
import sys
from pathlib import Path
from typing import List

from metadata import adjust_metadata


def get_paths(path: str) -> List[Path]:
    """
    Returns a list of paths from the given arguments.
    """

    if not os.path.exists(path):
        print(f"Given path does not exist: {path}")
        return []

    paths = []
    if os.path.isfile(path):
        paths.append(Path(path))
    elif os.path.isdir(path):
        for entry in os.scandir(path):
            if entry.is_file():
                paths.append(Path(entry.path))
    else:
        print(f"Given path is neither file nor directory: {path}")

    return paths


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "You need to specify a specific file " + "or a directory containing mp3s!"
        )
        sys.exit(1)

    files = get_paths(sys.argv[1])
    for file in files:
        print("processing file: ", file)
        adjust_metadata(file, comments="", genre="House")
