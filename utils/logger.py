import logging
from logging.handlers import RotatingFileHandler
import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, f"hardware_{datetime.now().strftime('%Y%m%d')}.log")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logger = logging.getLogger("hardware_logger")
logger.setLevel(logging.INFO)
handler = RotatingFileHandler(LOG_FILE, maxBytes=1024*1024, backupCount=5)
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Usage:
# logger.info("Device connected successfully")
# logger.error("Timeout on lane 4")

# For each hardware I/O line, log:
def log_hardware_io(direction, data):
    logger.info(f"{direction}: {data}")
