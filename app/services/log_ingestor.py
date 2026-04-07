from sqlalchemy.orm import Session
from app.models import Log


def ingest_log(db: Session, event: dict) -> Log:
    log = Log(
        timestamp=event["timestamp"],
        username=event["username"],
        ip_address=event["ip_address"],
        location=event["location"],
        device_type=event["device_type"],
        browser=event["browser"],
        status=event["status"],
        failed_attempts=event["failed_attempts"],
        request_count=event["request_count"],
        event_type=event["event_type"],
        is_new_ip=event["is_new_ip"],
        is_new_device=event["is_new_device"],
        login_hour=event["login_hour"],
        processed=False
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log