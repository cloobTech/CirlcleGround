from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.base import BaseRepository
from src.models.payment_method import PaymentMethod
from src.schemas.payment_method_schema import PaymentMethodSchema



class PaymentMethodRepository(BaseRepository[PaymentMethod]):
    def __init__(self, session: AsyncSession):
        super().__init__(PaymentMethod, session)
    
    async def add_payment_card(self, payment_method_details: dict):
        payload = PaymentMethod(
            user_id=payment_method_details["user_id"],
            authorization_code=payment_method_details["authorization_code"],
            expiry_date=payment_method_details["expiry_date"],
            last_four_digits=payment_method_details["last_four_digits"],
            reusable=payment_method_details["reusable"],
            card_type=payment_method_details["card_type"]
        )
        new_card = await self.create(payload)
        return new_card