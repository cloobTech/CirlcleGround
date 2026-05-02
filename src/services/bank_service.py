from src.unit_of_work.unit_of_work import UnitOfWork
from src.schemas.bank_schema import CreateBank
from src.integrations.paystack.banks import paystack_bank_client



class BankService:
    def __init__(self, uow_factory: UnitOfWork):
        self.uow_factory = uow_factory
        
    
    async def get_banks(self, currency: str):
        async with self.uow_factory as uow:
            banks = await uow.bank_repo.get_by_currency(currency)
    
            if not banks:
                payload = await paystack_bank_client.get_banks(currency)
                created_banks = await uow.bank_repo.create_banks(payload)
                return created_banks

