from uuid import uuid4
from pydantic import EmailStr
from src.unit_of_work.unit_of_work import UnitOfWork
from src.schemas.payment_method_schema import PaymentMethodSchema
from src.integrations.paystack.payment import paystack_payment_client
from src.integrations.paystack.customer import paystack_customer_client
from src.enums.enums import PaymentStatus, UserRole
from src.core.exceptions import PermissionDeniedError


class PaymentMethodService:
    def __init__(self, uow_factory: UnitOfWork):
        self.uow_factory = uow_factory

    async def initialize_card_authorization(self, user_id: str):     
        reference = f"CA-{uuid4().hex[:12].upper()}"
        async with self.uow_factory as uow:
            user = await uow.user_repo.get_by_id(user_id)
            if user.role != UserRole.HOST:
                raise PermissionDeniedError(
                    message="You do not have permisson to add card",
                    details={
                        "recommendation": "Pass a host id"
                    }
                )
        amount = 50
        # customer_code = await paystack_customer_client.create_customer(user.email, user.first_name, user.last_name, user.phone_number)
        result = await paystack_payment_client.initialize_payment(user_id=user_id, reference=reference, email=user.email, amount=amount)
        return result
    


    async def handle_card_authorization_success(self, card_payload: PaymentMethodSchema):
        # print("Yep")
        async with self.uow_factory:
            payload = card_payload.model_dump()
            new_card = await self.uow_factory.payment_method_repo.add_payment_card(payload)
            await paystack_customer_client.
            return new_card
        
        



    

    


        
        
        
        
        
        
        
        
        # async with self.uow_factory as uow:
        #     new_card = await uow.payment_method_repo.add_payment_card(payment_method_details)
        #     return new_card