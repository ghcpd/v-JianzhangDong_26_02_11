import pytest
from app.config import Config

def test_missing_env():
    with pytest.raises(RuntimeError):
        Config.get_data_path()
