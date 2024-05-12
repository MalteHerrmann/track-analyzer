"""
This file contains the logic to define the main window of the application.
"""

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
)

from gui.file_dialog import FileDialog


class MainWindow(QMainWindow):
    """
    The main window of the application.
    """

    def __init__(self):
        super().__init__()

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

    def load_track(self, file: str):
        """
        Adds the selected label to the track metadata.
        """
        # TODO: load track object
        print(f"TODO: set the label on the selected track - got file: {file}")


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
