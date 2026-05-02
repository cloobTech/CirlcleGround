from pydantic import BaseModel
from decimal import Decimal
from pydantic import EmailStr



class TopUpWallet(BaseModel):
    
    amount: Decimal
    


class Withdraw(BaseModel):
    
    amount: Decimal
    