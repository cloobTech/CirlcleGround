from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.base import BaseRepository
from src.models.space_amenities import SpaceAmenity


class SpaceAmenityRepository(BaseRepository[SpaceAmenity]):
    def __init__(self, session: AsyncSession):
        super().__init__(SpaceAmenity, session)

    async def create(self, space_id: str, amenitiy_id: str):
        space_amenity = SpaceAmenity(space_id=space_id, amenity_id=amenitiy_id)
        return await super().create(space_amenity)
