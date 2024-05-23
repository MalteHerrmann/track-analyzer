from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QWidget


# List of utility tags, that are common across genres.
UTILITY_TAGS = ["I", "O"]


class UtilityTags(QWidget):
    """
    Holds the list of utility tags that are common across genres.
    """

    def __init__(self):
        super().__init__()

        self.buttons: dict[str, QPushButton] = {}

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        for tag in UTILITY_TAGS:
            button = QPushButton(tag)
            button.setCheckable(True)
            self.layout.addWidget(button)
            self.buttons[tag] = button

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
            if tag not in UTILITY_TAGS:
                raise ValueError(
                    f"tag not found in utility tags: {tag}\navailable utility tags: {UTILITY_TAGS}"
                )

        for available_tag in UTILITY_TAGS:
            is_selected = available_tag in tags
            self.buttons[available_tag].setChecked(is_selected)


def split_utility_tags(tags: list[str]) -> tuple[list[str], list[str]]:
    """
    Splits the given list of tags into utility tags and genre-specific tags.
    """
    utility_tags = [tag for tag in tags if tag in UTILITY_TAGS]
    genre_tags = [tag for tag in tags if tag not in UTILITY_TAGS]

    return genre_tags, utility_tags
