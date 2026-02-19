from sqlalchemy import select
from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.amenities import Amenity
from src.schemas.amenities_schema import CreateAmenity


class AmenityRepository(BaseRepository[Amenity]):
    def __init__(self, session: AsyncSession):
        super().__init__(Amenity, session)
    
    async def create_amenities(self, amenities_data: CreateAmenity) -> Amenity:
        amenities = Amenity(**amenities_data.model_dump())
        created_amenities = await self.create(amenities)
        return created_amenities


    async def check_by_name(self, name: str):
        result = await self.session.execute(select(self.model).where(self.model.name == name))
        return result.scalar_one_or_none()