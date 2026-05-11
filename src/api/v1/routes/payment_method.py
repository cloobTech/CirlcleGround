from fastapi import APIRouter, Depends
from src.models.user import User
from src.api.v1.dependencies import get_current_user, get_payment_method_service
from src.services.payment_method_service import PaymentMethodService
from src.enums.enums import Currency




payment_method_router = APIRouter(prefix="/api/v1/payment-methods", tags=["Payment Method"])

@payment_method_router.post("/")
async def initialize_card_authorization(
    user: User = Depends(get_current_user),
    payment_method_service: PaymentMethodService = Depends(get_payment_method_service)
):
    response = await payment_method_service.initialize_card_authorization(user_id=user.id)
    return response

