from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.booking_addon import BookingAddon
from src.schemas.booking_schema import BookingAddonSchema


class BookingAddonRepository(BaseRepository[BookingAddon]):
    def __init__(self, session: AsyncSession):
        super().__init__(BookingAddon, session)

    async def create(self, booking_id: str, addon_id: str):
        booking_addon = BookingAddon(booking_id=booking_id, addon_id=addon_id)
        return await super().create(booking_addon)
