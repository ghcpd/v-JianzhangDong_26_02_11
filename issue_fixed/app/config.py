import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    APP_ENV = os.getenv("APP_ENV")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    @classmethod
    def validate(cls):
        if not cls.APP_ENV:
            raise ValueError("APP_ENV is not set")
