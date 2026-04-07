def predict_threat(features: dict):
    score = 0.0

    if features.get("high_failed_attempts", 0) == 1:
        score += 0.35
    if features.get("high_request_count", 0) == 1:
        score += 0.30
    if features.get("is_new_ip", 0) == 1:
        score += 0.10
    if features.get("is_new_device", 0) == 1:
        score += 0.10
    if features.get("unknown_location", 0) == 1:
        score += 0.10
    if features.get("unusual_time", 0) == 1:
        score += 0.05

    score = min(score, 1.0)

    return {
        "prediction": "suspicious" if score >= 0.4 else "normal",
        "probability": round(score, 4)
    }