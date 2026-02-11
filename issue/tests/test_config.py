import os
import pytest
from app.config import Config

def test_env_loaded():
    assert Config.APP_ENV == "test"
