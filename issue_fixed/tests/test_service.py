import pytest
from app.service import process

def test_process_runs():
    result = process()
    assert result == "done"
