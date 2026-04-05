from fastapi import WebSocket
from collections import defaultdict


class WebSocketManager:
    def __init__(self):
        # user_id -> set of websocket connections
        self.active_connections: dict[str, set[WebSocket]] = defaultdict(set)

    async def connect(self, user_id: str, websocket: WebSocket):
        # websocket.accept() should NOT be here
        self.active_connections[user_id].add(websocket)

    def disconnect(self, user_id: str, websocket: WebSocket):
        if user_id in self.active_connections:
            self.active_connections[user_id].discard(websocket)

            # clean up empty user entries
            if not self.active_connections[user_id]:
                del self.active_connections[user_id]

    async def send_personal_message(self, user_id: str, message: dict):
        if user_id not in self.active_connections:
            return

        for connection in self.active_connections[user_id]:
            await connection.send_json(message)

    async def broadcast(self, message: dict):
        for connections in self.active_connections.values():
            for connection in connections:
                await connection.send_json(message)


manager = WebSocketManager()
