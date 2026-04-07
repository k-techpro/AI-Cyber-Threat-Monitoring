from app.database import SessionLocal
from app.services.attack_simulator import generate_event
from app.services.log_ingestor import ingest_log
import time

def run():
    print("Running simulator...")

    while True:
        db = SessionLocal()
        event = generate_event()
        ingest_log(db, event)
        db.close()

        print("Log generated:", event["event_type"])
        time.sleep(2)

if __name__ == "__main__":
    run()