from fastapi import Depends, APIRouter, Body
from src.schemas.messaging import UpdateMessageSchema
from src.services.messaging_service import MessagingService
from src.api.v1.dependencies import get_current_user, get_uow
from src.models.user import User
from src.unit_of_work.unit_of_work import UnitOfWork


message_router = APIRouter(
    prefix="/api/v1/messages", tags=["Messages"])


@message_router.post("/start_conversation")
async def start_conversation(
    recipient_id: str = Body(..., embed=True),
    user: User = Depends(get_current_user),
    uow: UnitOfWork = Depends(get_uow)
):
    service = MessagingService(uow)

    conversation_id = await service.start_conversation(
        sender_id=user.id,
        recipient_id=recipient_id
    )

    return {"conversation_id": conversation_id}


@message_router.patch("/{message_id}")
async def update_message(
    message_id: str,
    data: UpdateMessageSchema = Body(...),
    user: User = Depends(get_current_user),
    uow: UnitOfWork = Depends(get_uow)
):
    service = MessagingService(uow)

    response = await service.update_message(
        message_id=message_id,
        user_id=user.id,
        data=data
    )

    return response


@message_router.delete("/{message_id}")
async def delete_message(
    message_id: str,
    user: User = Depends(get_current_user),
    uow: UnitOfWork = Depends(get_uow)
):
    service = MessagingService(uow)

    response = await service.delete_message(
        message_id=message_id,
        user_id=user.id
    )

    return response


@message_router.post("/read")
async def mark_messages_as_read(
    body: dict = Body(...),
    user: User = Depends(get_current_user),
    uow: UnitOfWork = Depends(get_uow)
):
    conversation_id = body.get("conversation_id")
    if not conversation_id:
        return {"error": "conversation_id is required"}

    service = MessagingService(uow)
    await service.mark_conversation_as_read(
        conversation_id=conversation_id,
        user_id=user.id
    )

    return {"message": "Messages marked as read"}