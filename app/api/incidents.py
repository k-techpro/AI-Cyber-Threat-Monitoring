from fastapi import APIRouter

router = APIRouter(tags=["Incidents"])

# Get all incidents
@router.get("/")
def get_incidents():
    return {
        "status": "success",
        "message": "Incidents fetched",
        "data": []
    }

# Get open incidents
@router.get("/open")
def get_open_incidents():
    return {
        "status": "success",
        "message": "Open incidents",
        "data": []
    }