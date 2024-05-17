"""
This file holds the utilities to load and set the configuration
of the application.
"""

import json
from pathlib import Path


def load_available_tags() -> dict[str, list[str]]:
    """
    Returns a dictionary with the available genre tags.
    """

    config_path = Path(__file__).parent / "config.json"
    with open(config_path, encoding="utf-8") as config_file:
        config = json.load(config_file)

    return config
