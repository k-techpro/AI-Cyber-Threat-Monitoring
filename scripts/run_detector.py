from app.database import SessionLocal
from app.models import Log
from app.services.rule_detector import detect_threat_from_log
from app.services.alert_service import create_alert
from app.services.incident_service import create_incident_from_alert

def run():
    db = SessionLocal()

    logs = db.query(Log).filter(Log.processed == False).all()

    for log in logs:
        log_dict = {
            "timestamp": log.timestamp,
            "username": log.username,
            "ip_address": log.ip_address,
            "location": log.location,
            "device_type": log.device_type,
            "browser": log.browser,
            "status": log.status,
            "failed_attempts": log.failed_attempts,
            "request_count": log.request_count,
            "event_type": log.event_type,
            "is_new_ip": int(log.is_new_ip),
            "is_new_device": int(log.is_new_device),
            "login_hour": log.login_hour
        }

        detection = detect_threat_from_log(log_dict)

        if detection:
            alert = create_alert(db, log.id, log_dict, detection)

            if alert.severity in ["HIGH", "CRITICAL"]:
                create_incident_from_alert(db, alert)

        log.processed = True

    db.commit()
    db.close()
    print("Detection completed.")

if __name__ == "__main__":
    run()