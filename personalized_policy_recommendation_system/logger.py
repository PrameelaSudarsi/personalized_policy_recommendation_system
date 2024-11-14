import logging
import os
from logging.handlers import RotatingFileHandler

# Set up the log directory
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Define log file path
LOG_FILE_PATH = os.path.join(LOG_DIR, "app.log")

# Set up logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[
        RotatingFileHandler(LOG_FILE_PATH, maxBytes=5 * 1024 * 1024, backupCount=3),
        logging.StreamHandler()
    ]
)

# Create a logger object
logger = logging.getLogger("InsuranceRecommendationApp")

# Log helper functions for different levels
def log_debug(message: str):
    """Logs a debug message."""
    logger.debug(message)

def log_info(message: str):
    """Logs an informational message."""
    logger.info(message)

def log_warning(message: str):
    """Logs a warning message."""
    logger.warning(message)

def log_error(message: str):
    """Logs an error message."""
    logger.error(message)

def log_exception(message: str):
    """Logs an exception message along with the traceback."""
    logger.exception(message)
