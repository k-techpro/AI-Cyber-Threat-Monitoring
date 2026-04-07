from sqlalchemy.orm import Session
from app.models import Incident


def create_incident_from_alert(db: Session, alert):
    incident_name = f"{alert.threat_type} from {alert.ip_address}"

    incident = Incident(
        created_at=alert.timestamp,
        incident_name=incident_name,
        source_ip=alert.ip_address,
        attack_pattern=alert.threat_type,
        severity=alert.severity,
        affected_users=alert.username,
        alert_count=1,
        status="OPEN",
        resolution_notes=""
    )
    db.add(incident)
    db.commit()
    db.refresh(incident)
    return incident