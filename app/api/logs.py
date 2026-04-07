from fastapi import APIRouter

router = APIRouter(tags=["Logs"])

# Get all logs (dummy for now)
@router.get("/")
def get_logs():
    return {
        "status": "success",
        "message": "Logs fetched successfully",
        "data": []
    }

# Get recent logs
@router.get("/recent")
def get_recent_logs():
    return {
        "status": "success",
        "message": "Recent logs",
        "data": []
    }