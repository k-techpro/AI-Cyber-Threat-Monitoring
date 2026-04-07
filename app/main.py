from fastapi import FastAPI
from app.api import logs, alerts, analytics, incidents
from app.websocket.live_updates import router as websocket_router

app = FastAPI(title="AI Cyber Threat Monitoring API")

@app.get("/")
def root():
    return {"message": "Cyber Threat Monitoring System Running"}

app.include_router(logs.router, prefix="/logs")
app.include_router(alerts.router, prefix="/alerts")
app.include_router(analytics.router, prefix="/analytics")
app.include_router(incidents.router, prefix="/incidents")
app.include_router(websocket_router)