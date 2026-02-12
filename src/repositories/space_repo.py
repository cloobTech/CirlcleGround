from src.models.space import Space
from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.space_schema import SpaceSchema


class SpaceRepository(BaseRepository[Space]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Space, session)

    async def create_space(self, host_id: str, data: SpaceSchema) -> Space:
        space = Space(host_id=host_id, **data.model_dump())
        created_space = await self.create(space)
        return created_space

    # async def list_space(self, space: Space):
    #     await self.create(space)
    #     return space

    # async def get_all_spaces(self):
    #     spaces = await self.get_all()
    #     return spaces

    async def get_space_by_id(self, space_id: str):
        space = await self.get_by_id(space_id)
        return space

    # async def update_space(self, space_id: str, data: dict):
    #     updated_space = await self.update(id=space_id, data=data)
    #     return updated_space
