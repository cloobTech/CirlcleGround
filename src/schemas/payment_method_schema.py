from pydantic import BaseModel



class PaymentMethodSchema(BaseModel):
    user_id: str
    last_four_digits: str
    authorization_code: str
    expiry_date: str
    reusable: bool
    card_type: str
    
