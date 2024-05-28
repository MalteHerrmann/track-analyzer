"""
This file contains the media player, which enables playback
of the selected audio files.
"""

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QAudio, QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QSlider, QVBoxLayout, QWidget


class AudioPlayer(QWidget):
    """
    Creates an instance of the audio player.
    """

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        layout.addWidget(self.slider)

        buttons = QWidget()
        button_layout = QHBoxLayout()
        buttons.setLayout(button_layout)
        layout.addWidget(buttons)

        stop_button = QPushButton("Stop")
        button_layout.addWidget(stop_button)

        play_button = QPushButton("Play")
        button_layout.addWidget(play_button)

        self.player = QMediaPlayer()
        self.player.setAudioRole(QAudio.MusicRole)
        self.media_content = QMediaContent()
        self.player.positionChanged.connect(self.set_slider_position)

        stop_button.clicked.connect(self.stop)
        play_button.clicked.connect(self.play)
        self.slider.sliderReleased.connect(self.update_position)

    def load_track(self, track: str):
        """
        Loads the selected audio file.
        """
        self.media_content = QMediaContent(QUrl.fromLocalFile(track))
        self.player.setMedia(self.media_content)
        self.play()

    def play(self):
        """
        Plays the selected audio file.
        """
        self.player.play()

    def stop(self):
        """
        Stops the selected audio file.
        """
        self.player.stop()

    def update_position(self):
        """
        Updates the position of the audio file from the position of the slider.
        """
        position = self.slider.value()
        self.player.setPosition(self.calculate_position(position))

    def set_slider_position(self, position: int):
        """
        Adjusts the slider position according to the audio file position.
        """
        if not self.slider.isSliderDown():
            self.slider.setValue(self.calculate_normalized_position(position))

    def calculate_position(self, position: int) -> int:
        """
        Calculates the position of the audio file from the normalized position
        value (0 < x < 100).
        """
        return round(position * self.player.duration() / 100)

    def calculate_normalized_position(self, position: int) -> int:
        """
        Calculates the normalized position of the audio file.
        """
        duration = self.player.duration()
        if duration == 0:
            return 0

        return round(position * 100 / duration)
