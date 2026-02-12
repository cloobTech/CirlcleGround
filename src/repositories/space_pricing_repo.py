from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.space_pricing import SpacePricing
from src.schemas.space_schema import SpacePricingSchema


class SpacePricingRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(SpacePricing, session)

    async def create(self, space_id: str, data: SpacePricingSchema):
        obj = SpacePricing(space_id=space_id, **data.model_dump())
        return await super().create(obj)
