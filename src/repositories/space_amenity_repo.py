from sqlalchemy import select, delete, func
from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.base import BaseRepository
from src.models.space_amenities import SpaceAmenity


class SpaceAmenityRepository(BaseRepository[SpaceAmenity]):
    def __init__(self, session: AsyncSession):
        super().__init__(SpaceAmenity, session)

    async def create(self, space_id: str, amenitiy_id: str):
        space_amenity = SpaceAmenity(space_id=space_id, amenity_id=amenitiy_id)
        return await super().create(space_amenity)
    
    async def delete_multiple_space_amenities(self, space_amenities_id: list[str]):
        """to delete multiple space amenities"""
        count_stmt = select(func.count()).where(self.model.id.in_(space_amenities_id))
        count = await self.session.execute(count_stmt)
        total = count.scalar_one()
        await self.session.execute(delete(self.model).where(self.model.id.in_(space_amenities_id)))
        return total
    
    async def get_by_ids(self, ids: list[str]):
        stmt = select(self.model.id).where(self.model.id.in_(ids))
        result = await self.session.execute(stmt)
        return result