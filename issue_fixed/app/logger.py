import logging
from app.config import Config

logger = logging.getLogger("ci_cd_project")


def setup_logger(level: str):
    # Accept strings or numeric levels
    if isinstance(level, str):
        numeric_level = getattr(logging, level.upper(), logging.INFO)
    else:
        numeric_level = level
    logger.setLevel(numeric_level)

    # Ensure at least one handler is configured (avoid duplicate handlers in tests)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)


# Configure logger using configured level on import
setup_logger(Config.LOG_LEVEL)
