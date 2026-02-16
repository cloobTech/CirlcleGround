from src.repositories.base import BaseRepository
from src.models.booking import Booking
from src.enums.enums import BookingStatus
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class BookingRepository(BaseRepository[Booking]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Booking, session)

    async def get_user_bookings(self, guest_id: str) -> list[Booking]:
        stmt = select(Booking).where(Booking.guest_id == guest_id)
        result = await self.session.execute(stmt)
        return list(result.scalars().all())

    async def get_space_bookings(self, space_id: str) -> list[Booking]:
        stmt = select(Booking).where(Booking.space_id == space_id)
        result = await self.session.execute(stmt)
        return list(result.scalars().all())

    async def has_conflict(self, space_id, start, end):
        q = select(Booking).where(
            Booking.space_id == space_id,
            Booking.status.in_(
                [BookingStatus.CONFIRMED, BookingStatus.PENDING]),
            Booking.end_time > start,
            Booking.start_time < end
        )
        return (await self.session.execute(q)).scalar()

    async def get_space_unavailable_dates(self, space_id: str):
        stmt = select(Booking.start_time, Booking.end_time).where(
            Booking.space_id == space_id,
            Booking.status.in_(
                [BookingStatus.CONFIRMED, BookingStatus.PENDING])
        )

        result = await self.session.execute(stmt)
        return list(result.scalars().all())
    


