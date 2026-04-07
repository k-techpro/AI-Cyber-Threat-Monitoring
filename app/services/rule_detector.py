from app.core.security_rules import evaluate_security_rules
from app.core.severity_engine import calculate_risk_score, get_severity, get_threat_type


def detect_threat_from_log(log: dict):
    reasons = evaluate_security_rules(log)

    if not reasons:
        return None

    risk_score = calculate_risk_score(log, reasons)
    severity = get_severity(risk_score)
    threat_type = get_threat_type(log)

    return {
        "threat_type": threat_type,
        "severity": severity,
        "risk_score": risk_score,
        "reason": ", ".join(reasons)
    }