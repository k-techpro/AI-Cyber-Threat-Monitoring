from fastapi import APIRouter

router = APIRouter(tags=["Analytics"])

# Dashboard summary
@router.get("/summary")
def get_summary():
    return {
        "total_logs": 0,
        "total_alerts": 0,
        "critical_alerts": 0,
        "high_alerts": 0
    }

# Top suspicious IPs
@router.get("/top-ips")
def get_top_ips():
    return {
        "data": []
    }

# Threat trend
@router.get("/threat-trend")
def get_threat_trend():
    return {
        "data": []
    }