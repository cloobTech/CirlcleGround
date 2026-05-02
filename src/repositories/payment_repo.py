from src.repositories.base import BaseRepository
from src.models.payments import Payment
from src.models.booking import Booking
from src.enums.enums import PaymentStatus
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload


class PaymentRepository(BaseRepository[Payment]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Payment, session)
    
    async def create_payment(self, payload: dict):
        
        payment = Payment(**payload)
        new_payment = await self.create(payment)
        return new_payment
    
    async def get_payment_by_booking(self, booking_id: str):
        stmt = select(self.model).where(self.model.booking_id == booking_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_all_payment(self):
        payments = await self.get_all()
        return payments
    
    async def get_payment_by_reference(self, reference_id: str):
        stmt = (
            select(Payment)
            .options(selectinload(Payment.booking).selectinload(Booking.space))
            .where(self.model.reference == reference_id)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    
    
