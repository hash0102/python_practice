import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def do_something():
    logger.info("sub_module.py からのログ")
