import os


def build_path(filename: str) -> str:
    """Return a path to the data folder using OS-appropriate separators."""
    return os.path.join("data", filename)
