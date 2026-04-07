import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_URL = f"sqlite:///{BASE_DIR}/cyber_monitor.db"

# Detection thresholds
FAILED_ATTEMPT_THRESHOLD = 5
REQUEST_COUNT_THRESHOLD = 100

# Risk scoring weights
WEIGHTS = {
    "failed_attempts": 40,
    "request_count": 35,
    "new_ip": 10,
    "new_device": 10,
    "unusual_time": 10
}