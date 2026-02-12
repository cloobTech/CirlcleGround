from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.custom_amenity import CustomAmenity


class CustomAmenityRepository(BaseRepository[CustomAmenity]):
    def __init__(self, session: AsyncSession):
        super().__init__(CustomAmenity, session)
