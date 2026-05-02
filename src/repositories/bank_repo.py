from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.repositories.base import BaseRepository
from src.models.bank import Bank
from src.schemas.bank_schema import CreateBank


class BankRepository(BaseRepository[Bank]):
    def __init__(self, session: AsyncSession):
        super().__init__(Bank, session)

    async def create_banks(self, bank_data: list[dict]):
        bank = [Bank(**data) for data in bank_data]
        created_banks = await self.bulk_create(bank)
        return created_banks
        


    async def get_by_currency(self, currency: str):
        stmt = select(self.model).where(self.model.currency == currency)
        result = await self.session.execute(stmt)
        return result.scalars().all()