from src.repositories.base import BaseRepository
from src.models.payments import Payment
from sqlalchemy.ext.asyncio import AsyncSession


class PaymentRepository(BaseRepository[Payment]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Payment, session)
    
    async def create_payment(self, payment: Payment):
        await self.create(payment)
        return payment
    
    async def get_all_payment(self):
        payments = await self.get_all()
        return payments