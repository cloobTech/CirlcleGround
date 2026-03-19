from sqlalchemy import select, func
from sqlalchemy.orm import selectinload
from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.message import Message
from src.models.conversation_participant import ConversationParticipant


class MessageRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(Message, session)

    async def create(self, conversation_id: str, sender_id: str, content: str) -> Message:
        data = Message(conversation_id=conversation_id,
                       sender_id=sender_id, content=content)
        return await super().create(data)

    async def get_messages_by_conversation(
        self,
        conversation_id: str,
        limit: int = 50,
        offset: int = 0
    ):
        stmt = (
            select(Message)
            .options(selectinload(Message.sender))
            .where(Message.conversation_id == conversation_id, Message.is_deleted == False)
            .order_by(Message.created_at.asc())
            .limit(limit)
            .offset(offset)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_unread_messages(self, conversation_id: str, user_id: str):
        subquery = (
            select(ConversationParticipant.last_read_at)
            .where(
                ConversationParticipant.conversation_id == conversation_id,
                ConversationParticipant.user_id == user_id
            )
            .scalar_subquery()
        )

        stmt = (
            select(Message)
            .where(
                Message.conversation_id == conversation_id,
                Message.created_at > subquery
            )
        )

        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_unread_count(self, conversation_id: str, user_id: str):
        subquery = (
            select(ConversationParticipant.last_read_at)
            .where(
                ConversationParticipant.conversation_id == conversation_id,
                ConversationParticipant.user_id == user_id
            )
            .scalar_subquery()
        )

        stmt = (
            select(func.count())
            .where(
                Message.conversation_id == conversation_id,
                Message.created_at > subquery
            )
        )

        result = await self.session.execute(stmt)
        return result.scalar()
    

    async def get_last_message(self, conversation_id: str):
        # Subquery to get the latest created_at for the conversation
        last_message_subq = (
            select(func.max(Message.created_at))
            .where(Message.conversation_id == conversation_id)
            .scalar_subquery()
        )

        # Get the actual message with that timestamp
        stmt = (
            select(Message)
            .where(
                Message.conversation_id == conversation_id,
                Message.created_at == last_message_subq
            )
        )

        result = await self.session.execute(stmt)
        last_message = result.scalars().first()
        return last_message
