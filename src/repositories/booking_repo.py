from src.repositories.base import BaseRepository
from src.models.booking import Booking
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class BookingRepository(BaseRepository[Booking]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Booking, session)

    
    async def get_user_bookings(self, guest_id: str) -> list[Booking]:
        stmt = select(Booking).where(Booking.guest_id == guest_id)
        result = await self.session.execute(stmt)
        return result.scalars().all()