import time
from app.database import SessionLocal
from app.services.attack_simulator import generate_event
from app.services.log_ingestor import ingest_log
from app.services.rule_detector import detect_threat_from_log
from app.services.alert_service import create_alert
from app.services.incident_service import create_incident_from_alert
from app.core.logger import get_logger
from app.core.logger import get_logger

logger = get_logger("scheduler")


def run_pipeline():
    logger.info("Scheduler pipeline started")

    while True:
        db = SessionLocal()
        try:
            event = generate_event()
            log = ingest_log(db, event)

            detection = detect_threat_from_log({
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
            })

            if detection:
                alert = create_alert(db, log.id, event, detection)
                logger.info(
                    f"Alert created | log_id={log.id} | "
                    f"type={alert.threat_type} | severity={alert.severity}"
                )

                if alert.severity in ["HIGH", "CRITICAL"]:
                    incident = create_incident_from_alert(db, alert)
                    logger.info(
                        f"Incident created | incident_id={incident.id} | "
                        f"name={incident.incident_name}"
                    )

        except Exception as e:
            logger.exception(f"Pipeline error: {e}")
        finally:
            db.close()

        time.sleep(2)