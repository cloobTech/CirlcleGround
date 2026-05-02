from pydantic import BaseModel



class CreateBankAccount(BaseModel):
    
    currency: str = "NGN"
    bank_code: str
    account_number: str
    account_name: str