from typing import Dict


def build_features(log: Dict) -> Dict:
    failed_attempts = int(log.get("failed_attempts", 0))
    request_count = int(log.get("request_count", 0))
    is_new_ip = int(log.get("is_new_ip", 0))
    is_new_device = int(log.get("is_new_device", 0))
    login_hour = int(log.get("login_hour", 12))
    location = str(log.get("location", "Unknown"))

    features = {
        "failed_attempts": failed_attempts,
        "request_count": request_count,
        "is_new_ip": is_new_ip,
        "is_new_device": is_new_device,
        "unknown_location": 1 if location.lower() == "unknown" else 0,
        "unusual_time": 1 if login_hour < 6 or login_hour > 22 else 0,
        "high_failed_attempts": 1 if failed_attempts >= 5 else 0,
        "high_request_count": 1 if request_count >= 100 else 0,
    }

    return features