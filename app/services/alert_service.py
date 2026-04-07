from sqlalchemy.orm import Session
from app.models import Alert


def create_alert(db: Session, log_id: int, log: dict, detection_result: dict) -> Alert:
    alert = Alert(
        log_id=log_id,
        timestamp=log["timestamp"],
        username=log["username"],
        ip_address=log["ip_address"],
        threat_type=detection_result["threat_type"],
        severity=detection_result["severity"],
        risk_score=detection_result["risk_score"],
        reason=detection_result["reason"]
    )
    db.add(alert)
    db.commit()
    db.refresh(alert)
    return alert