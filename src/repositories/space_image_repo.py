from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.space_image import SpaceImage


class SpaceImageRepository(BaseRepository[SpaceImage]):
    def __init__(self, session: AsyncSession):
        super().__init__(SpaceImage, session)
