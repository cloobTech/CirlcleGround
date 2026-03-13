from src.unit_of_work.unit_of_work import UnitOfWork
from src.events.message_events import MessageCreatedEvent
from src.schemas.messaging import MessageSchema
from src.core.exceptions import EntityNotFound


class MessagingService:
    def __init__(self, uow_factory: UnitOfWork) -> None:
        self.uow_factory = uow_factory

    async def send_message(self, sender_id: str,
                           conversation_id: str,
                           content: str):
        async with self.uow_factory as uow:
            conversation = await uow.conversation_repo.get_by_id(conversation_id)

            if not conversation:
                raise EntityNotFound(
                    message=f"Conversation with id {conversation_id} not found",
                    details={"conversation_id": conversation_id}
                )

            message = await uow.message_repo.create(
                conversation_id=conversation_id,
                sender_id=sender_id,
                content=content
            )

            recipient_ids = [
                participant.user_id for participant in conversation.participants]

            message_schema = MessageSchema(
                content=content,
                sender_id=sender_id,
                conversation_id=conversation_id
            )

            uow.collect_event(
                MessageCreatedEvent(
                    message=message_schema, recipient_ids=recipient_ids)
            )

        return message
