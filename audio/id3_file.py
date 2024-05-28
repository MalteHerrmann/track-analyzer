"""
This file contains the ID3File class, which enables accessing and
adjusting the metadata of audio files with the ID3 metadata standard.
"""

import os
import re
from pathlib import Path

import eyed3


class ID3File:
    """
    This utility class is used to access audio files, that
    have ID3 metadata.
    """

    def __init__(self, filepath: Path):
        self.filepath = filepath
        self.dirty: bool = False  # indicates whether the file has been changed

        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"path does not exist: {self.filepath}")

        if not os.path.isfile(self.filepath):
            raise FileNotFoundError(f"path is not a file: {self.filepath}")

        self.id3_file = eyed3.load(self.filepath)
        if self.id3_file is None:
            raise ValueError(f"failed to load the MP3 file: {self.filepath}")

    def save(self):
        """
        Saves the file if there have been changes made to it.
        """
        if not self.dirty:
            return

        self.id3_file.tag.save()

    def get_comments(self) -> list[str]:
        """
        Returns the comments field from the ID3 metadata.
        """
        comments = self.id3_file.tag.comments.get("")
        if comments is None:
            return []

        return re.split(r"\s|,", comments.text)

    def get_tags(self) -> list[str]:
        """
        Returns the tags from the comment field of the ID3 tag.
        """
        tags = []
        for comment in self.get_comments():
            if comment[0] != "#":
                print(f"found non-tag comment (not starting with #): {comment}")
                continue
            tags.append(comment[1:])

        return tags

    def set_tags(self, tags: list[str]):
        """
        Sets the tags in the comment field of the ID3 tag.
        """
        if self.get_tags() != tags:
            self.id3_file.tag.comments.set(" ".join(tags))
            self.dirty = True

    def get_title(self) -> None | str:
        """
        Returns the title from the ID3 metadata if it is set.
        """
        return self.id3_file.tag.title

    def set_title(self, title: str):
        """
        Sets the title in the ID3 metadata.
        """
        if self.get_title() != title:
            self.id3_file.tag.title = title
            self.dirty = True

    def get_artist(self) -> str:
        """
        Gets the artist from the ID3 metadata.
        """
        return self.id3_file.tag.artist

    def set_artist(self, artist: str):
        """
        Sets the artist in the ID3 metadata.
        """
        if artist != self.get_artist():
            self.id3_file.tag.artist = artist
            self.dirty = True

    def get_genre(self) -> str:
        """
        Gets the genre from the ID3 metadata.
        """
        return self.id3_file.tag.genre

    def set_genre(self, genre: str):
        """
        Sets the genre in the ID3 metadata.
        """
        if genre != self.get_genre():
            self.id3_file.tag.genre = genre
            self.dirty = True
