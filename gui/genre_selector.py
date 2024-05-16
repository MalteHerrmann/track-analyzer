from PyQt5.QtWidgets import QComboBox, QHBoxLayout, QLabel, QWidget


class GenreSelector(QWidget):
    """
    A widget that allows the user to select a genre.
    """

    def __init__(self, available_tags: dict[str, list[str]], selected_genre: str):
        super().__init__()

        self.available_tags = available_tags
        self.selected_genre = selected_genre

        layout = QHBoxLayout()
        self.setLayout(layout)

        label = QLabel("Select Genre:")
        layout.addWidget(label)

        self.combobox = QComboBox()
        self.combobox.addItems(self.available_tags.keys())
        layout.addWidget(self.combobox)
