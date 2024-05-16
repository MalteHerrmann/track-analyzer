import pytest
from os.path import dirname
from pathlib import Path

from id3_file import ID3File


@pytest.fixture
def track_with_metadata() -> ID3File:
    id3_file = ID3File(
        Path(dirname(__file__)) /
        "testdata" /
        "artist - title (with metadata).mp3"
    )
    return id3_file


def test_getters(track_with_metadata):
    assert track_with_metadata.get_comments() == ["#Garage", "#4x4"]
    assert track_with_metadata.get_title() == "Cycles (Oppidan Remix)"
    assert track_with_metadata.get_artist() == "33 Below"
    assert track_with_metadata.get_genre() == "House"

# NOTE: Setters are tested in the adjust_metadata function
