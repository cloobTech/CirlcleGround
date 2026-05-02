from pydantic import BaseModel
from src.enums.enums import Currency


class CreateWallet(BaseModel):
    user_id: str
    currency: Currency
    account_number: str
    wallet_pin: str



