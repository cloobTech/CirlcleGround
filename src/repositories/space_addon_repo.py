from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.space_addon import SpaceAddon


class SpaceAddonRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(SpaceAddon, session)
