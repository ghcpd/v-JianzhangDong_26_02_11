import logging
from app.config import Config

logger = logging.getLogger("ci_cd_project")

# configure root logger and the module logger using the configured LOG_LEVEL
_level = Config.LOG_LEVEL if hasattr(Config, "LOG_LEVEL") else "INFO"
logging.basicConfig(level=_level)
logger.setLevel(_level)


def setup_logger(level: str):
    """Allow explicit logger reconfiguration (string or int accepted)."""
    logging.basicConfig(level=level)
    logger.setLevel(level)
