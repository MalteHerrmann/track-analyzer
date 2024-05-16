from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget


class TagList(QWidget):
    """
    Holds the list of available tags for the selected genre.
    """

    def __init__(self, available_tags: dict[str, list[str]], selected_genre: str):
        super().__init__()

        self.available_tags = available_tags
        self.selected_genre = selected_genre
        self.buttons: dict[str, QPushButton] = {}

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.create_available_tags()

    def create_available_tags(self):
        """
        Creates the list of available tags for the selected genre.
        """
        if self.selected_genre not in self.available_tags:
            raise ValueError(
                f"genre not found in configuration: {self.selected_genre}\n"
                + f"available genres: {self.available_tags.keys()}"
            )

        for tag in self.available_tags[self.selected_genre]:
            button = QPushButton(tag)
            button.setCheckable(True)
            self.layout.addWidget(button)
            self.buttons[tag] = button

    def update_tags(self, genre: str):
        """
        Updates the list of available tags for the selected genre.
        """
        self.selected_genre = genre
        for button in self.buttons.values():
            button.deleteLater()

        self.buttons.clear()
        self.create_available_tags()

    def get_selected_tags(self) -> list[str]:
        """
        Returns the list of selected tags.
        """
        return [f"#{key}" for key, button in self.buttons.items() if button.isChecked()]

    def set_selected_tags(self, tags: list[str]):
        """
        Sets the buttons corresponding to the given tags to be checked.
        """
        for tag in tags:
            if tag not in self.available_tags[self.selected_genre]:
                raise ValueError(
                    f"tag not found in available tags: {tag}\navailable tags: {self.available_tags}"
                )

        for available_tag in self.available_tags[self.selected_genre]:
            is_selected = available_tag in tags
            self.buttons[available_tag].setChecked(is_selected)
