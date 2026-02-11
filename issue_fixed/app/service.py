from app.config import Config
from app.logger import logger, setup_logger

def process():
    Config.validate()
    setup_logger(Config.LOG_LEVEL)
    logger.info("Processing started")
    return "done"
