from src.repositories.base import BaseRepository
from src.models.booking import Booking
from sqlalchemy.ext.asyncio import AsyncSession



class BookingRepository(BaseRepository[Booking]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Booking, session)

    async def get_user_bookings(self, user_id: str):
        bookings = await self.get_by_id(user_id)
        return bookings
    