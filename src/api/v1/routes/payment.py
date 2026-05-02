from fastapi import APIRouter, Depends
from decimal import Decimal
from src.services.payment_service import PaymentService
from src.models.user import User
from src.api.v1.dependencies import get_payment_service, get_current_user




payment_router = APIRouter(prefix="/api/v1/payments", tags=["Payments"])



@payment_router.post("/initialize-booking-payment")
async def initialize_booking_payment(booking_id: str,  amount_paid: Decimal, user: User = Depends(get_current_user), payment_service: PaymentService = Depends(get_payment_service)):
    response = await payment_service.initialize_booking_payment(email=user.email, amount_paid=amount_paid, booking_id=booking_id, user_id=user.id)
    return response
