from fastapi import APIRouter

router = APIRouter(tags=["Alerts"])

# Get all alerts
@router.get("/")
def get_alerts():
    return {
        "status": "success",
        "message": "Alerts fetched successfully",
        "data": []
    }

# Get critical alerts
@router.get("/critical")
def get_critical_alerts():
    return {
        "status": "success",
        "message": "Critical alerts",
        "data": []
    }