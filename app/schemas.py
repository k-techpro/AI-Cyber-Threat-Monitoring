from pydantic import BaseModel

class LogBase(BaseModel):
    username: str
    ip_address: str
    status: str
    failed_attempts: int
    request_count: int


class AlertResponse(BaseModel):
    id: int
    username: str
    ip_address: str
    threat_type: str
    severity: str
    risk_score: float

    class Config:
        from_attributes = True