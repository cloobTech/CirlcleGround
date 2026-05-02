from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.base import BaseRepository
from src.models.bank_account import BankAccount
from src.schemas.bank_account_schema import CreateBankAccount


class BankAccountRepository(BaseRepository[BankAccount]):
    def __init__(self, session: AsyncSession):
        super().__init__(BankAccount, session)
    
    async def add_bank_account(self, user_id: str, recipient: str, account_details: CreateBankAccount):
        data = account_details.model_dump()
        account = BankAccount(
            user_id=user_id,
            recipient=recipient,
            **data
        )
        created_account = await self.create(account)
        return created_account
    
    async def get_account_by_user_id(self, user_id: str):
        stmt = select(self.model).where(self.model.user_id == user_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    

