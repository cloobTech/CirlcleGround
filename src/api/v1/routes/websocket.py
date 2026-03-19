from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from src.events.connections.websocket_manager import manager
from src.api.v1.dependencies import get_current_user
from src.unit_of_work.unit_of_work import UnitOfWork
from src.services.messaging_service import MessagingService
from src.storage import db


ws_router = APIRouter(prefix='/api/v1/websocket', tags=["WebSocket"])


@ws_router.websocket("/messages")
async def websocket_endpoint(
    websocket: WebSocket,
):
    await websocket.accept()

    token = websocket.query_params.get("token")
    conversation_id = websocket.query_params.get("conversation_id")
    if not token:
        await websocket.close(code=1008)
        return

    if not conversation_id:
        await websocket.close(code=1008)
        return

    # manually create session and uow
    async with db.get_session() as session:
        uow = UnitOfWork(session)

        try:
            # manually call your helper
            user = await get_current_user(token=token, uow=uow)

            await manager.connect(user.id, websocket)
            messaging_service = MessagingService(uow)

            last_messages = await messaging_service.get_messages(
                conversation_id=conversation_id,
                limit=50
            )
            await websocket.send_json({
                "type": "message_history",
                "conversation_id": conversation_id,
                "messages": [
                    {
                        "id": msg.id,
                        "sender_id": msg.sender_id,
                        "content": msg.content,
                        "created_at": msg.created_at.isoformat(),
                        "is_edited": msg.is_edited
                    }
                    for msg in last_messages
                ]
            })

            while True:
                data = await websocket.receive_json()
                await messaging_service.send_message(
                    conversation_id=conversation_id,
                    sender_id=user.id,
                    content=data["content"]
                )

        except WebSocketDisconnect:
            manager.disconnect(user.id, websocket)

        except Exception as e:
            if user:
                manager.disconnect(user.id, websocket)
            await websocket.close()
            print("WebSocket error:", e)
