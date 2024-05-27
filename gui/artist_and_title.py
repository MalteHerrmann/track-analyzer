"""
Contains the widget to adjust the title and artist of a given track.
"""

from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QWidget


class ArtistAndTitle(QWidget):
    """
    A widget that allows the user to adjust the title and artist of a track.
    """

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        self.setLayout(layout)

        artist_label = QLabel("Artist:")
        layout.addWidget(artist_label)

        self.artist = QLineEdit("")
        layout.addWidget(self.artist)

        title_label = QLabel("Title:")
        layout.addWidget(title_label)

        self.title = QLineEdit("")
        layout.addWidget(self.title)

    def set_title(self, title: str):
        """
        Sets the title of the track.
        """
        self.title.setText(title)

    def set_artist(self, artist: str):
        """
        Sets the artist of the track.
        """
        self.artist.setText(artist)

    def get_title(self) -> str:
        """
        Returns the title of the track.
        """
        return self.title.text()

    def get_artist(self) -> str:
        """
        Returns the artist of the track.
        """
        return self.artist.text()
