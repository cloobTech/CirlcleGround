from sqlalchemy import select, delete, func
from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.amenities import Amenity
from src.schemas.amenities_schema import CreateAmenity


class AmenityRepository(BaseRepository[Amenity]):
    def __init__(self, session: AsyncSession):
        super().__init__(Amenity, session)
    
  
    async def check_by_name(self, name: str):
        """to check amenity by name"""
        result = await self.session.execute(select(self.model).where(self.model.name == name))
        return result.scalar_one_or_none()
    
    async def delete_multiple_amenities(self, amenities_id: list[str]):
        """to delete multiple amenities"""
        count_stmt = select(func.count()).where(self.model.id.in_(amenities_id))
        count = await self.session.execute(count_stmt)
        total = count.scalar_one()
        stmt = delete(self.model).where(self.model.id.in_(amenities_id))
        await self.session.execute(stmt)
        return total
    
    async def get_by_ids(self, ids: list[str]):
        stmt = select(self.model.id).where(self.model.id.in_(ids))
        result = await self.session.execute(stmt)
        return result
