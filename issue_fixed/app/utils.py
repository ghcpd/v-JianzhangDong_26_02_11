import os

def build_path(filename: str) -> str:
    """Builds a platform-correct path to the data folder."""
    return os.path.join("data", filename)
