"""
This file contains the definition of the FileDialog class,
used to create a widget that is used to select the file to be analyzed.
"""

from PyQt5.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFileDialog,
)


class FileDialog(QWidget):
    """
    Creates a widget to select a file.
    """

    def __init__(self, title: str):
        super().__init__()

        self.title = title
        self.file: str = ""

        self.file_entry: QLineEdit
        self.button: QPushButton

        self.create_widget()

    def create_widget(self):
        """
        Creates the widget to select a file.
        """
        h_box = QHBoxLayout()
        self.setLayout(h_box)

        if self.title:
            label = QLabel(self.title)
            h_box.addWidget(label)

        self.file_entry = QLineEdit()
        h_box.addWidget(self.file_entry)

        self.button = QPushButton("...")
        h_box.addWidget(self.button)

        self.button.clicked.connect(self.select_file)

    def select_file(self):
        """
        Opens a file dialog to select a file.
        """
        self.file, _ = QFileDialog.getOpenFileName(
            self,
            self.title,
            "",
            "MP3 Files (*.mp3);;All Files (*.*)",
        )
        self.file_entry.setText(self.file)
