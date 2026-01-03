from repository.base import BaseRepository

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.user import User
from pydantic import EmailStr

class UserRepository(BaseRepository[User]):

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(User, session)

    async def get_by_email(self, email: EmailStr):
        result = await self.session.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()
    
    