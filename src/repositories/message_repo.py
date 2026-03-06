from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.message import Message


class MessageRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(Message, session)
