import os

class Config:
    @staticmethod
    def get_data_path():
        path = os.getenv("DATA_PATH")
        if not path:
            raise RuntimeError("DATA_PATH environment variable not set")
        return path
