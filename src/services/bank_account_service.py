from src.unit_of_work.unit_of_work import UnitOfWork
from src.schemas.bank_account_schema import CreateBankAccount
from src.schemas.paystack_client_schema import CreateRecipient
from src.core.exceptions import EntityNotFound
from src.integrations.paystack.banks import paystack_bank_client
from src.integrations.paystack.recipient import paystack_recipient_client
from src.core.pydantic_confirguration import config




class BankAccountService:
    def __init__(self, uow_factory: UnitOfWork):
        self.uow_factory = uow_factory
    

    async def add_bank_account(self, user_id: str, account_details: CreateBankAccount):

        if config.PAYSTACK_TEST_MODE == "test":
            resolved_account = {
                "account_name": account_details.account_name,
                "account_number": account_details.account_number
            }
            
        else:
            resolved_account = await paystack_bank_client.resolve_bank(account_details.account_number, account_details.bank_code)

        
        recipient = await paystack_recipient_client.create_recipient(recipient_data=CreateRecipient(
            account_number= resolved_account["account_number"],
            account_name=resolved_account["account_name"],
            bank_code=account_details.bank_code,
            currency=account_details.currency
        ))
        recipient = recipient["recipient_code"]
        async with self.uow_factory as uow:
            account = await uow.bank_account_repo.add_bank_account(user_id, recipient=recipient, account_details=account_details)
            return account
        
    
    
        