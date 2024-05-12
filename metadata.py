import os
from pathlib import Path

import eyed3


def set_comments(mp3_file, comments: str) -> None:
    """
    Helper function to set the comments field on a given MP3 file.
    """

    mp3_file.tag.comments.set(comments)


def get_comments(mp3_file) -> str | None:
    """
    Helper function to return the comments field from the given MP3 file.
    """

    comments = mp3_file.tag.comments.get("")
    return None if comments is None else comments.text


def adjust_metadata(path: Path, comments: str, genre: str) -> None:
    """
    Adjusts the metadata of the given MP3 file,
    in case it is not already defined.
    """

    mp3_file = eyed3.load(path)
    if mp3_file is None:
        raise ValueError("Could not load the MP3 file.")

    filename = os.path.splitext(path.name)[0]
    split_name = filename.split(" - ")
    if len(split_name) != 2:
        raise ValueError(f"Unexpected filename syntax: {path.name}")

    artist, title = split_name
    file_adjusted = False

    if mp3_file.tag.artist is None:
        mp3_file.tag.artist = artist
        file_adjusted = True
    else:
        print(f"Artist already filled: {mp3_file.tag.artist}")

    if mp3_file.tag.title is None:
        mp3_file.tag.title = title
        file_adjusted = True
    else:
        print(f"Title already filled: {mp3_file.tag.title}")

    available_comments = get_comments(mp3_file)
    if available_comments is None:
        set_comments(mp3_file, comments)
        file_adjusted = True
    else:
        print(f"Comments already filled: {available_comments}")

    if mp3_file.tag.genre is None:
        mp3_file.tag.genre = genre
        file_adjusted = True
    else:
        print(f"Genre already filled: {mp3_file.tag.genre}")

    if file_adjusted:
        mp3_file.tag.save()
