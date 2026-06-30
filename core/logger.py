import logging
import sys
from logging.handlers import RotatingFileHandler

from rich.logging import RichHandler

from config import settings


def setup_logger(name: str = "automation-engine") -> logging.Logger:
    """
    Sets up a logger with RichHandler for colored console logs
    and RotatingFileHandler for saving logs to file.
    """
    logger = logging.getLogger(name)

    # Set logging level based on configuration
    log_level_str = settings.LOG_LEVEL.upper()
    log_level = getattr(logging, log_level_str, logging.INFO)
    logger.setLevel(log_level)

    # Avoid duplicate handlers if setup multiple times
    if logger.handlers:
        return logger

    # Formatter for file logging
    file_formatter = logging.Formatter("[%(asctime)s] %(levelname)-8s %(name)s (%(filename)s:%(lineno)d) - %(message)s")

    # Console Handler (Rich)
    console_handler = RichHandler(rich_tracebacks=True, markup=True, show_path=False)
    console_handler.setLevel(log_level)
    logger.addHandler(console_handler)

    # File Handler
    try:
        log_file = settings.LOGS_DIR / "app.log"
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=10 * 1024 * 1024,  # 10MB
            backupCount=5,
            encoding="utf-8",
        )
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(log_level)
        logger.addHandler(file_handler)
    except Exception as e:
        print(f"Warning: Could not set up file logger due to: {e}", file=sys.stderr)

    return logger


# Shared logger instance
logger = setup_logger()
