from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.space_blackout import SpaceBlackout


class SpaceBlackoutRepository(BaseRepository[SpaceBlackout]):
    def __init__(self, session: AsyncSession):
        super().__init__(SpaceBlackout, session)
