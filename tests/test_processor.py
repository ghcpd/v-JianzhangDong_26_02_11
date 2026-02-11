import os
import pytest
from app.processor import get_user_emails

def test_get_user_emails(tmp_path):
    data_dir = tmp_path
    file_path = data_dir / "users.json"
    file_path.write_text("""
    [
      {"id": 1, "name": "Test", "email": "test@example.com"}
    ]
    """, encoding="utf-8")

    os.environ["DATA_PATH"] = str(data_dir)

    emails = get_user_emails()
    assert emails == ["test@example.com"]
