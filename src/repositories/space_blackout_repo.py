from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.repositories.base import BaseRepository
from src.schemas.space_schema import CreateSpaceBlackout
from src.models.space_blackout import SpaceBlackout


class SpaceBlackoutRepository(BaseRepository[SpaceBlackout]):
    def __init__(self, session: AsyncSession):
        super().__init__(SpaceBlackout, session)
    
    async def create(self, space_id: str, data: CreateSpaceBlackout) -> SpaceBlackout:
        space_blackout = SpaceBlackout(space_id=space_id, **data.model_dump())
        return await super().create(space_blackout)
    
    async def get_space_blackout(self, space_id: str)-> SpaceBlackout:
        stmt = select(self.model).where(self.model.space_id == space_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
