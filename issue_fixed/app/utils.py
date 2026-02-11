import os

def build_path(filename: str) -> str:
    return os.path.join("data", filename)
