from fastapi import APIRouter, WebSocket, Depends
from src.events.connections.websocket_manager import manager
from src.api.v1.dependencies import get_current_user, get_uow
from src.models.user import User
from src.unit_of_work.unit_of_work import UnitOfWork
from src.services.messaging_service import MessagingService


ws_router = APIRouter(prefix='/api/v1/websocket', tags=["WebSocket"])


@ws_router.websocket("/messages")
async def websocket_endpoint(
    websocket: WebSocket,
    # uow: UnitOfWork = Depends(get_uow),
    # user: User = Depends(get_current_user)
):
    token = websocket.query_params.get("token")
    user = await get_current_user(token)
    uow = await get_uow()

    messaging_service = MessagingService(uow)
    await manager.connect(user.id, websocket)

    try:
        while True:
            data = await websocket.receive_json()

            await messaging_service.send_message(
                conversation_id=data["conversation_id"],
                sender_id=user.id,
                content=data["content"]
            )

    except:
        manager.disconnect(user.id, websocket)
