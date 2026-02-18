from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.space_operating_hour import SpaceOperatingHour
from src.schemas.space_schema import SpaceOperationHourSchema


class SpaceOperatingHourRepository(BaseRepository[SpaceOperatingHour]):
    def __init__(self, session: AsyncSession):
        super().__init__(SpaceOperatingHour, session)

    async def create(self, space_id: str, data: SpaceOperationHourSchema):
        space_operating_hour = SpaceOperatingHour(
            space_id=space_id, **data.model_dump())
        return await super().create(space_operating_hour)
