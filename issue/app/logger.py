import logging

logger = logging.getLogger("ci_cd_project")

def setup_logger(level: str):
    logging.basicConfig(level=level)
