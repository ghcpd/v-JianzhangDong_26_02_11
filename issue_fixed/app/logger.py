import logging
from app.config import Config

logger = logging.getLogger("ci_cd_project")

def setup_logger(level: str):
    logging.basicConfig(level=level)

# Initialize logger with LOG_LEVEL from config
setup_logger(Config.LOG_LEVEL)
