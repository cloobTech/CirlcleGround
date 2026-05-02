from sqlalchemy import select
from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.wallet import Wallet
from src.schemas.wallet_schema import CreateWallet



class WalletRepository(BaseRepository[Wallet]):
    def __init__(self, session: AsyncSession):
        super().__init__(Wallet, session)

    async def create_wallet(self, new_wallet: CreateWallet):
        wallet = Wallet(
          user_id=new_wallet.user_id,
          balance=0,
          currency=new_wallet.currency,
          account_number=new_wallet.account_number,
          wallet_pin=new_wallet.wallet_pin
        )
        created_wallet = await self.create(wallet)
        return created_wallet
    
    async def get_wallet_by_user_id(self, user_id: str):
        stmt = select(self.model).where(self.model.user_id == user_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
