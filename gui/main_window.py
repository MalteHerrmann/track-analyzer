"""
This file contains the logic to define the main window of the application.
"""
import os
import re
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

from audio import ID3File
from config import load_available_tags
from gui.artist_and_title import ArtistAndTitle
from gui.audio import AudioPlayer
from gui.file_dialog import DirDialog
from gui.genre_selector import GenreSelector
from gui.tag_list import TagList
from gui.track_list import TrackList
from gui.utility_tags import split_utility_tags, UtilityTags


class MainWindow(QMainWindow):
    """
    The main window of the application.
    """

    def __init__(self):
        super().__init__()

        self.loaded_file: ID3File
        self.tag_list: TagList
        self.utility_tags: UtilityTags

        self.available_tags: dict[str, list[str]] = load_available_tags()
        self.selected_genre: str = list(self.available_tags.keys())[0]

        self.setWindowTitle("DJ Tracks Analyzer Tool")
        self.create_widgets()
        self.resize(800, 600)

    def create_widgets(self):
        """
        Creates the widgets that will be displayed in the main window.
        """
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        selected_dir_widget = DirDialog("")
        layout.addWidget(selected_dir_widget)

        track_list = TrackList()
        layout.addWidget(track_list)

        player = AudioPlayer()
        layout.addWidget(player)

        self.artist_and_title_widget = ArtistAndTitle()
        layout.addWidget(self.artist_and_title_widget)

        genre_selector = GenreSelector(
            self.available_tags, self.selected_genre
        )
        layout.addWidget(genre_selector)

        self.utility_tags = UtilityTags()
        layout.addWidget(self.utility_tags)

        self.tag_list = TagList(self.available_tags, self.selected_genre)
        layout.addWidget(self.tag_list)

        apply_button = QPushButton("Apply")
        layout.addWidget(apply_button)

        # ----------------------------------------
        # Add interactivity for GUI elements

        # Update track list when changing directory
        selected_dir_widget.dir_entry.textChanged.connect(
            lambda x: track_list.update_track_list(Path(x))
        )
        # Load track when selecting from list
        track_list.listbox.itemClicked.connect(
            lambda x: self.load_track(x.text())
        )
        track_list.listbox.itemClicked.connect(
            lambda x: player.load_track(x.text())
        )
        # Update available tags when changing genre
        genre_selector.combobox.currentTextChanged.connect(self.update_genre)
        # Apply changes upon button press
        apply_button.clicked.connect(self.apply)

    def load_track(self, file: str):
        """
        Adds the selected label to the track metadata.
        """
        self.loaded_file = ID3File(Path(file))
        self.update_track_info()
        self.update_genre(self.selected_genre)

    def update_track_info(self):
        """
        Updates the track information in the GUI.
        """
        if self.loaded_file is None:
            return

        filename = os.path.split(self.loaded_file.filepath)[1]
        split_name = re.split(r"\s+-\s+", filename, maxsplit=1)
        if len(split_name) < 2:
            artist_from_filename = split_name[0]
            title_from_filename = ""
        else:
            artist_from_filename = split_name[0]
            title_from_filename = split_name[1]

        id3_artist = self.loaded_file.get_artist()
        if id3_artist:
            self.artist_and_title_widget.set_artist(id3_artist)
        else:
            self.artist_and_title_widget.set_artist(artist_from_filename)

        id3_title = self.loaded_file.get_title()
        if id3_title:
            self.artist_and_title_widget.set_title(id3_title)
        else:
            self.artist_and_title_widget.set_title(title_from_filename)

    def update_genre(self, genre: str):
        """
        When updating the genre, the available genre tags are adjusted
        and the corresponding buttons are checked for the loaded track.
        """
        self.selected_genre = genre
        self.tag_list.update_tags(genre)

        if self.loaded_file is None:
            return

        (genre_tags, utility_tags) = split_utility_tags(
            self.loaded_file.get_tags()
        )
        self.tag_list.set_selected_tags(genre_tags)
        self.utility_tags.set_selected_tags(utility_tags)

    def apply(self):
        """
        Applies the made changes to the file.
        """
        if self.loaded_file is None:
            return

        genre_tags = self.tag_list.get_selected_tags()
        utility_tags = self.utility_tags.get_selected_tags()
        self.loaded_file.set_tags(genre_tags + utility_tags)
        self.loaded_file.set_genre(self.tag_list.selected_genre)
        self.loaded_file.set_artist(self.artist_and_title_widget.get_artist())
        self.loaded_file.set_title(self.artist_and_title_widget.get_title())
        self.loaded_file.save()


def show_main_window():
    """
    Creates the main window for the application and shows it.
    """
    # Create the main application
    app = QApplication([])

    # Create the main window
    main_window = MainWindow()
    main_window.show()

    # Start the event loop
    app.exec()
