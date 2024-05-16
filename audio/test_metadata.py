import os
import shutil
from pathlib import Path

from metadata import adjust_metadata
from audio.id3_file import ID3File


def test_adjust_metadata(tmpdir):
    orig_filename = "artist - title (without metadata).mp3"
    file_without_metadata = Path(os.path.dirname(__file__)) / "testdata" / orig_filename
    target_file = Path(tmpdir) / orig_filename
    shutil.copyfile(file_without_metadata, target_file)
    adjust_metadata(target_file, comments=["#Disco"], genre="House")

    mp3_file = ID3File(target_file)
    assert mp3_file.get_artist() == "artist"
    assert mp3_file.get_title() == "title (without metadata)"
    assert mp3_file.get_comments() == ["#Disco"]
    assert mp3_file.get_genre() == "House"
