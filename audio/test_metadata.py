import shutil
from pathlib import Path

import eyed3
from metadata import adjust_metadata, get_comments


def test_adjust_metadata(tmpdir):
    orig_filename = "artist - title (without metadata).mp3"
    file_without_metadata = Path("testdata") / orig_filename
    target_file = Path(tmpdir) / orig_filename
    shutil.copyfile(file_without_metadata, target_file)
    adjust_metadata(target_file, comments="#Disco", genre="House")

    mp3_file = eyed3.load(target_file)
    assert mp3_file.tag.artist == "artist"
    assert mp3_file.tag.title == "title (without metadata)"
    assert get_comments(mp3_file) == "#Disco"
    assert mp3_file.tag.genre == "House"


def test_get_comments():
    mp3_file = eyed3.load("testdata/artist - title (with metadata).mp3")
    assert get_comments(mp3_file) == "#Garage #4x4"
