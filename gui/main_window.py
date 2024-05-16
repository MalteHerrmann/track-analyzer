"""
This file contains the logic to define the main window of the application.
"""

from pathlib import Path

from audio import ID3File
from config import load_available_tags
from gui.file_dialog import FileDialog
from gui.tag_list import TagList

from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    """
    The main window of the application.
    """

    def __init__(self):
        super().__init__()

        self.loaded_file: ID3File | None = None
        self.tag_list: TagList | None = None

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

        file_dialog_widget = FileDialog("")
        layout.addWidget(file_dialog_widget)

        button = QPushButton("Load Track")
        layout.addWidget(button)

        button.clicked.connect(lambda x: self.load_track(file_dialog_widget.file))

        # TODO: add listbox for available genres
        genre_selector = QComboBox()
        genre_selector.addItems(self.available_tags.keys())
        layout.addWidget(genre_selector)

        genre_selector.currentTextChanged.connect(lambda x: self.tag_list.update_tags(x))

        self.tag_list = TagList(self.available_tags, self.selected_genre)
        layout.addWidget(self.tag_list)

        apply_button = QPushButton("Apply")
        layout.addWidget(apply_button)

        apply_button.clicked.connect(self.apply)

    def load_track(self, file: str):
        """
        Adds the selected label to the track metadata.
        """
        # TODO: load track object
        print(f"TODO: set the label on the selected track - got file: {file}")
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
