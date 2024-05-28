"""
This file contains the track list widget that shows
the available audio files with a given directory.
"""

from pathlib import Path
from PyQt5.QtWidgets import QListWidget, QPushButton, QVBoxLayout, QWidget


class TrackList(QWidget):
    """
    This widget holds the list of audio files in the given directory.
    """

    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.track_list: list[str] = []
        self.buttons: dict[str, QPushButton] = {}
        self.listbox = QListWidget()
        self.layout.addWidget(self.listbox)

    def update_track_list(self, directory: Path) -> None:
        """
        Updates the track list with the contents of the given directory.
        """
        if not directory.exists():
            return

        self.track_list = [
            str(file)
            for file in directory.iterdir()
            if file.is_file() and file.suffix == ".mp3"
        ]
        self.listbox.clear()
        self.listbox.addItems(self.track_list)
