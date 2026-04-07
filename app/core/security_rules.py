from typing import Dict, List


def check_failed_attempts(log: Dict) -> List[str]:
    reasons = []
    if log.get("failed_attempts", 0) >= 5:
        reasons.append("Multiple failed login attempts detected")
    return reasons


def check_request_flood(log: Dict) -> List[str]:
    reasons = []
    if log.get("request_count", 0) >= 100:
        reasons.append("High request frequency detected")
    return reasons


def check_new_ip(log: Dict) -> List[str]:
    reasons = []
    if log.get("is_new_ip", 0) == 1:
        reasons.append("Login from new IP address")
    return reasons


def check_new_device(log: Dict) -> List[str]:
    reasons = []
    if log.get("is_new_device", 0) == 1:
        reasons.append("Login from new device")
    return reasons


def check_unusual_location(log: Dict) -> List[str]:
    reasons = []
    if log.get("location", "").lower() == "unknown":
        reasons.append("Login from unknown location")
    return reasons


def check_unusual_time(log: Dict) -> List[str]:
    reasons = []
    hour = log.get("login_hour", 12)
    if hour < 6 or hour > 22:
        reasons.append("Login at unusual time")
    return reasons


def evaluate_security_rules(log: Dict) -> List[str]:
    reasons = []
    reasons.extend(check_failed_attempts(log))
    reasons.extend(check_request_flood(log))
    reasons.extend(check_new_ip(log))
    reasons.extend(check_new_device(log))
    reasons.extend(check_unusual_location(log))
    reasons.extend(check_unusual_time(log))
    return reasons