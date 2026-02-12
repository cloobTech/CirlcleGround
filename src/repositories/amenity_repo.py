from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.amenities import Amenity


class AmenityRepository(BaseRepository[Amenity]):
    def __init__(self, session: AsyncSession):
        super().__init__(Amenity, session)
