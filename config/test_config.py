from config.config import load_available_tags


def test_load_available_genre_tags():
    available_tags = load_available_tags()
    assert "House" in available_tags
    assert "Garage" in available_tags["House"]
