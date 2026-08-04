"""
=========================================================
ShopSphere Analytics
logger.py

Central Logging Utility

Author : Prasanta Kumar Deb
=========================================================
"""

from pathlib import Path
import logging

# ==========================================================
# Log Folder
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

LOG_DIR = PROJECT_ROOT / "logs"

LOG_DIR.mkdir(
    parents=True,
    exist_ok=True
)

LOG_FILE = LOG_DIR / "etl.log"

# ==========================================================
# Logger
# ==========================================================

logger = logging.getLogger("ShopSphereETL")

logger.setLevel(logging.INFO)

# Prevent duplicate handlers
if not logger.handlers:

    formatter = logging.Formatter(

        "%(asctime)s | %(levelname)-8s | %(message)s",

        "%Y-%m-%d %H:%M:%S"

    )

    # ------------------------------------------------------

    file_handler = logging.FileHandler(

        LOG_FILE,

        encoding="utf-8"

    )

    file_handler.setLevel(logging.INFO)

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    # ------------------------------------------------------

    console_handler = logging.StreamHandler()

    console_handler.setLevel(logging.INFO)

    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)


# ==========================================================
# Helper Functions
# ==========================================================

def log_info(message: str):

    logger.info(message)


def log_warning(message: str):

    logger.warning(message)


def log_error(message: str):

    logger.error(message)


def log_success(message: str):

    logger.info(f"SUCCESS : {message}")


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    log_info("Logger Started")

    log_success("Database Connected")

    log_warning("Duplicate Email Found")

    log_error("Customer Import Failed")