"""
This file contains the logic to define the main window of the application.
"""

from pathlib import Path
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

from audio import ID3File
from config import load_available_tags
from gui.file_dialog import DirDialog
from gui.genre_selector import GenreSelector
from gui.tag_list import TagList
from gui.track_list import TrackList


class MainWindow(QMainWindow):
    """
    The main window of the application.
    """

    def __init__(self):
        super().__init__()

        self.loaded_file: ID3File
        self.tag_list: TagList

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

        genre_selector = GenreSelector(self.available_tags, self.selected_genre)
        layout.addWidget(genre_selector)

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
        track_list.listbox.itemClicked.connect(lambda x: self.load_track(x.text()))
        # Update available tags when changing genre
        genre_selector.combobox.currentTextChanged.connect(
            lambda x: self.tag_list.update_tags(x)
        )
        # Apply changes upon button press
        apply_button.clicked.connect(self.apply)

    def load_track(self, file: str):
        """
        Adds the selected label to the track metadata.
        """
        self.loaded_file = ID3File(Path(file))
        self.tag_list.set_selected_tags(self.loaded_file.get_tags())

    def apply(self):
        """
        Applies the made changes to the file.
        """
        print(f"Selected tags: {self.tag_list.get_selected_tags()}")
        if self.loaded_file is not None:
            self.loaded_file.set_tags(self.tag_list.get_selected_tags())
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
