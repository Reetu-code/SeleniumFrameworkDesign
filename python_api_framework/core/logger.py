import logging
import sys
from pathlib import Path

# Create logs directory
LOGS_DIR = Path(__file__).parent.parent / "logs"
LOGS_DIR.mkdir(exist_ok=True)
LOG_FILE = LOGS_DIR / "api_test.log"


def setup_logger(name: str = "API_Framework", log_level: int = logging.INFO) -> logging.Logger:
    """Configures a custom logger with formatted console and file output."""
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    # Log Formatter
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console Handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(log_level)
    logger.addHandler(console_handler)

    # File Handler
    file_handler = logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8")
    file_handler.setFormatter(formatter)
    file_handler.setLevel(log_level)
    logger.addHandler(file_handler)

    return logger


logger = setup_logger()
