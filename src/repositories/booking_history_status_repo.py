from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.booking_history import BookingStatusHistory
from src.schemas.booking_schema import BookingHistorySchema


class BookingHistoryStatusRepository(BaseRepository[BookingStatusHistory]):
    def __init__(self, session: AsyncSession):
        super().__init__(BookingStatusHistory, session)

    async def create(self, booking_id: str,  obj: BookingHistorySchema):
        booking_history = BookingStatusHistory(
            booking_id=booking_id, **obj.model_dump())
        return await super().create(booking_history)
