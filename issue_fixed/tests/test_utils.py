import os
from app.utils import build_path

def test_build_path():
    path = build_path("file.txt")
    expected = os.path.join("data", "file.txt")
    assert path == expected
