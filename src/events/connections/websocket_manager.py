from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, list[WebSocket]] = {}

    async def connect(self, user_id: str, websocket: WebSocket):
        await websocket.accept()

        if user_id not in self.active_connections:
            self.active_connections[user_id] = []

        self.active_connections[user_id].append(websocket)

    def disconnect(self, user_id: str, websocket: WebSocket):
        self.active_connections[user_id].remove(websocket)

    async def send_to_users(self, user_ids: list[str], payload: dict):
        for user_id in user_ids:
            if user_id in self.active_connections:
                for ws in self.active_connections.get(user_id, []):
                    await ws.send_json(payload)


manager = ConnectionManager()
