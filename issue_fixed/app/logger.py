import logging

logger = logging.getLogger("ci_cd_project")

def setup_logger(level: str):
    numeric_level = getattr(logging, level.upper(), logging.INFO)
    logging.basicConfig(level=numeric_level)
