from app.config import Config
from app.logger import logger


def process():
    Config.validate()
    logger.info("Processing started")
    return "done"
