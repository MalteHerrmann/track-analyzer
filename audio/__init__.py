"""
This module exposes the necessary classes and functions
to adjust audio files metadata.
"""

from audio.id3_file import ID3File
from audio.metadata import adjust_metadata

__all__ = ["ID3File", "adjust_metadata"]
