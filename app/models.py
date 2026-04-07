from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from app.database import Base


class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(String, nullable=False)
    username = Column(String, nullable=False)
    ip_address = Column(String, nullable=False)
    location = Column(String, nullable=False)
    device_type = Column(String, nullable=False)
    browser = Column(String, nullable=False)
    status = Column(String, nullable=False)
    failed_attempts = Column(Integer, nullable=False, default=0)
    request_count = Column(Integer, nullable=False, default=0)
    event_type = Column(String, nullable=False)
    is_new_ip = Column(Boolean, nullable=False, default=False)
    is_new_device = Column(Boolean, nullable=False, default=False)
    login_hour = Column(Integer, nullable=False)
    processed = Column(Boolean, nullable=False, default=False)


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    log_id = Column(Integer, ForeignKey("logs.id"), nullable=False)
    timestamp = Column(String, nullable=False)
    username = Column(String, nullable=False)
    ip_address = Column(String, nullable=False)
    threat_type = Column(String, nullable=False)
    severity = Column(String, nullable=False)
    risk_score = Column(Float, nullable=False)
    reason = Column(String, nullable=False)


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(String, nullable=False)
    incident_name = Column(String, nullable=False)
    source_ip = Column(String, nullable=False)
    attack_pattern = Column(String, nullable=False)
    severity = Column(String, nullable=False)
    affected_users = Column(String, nullable=False)
    alert_count = Column(Integer, nullable=False, default=1)
    status = Column(String, nullable=False, default="OPEN")
    resolution_notes = Column(String, nullable=False, default="")