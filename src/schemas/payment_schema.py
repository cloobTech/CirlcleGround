from pydantic import BaseModel


class MakePaymentSchema(BaseModel):
    booking_id: str
    amount: str
    payment_status: str
