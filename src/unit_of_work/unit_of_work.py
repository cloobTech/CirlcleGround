from sqlalchemy.ext.asyncio import AsyncSession
from repository.customer_repo import 
class UnitOfWork:
    def __init__(self, session: AsyncSession):
        self.session = session

        self.
    
    async def __aenter__(self):
        await self.session.begin()
        return self
    
    async def __aexist__(self, exc_type, exc, tb):
        if exc:
            await self.session.rollback()
