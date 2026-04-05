from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.space_addon import SpaceAddon
from src.schemas.space_schema import SpaceAddonSchema


class SpaceAddonRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(SpaceAddon, session)

    async def create(self, space_id: str, data: SpaceAddonSchema)-> SpaceAddon:
        space_addon = SpaceAddon(space_id=space_id, **data.model_dump())
        return await super().create(space_addon)
