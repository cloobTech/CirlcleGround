from datetime import datetime, timezone
from src.unit_of_work.unit_of_work import UnitOfWork
from src.events.message_events import MessageCreatedEvent
from src.schemas.messaging import MessageSchema, UpdateMessageSchema
from src.core.exceptions import EntityNotFound, PermissionDeniedError


class MessagingService:
    def __init__(self, uow_factory: UnitOfWork) -> None:
        self.uow_factory = uow_factory

    def generate_direct_chat_key(self, user_id_1: str, user_id_2: str) -> str:
        sorted_ids = sorted([user_id_1, user_id_2])
        return f"{sorted_ids[0]}:{sorted_ids[1]}"

    async def start_conversation(self, sender_id: str, recipient_id: str):
        async with self.uow_factory as uow:
            chat_key = self.generate_direct_chat_key(sender_id, recipient_id)
            conversation = await uow.conversation_repo.get_conversation_by_chat_key(
                chat_key
            )
            if conversation:
                return conversation.id

            conversation = await uow.conversation_repo.create_conversation()
            conversation.direct_chat_key = chat_key

            await uow.conversation_participant_repo.add_participant(
                conversation_id=conversation.id, user_id=sender_id
            )

            await uow.conversation_participant_repo.add_participant(
                conversation_id=conversation.id, user_id=recipient_id
            )

            return conversation.id

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

            recipient_id = await uow.conversation_participant_repo.get_conversation_participant_id(
                conversation_id
            )

            message_schema = MessageSchema(
                content=content,
                sender_id=sender_id,
                conversation_id=conversation_id
            )

            if not recipient_id:
                raise EntityNotFound(
                    message=f"Conversation with id {conversation_id} not found",
                    details={"conversation_id": conversation_id}
                )

            uow.collect_event(
                MessageCreatedEvent(
                    message=message_schema, recipient_id=recipient_id)
            )

        return message

    async def get_messages(self, conversation_id: str, limit: int = 50, offset: int = 0):
        async with self.uow_factory as uow:
            messages = await uow.message_repo.get_messages_by_conversation(
                conversation_id=conversation_id,
                limit=limit,
                offset=offset
            )
        return messages

    async def delete_message(self, message_id: str, user_id: str):
        async with self.uow_factory as uow:
            message = await uow.message_repo.get_by_id(message_id)
            if not message:
                raise EntityNotFound(
                    message=f"Message with id {message_id} not found",
                    details={"message_id": message_id}
                )
            if message.sender_id != user_id:
                raise PermissionDeniedError(
                    message=f"User with id {user_id} does not have permission to delete this message",
                    details={"message_id": message_id, "user_id": user_id}
                )
            await uow.message_repo.delete(id=message_id, soft=True)
            return {"message": "Message deleted successfully"}

    async def update_message(self, message_id: str, user_id: str, data: UpdateMessageSchema):
        async with self.uow_factory as uow:
            message = await uow.message_repo.get_by_id(message_id)
            if not message:
                raise EntityNotFound(
                    message=f"Message with id {message_id} not found",
                    details={"message_id": message_id}
                )
            if message.sender_id != user_id:
                raise PermissionDeniedError(
                    message=f"User with id {user_id} does not have permission to edit this message",
                    details={"message_id": message_id, "user_id": user_id}
                )
            message.is_edited = True
            await uow.message_repo.update(id=message_id,
                                          data=data.model_dump(exclude_unset=True))
            return {"message": "Message updated successfully"}

    async def mark_conversation_as_read(self, conversation_id: str, user_id: str):
        async with self.uow_factory as uow:
            last_message = await uow.message_repo.get_last_message(
                conversation_id
            )

            await uow.conversation_participant_repo.update(
                filters={
                    "conversation_id": conversation_id,
                    "user_id": user_id
                },
                data={"last_read_at": last_message.created_at if
                      last_message else datetime.now(tz=timezone.utc)}
            )