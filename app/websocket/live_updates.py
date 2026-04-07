from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List
import asyncio
from datetime import datetime


router = APIRouter()


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def send_personal_message(self, message: dict, websocket: WebSocket):
        await websocket.send_json(message)

    async def broadcast(self, message: dict):
        disconnected = []
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except Exception:
                disconnected.append(connection)

        for conn in disconnected:
            self.disconnect(conn)


manager = ConnectionManager()


@router.websocket("/ws/live")
async def websocket_live_updates(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await manager.send_personal_message(
                {
                    "type": "heartbeat",
                    "message": "Live monitoring active",
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                },
                websocket
            )
            await asyncio.sleep(5)
    except WebSocketDisconnect:
        manager.disconnect(websocket)