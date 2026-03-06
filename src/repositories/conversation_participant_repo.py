from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.conversation_participant import ConversationParticipant


class ConversationParticipantRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(ConversationParticipant, session)
