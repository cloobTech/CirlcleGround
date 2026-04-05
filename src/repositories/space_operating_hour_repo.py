from sqlalchemy import select
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
    

    #TBC
    async def update_space_operating_hours(self, space_id: str, data: SpaceOperationHourSchema):
        space_operating_hour = SpaceOperatingHour(
            space_id=space_id, **data.model_dump())
        return await super().update(space_operating_hour)
    
    async def get_space_operating_hour(self, space_id: str):
        stmt = select(self.model).where(self.model.space_id == space_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()