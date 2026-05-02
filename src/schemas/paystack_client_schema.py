from pydantic import BaseModel, EmailStr
from decimal import Decimal


class CreateRecipient(BaseModel):
    account_name: str
    account_number: str
    bank_code: str
    currency: str = "NGN"



class InitializeTransfer(BaseModel):
    amount: Decimal
    recipient: str
    reference: str 


class InitializePaymentResponseSchema(BaseModel):
    authorization_url: str
    reference: str
    access_code: str

class PaymentStatusResponseSchema(BaseModel):
    status: str
    email: EmailStr
    reference: str
    amount: Decimal

class PaystackBankResolveResponseSchema(BaseModel):
    account_name: str
    account_number: str