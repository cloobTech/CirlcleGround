from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.message import Message


class MessageRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(Message, session)

    async def create(self, conversation_id: str, sender_id: str, content: str) -> Message:
        data = Message(conversation_id=conversation_id,
                       sender_id=sender_id, content=content)
        return await super().create(data)
