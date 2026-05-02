from pydantic import BaseModel
from decimal import Decimal



    
    


class WithdrawalSchema(BaseModel):
    host_id: str
    amount:  Decimal
    bank_code: str
    account_number: str
    account_name: str
    request_id: str | None = None



    
