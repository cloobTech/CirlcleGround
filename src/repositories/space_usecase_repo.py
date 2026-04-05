from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.space_use_case import SpaceUseCase
from src.schemas.space_schema import SpaceUseCaseSchema


class SpaceUseCaseRepository(BaseRepository[SpaceUseCase]):
    def __init__(self, session: AsyncSession):
        super().__init__(SpaceUseCase, session)

    async def create(self, space_id: str, data: SpaceUseCaseSchema):
        space_usecase = SpaceUseCase(space_id=space_id, **data.model_dump())
        return await super().create(space_usecase)
