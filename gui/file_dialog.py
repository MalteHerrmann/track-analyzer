"""
This file contains the definition of the FileDialog class,
used to create a widget that is used to select the file to be analyzed.
"""

from PyQt5.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QWidget,
)


class DirDialog(QWidget):
    """
    Creates a widget to select a directory.
    """

    def __init__(self, title: str):
        super().__init__()

        self.title = title
        self.dir: str = ""

        self.dir_entry: QLineEdit
        self.button: QPushButton

        self.create_widget()

    def create_widget(self):
        """
        Creates the widget to select a directory.
        """
        h_box = QHBoxLayout()
        self.setLayout(h_box)

        if self.title:
            label = QLabel(self.title)
            h_box.addWidget(label)

        self.dir_entry = QLineEdit()
        h_box.addWidget(self.dir_entry)

        self.button = QPushButton("...")
        h_box.addWidget(self.button)

        self.button.clicked.connect(self.select_dir)

    def select_dir(self):
        """
        Opens a file dialog to select a directory.
        """
        self.dir = QFileDialog.getExistingDirectory(
            self,
            self.title,
            "",
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks,
        )
        self.dir_entry.setText(self.dir)
