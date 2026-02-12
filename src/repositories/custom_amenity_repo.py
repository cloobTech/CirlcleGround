from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.custom_amenity import CustomAmenity
from src.schemas.space_schema import SpaceCustomAmenitySchema


class CustomAmenityRepository(BaseRepository[CustomAmenity]):
    def __init__(self, session: AsyncSession):
        super().__init__(CustomAmenity, session)

    async def create(self, space_id: str, data: SpaceCustomAmenitySchema):
        custom_amenity = CustomAmenity(space_id=space_id, **data.model_dump())
        return await super().create(custom_amenity)
