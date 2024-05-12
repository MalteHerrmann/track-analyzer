"""
This file contains the logic to define the main window of the application.
"""

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLineEdit,
    QLabel,
    QPushButton,
    QFileDialog,
)


class MainWindow(QMainWindow):
    """
    The main window of the application.
    """

    def __init__(self):
        super().__init__()
        self.file_entry: QLineEdit

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

        file_dialog_widget = self.create_file_dialog_widget("File")
        layout.addWidget(file_dialog_widget)

        button = QPushButton("Analyze Tracks")
        layout.addWidget(button)

        button.clicked.connect(self.set_track_label)

    def create_file_dialog_widget(self, title: str):
        """
        Creates the collection of widgets to build the file dialog.
        """
        file_widget = QWidget()

        h_box = QHBoxLayout()
        file_widget.setLayout(h_box)

        label = QLabel(title)
        h_box.addWidget(label)

        self.file_entry = QLineEdit()
        h_box.addWidget(self.file_entry)

        button = QPushButton(text="...")
        h_box.addWidget(button)

        button.clicked.connect(self.choose_file)

        return file_widget

    def choose_file(self):
        """
        This method opens a file dialog and fills the selected file into
        the file entry in the GUI.
        """
        # TODO: use last opened folder as target directory
        filename, _ = QFileDialog.getOpenFileName(self)
        self.file_entry.setText(filename)

    def set_track_label(self, label: str):
        """
        Adds the selected label to the track metadata.
        """
        print("TODO: set the label on the selected track")


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
