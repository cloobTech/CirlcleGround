from src.models.space import Space
from src.repositories.base import BaseRepository

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class SpaceRepository(BaseRepository[Space]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Space, session)

    async def list_space(self, space: Space):
        await self.create(space)
        return space

    async def get_all_spaces(self):
        spaces = await self.get_all()
        return spaces

    async def get_space_by_id(self, guest_id: str):
        space = await self.get_by_id(guest_id)
        return space

    async def update_space(self, space_id: str, data: dict):
        updated_space = await self.update(id=space_id, data=data)
        return updated_space
