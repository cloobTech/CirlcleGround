from sqlalchemy import select
from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.wallet_transaction import WalletTransaction




class WalletTransactionRepository(BaseRepository[WalletTransaction]):
    def __init__(self, session: AsyncSession):
        super().__init__(WalletTransaction, session)
    
    async def create_wallet_transaction(self, payload: dict):
        wallet_transaction = WalletTransaction(**payload)
        created_transaction = await self.create(wallet_transaction)
        return created_transaction

    async def get_wallet_pending_withdrawals(self, wallet_id: str):
        stmt = select(self.model).where(self.model.wallet_id == wallet_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    async def get_transaction_by_reference(self, reference_id: str):
        stmt = select(self.model).where(self.model.reference == reference_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
        