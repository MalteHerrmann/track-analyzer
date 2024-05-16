import os
from pathlib import Path
from typing import List

from audio.id3_file import ID3File


def adjust_metadata(path: Path, comments: List[str], genre: str) -> None:
    """
    Adjusts the metadata of the given MP3 file,
    in case it is not already defined.

    Useful tool to assign title and artist when the syntax of the filename
    is "[ARTIST] - [TITLE].mp3".
    """
    mp3_file = ID3File(path)

    filename = os.path.splitext(path.name)[0]
    split_name = filename.split(" - ")
    if len(split_name) != 2:
        raise ValueError(f"Unexpected filename syntax: {path.name}")

    artist, title = split_name

    if mp3_file.get_artist() is None:
        mp3_file.set_artist(artist)
    else:
        print(f"Artist already filled: {mp3_file.get_artist()}")

    if mp3_file.get_title() is None:
        mp3_file.set_title(title)
    else:
        print(f"Title already filled: {mp3_file.get_title()}")

    available_comments = mp3_file.get_comments()
    if available_comments is None or available_comments == []:
        mp3_file.set_tags(comments)
    else:
        print(f"Comments already filled: {available_comments}")

    if mp3_file.get_genre() is None:
        mp3_file.set_genre(genre)
    else:
        print(f"Genre already filled: {mp3_file.get_genre()}")

    mp3_file.save()
