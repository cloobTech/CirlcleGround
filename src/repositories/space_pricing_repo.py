from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.space_pricing import SpacePricing


class SpacePricingRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(SpacePricing, session)
