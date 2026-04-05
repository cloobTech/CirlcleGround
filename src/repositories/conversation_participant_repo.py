from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.conversation_participant import ConversationParticipant
from sqlalchemy import select


class ConversationParticipantRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(ConversationParticipant, session)

    async def get_conversation_participants_ids(self, conversation_id: str) -> list[str]:
        result = await self.session.execute(
            select(ConversationParticipant.user_id).where(
                ConversationParticipant.conversation_id == conversation_id
            )
        )
        return list(result.scalars().all())

    async def get_conversation_participant_id(self, conversation_id: str) -> str | None:
        result = await self.session.scalar(
            select(ConversationParticipant.user_id).where(
                ConversationParticipant.conversation_id == conversation_id
            )
        )
        return result

    async def add_participant(self, conversation_id: str, user_id: str):
        participant = ConversationParticipant(
            conversation_id=conversation_id,
            user_id=user_id
        )
        await self.create(participant)
