from typing import Dict, List


def calculate_risk_score(log: Dict, reasons: List[str]) -> float:
    score = 0

    if log.get("failed_attempts", 0) >= 5:
        score += 40

    if log.get("request_count", 0) >= 100:
        score += 35

    if log.get("is_new_ip", 0) == 1:
        score += 10

    if log.get("is_new_device", 0) == 1:
        score += 10

    if str(log.get("location", "")).lower() == "unknown":
        score += 10

    hour = log.get("login_hour", 12)
    if hour < 6 or hour > 22:
        score += 10

    score += min(len(reasons) * 2, 10)

    return min(score, 100)


def get_severity(score: float) -> str:
    if score >= 80:
        return "CRITICAL"
    if score >= 60:
        return "HIGH"
    if score >= 40:
        return "MEDIUM"
    return "LOW"


def get_threat_type(log: Dict) -> str:
    event_type = str(log.get("event_type", "unknown")).lower()

    if event_type == "brute_force":
        return "Brute Force Attack"
    if event_type == "request_flood":
        return "Request Flood / Bot Activity"
    if event_type == "suspicious_login":
        return "Suspicious Login"

    return "Anomalous Activity"