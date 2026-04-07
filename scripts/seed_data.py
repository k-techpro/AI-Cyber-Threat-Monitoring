import pandas as pd
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Log

DATA_PATH = "data/raw/historical_logs.csv"

def seed():
    db: Session = SessionLocal()
    df = pd.read_csv(DATA_PATH)

    for _, row in df.iterrows():
        log = Log(
            timestamp=row["timestamp"],
            username=row["username"],
            ip_address=row["ip_address"],
            location=row["location"],
            device_type=row["device_type"],
            browser=row["browser"],
            status=row["status"],
            failed_attempts=row["failed_attempts"],
            request_count=row["request_count"],
            event_type=row["event_type"],
            is_new_ip=row["is_new_ip"],
            is_new_device=row["is_new_device"],
            login_hour=row["login_hour"],
            processed=False
        )
        db.add(log)

    db.commit()
    db.close()
    print("Historical logs inserted.")

if __name__ == "__main__":
    seed()