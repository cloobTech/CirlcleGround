from src.repositories.base import BaseRepository
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.user import User
from pydantic import EmailStr

class UserRepository(BaseRepository[User]):

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(User, session)
        
    
    async def get_all_users(self):
        """to fetch all users from database"""
        users = self.get_all()
        return users
        
    async def get_user_by_email(self, email: EmailStr):
        """get user by email"""
        user = await self.get_by_email(email)
        return user
    
    async def update_password(self, user_id: str, hashed_password: str): 
        """update user password"""
        user = await self.get_by_id(user_id)
        if not user:
            return False
        
        user.password = hashed_password
        hashed_password = hashed_password
        return user
    
    async def verify_user(self, token: str, user_id: str):
        """verify user"""
        user = await self.get_by_id(user_id)
        if not user:
            return False
        verified_user = self.verify_reset_token(token)
        if not verified_user:
            return False
        
        user.is_email_verfied = True
        
    async def deactivate_user(self, user_id: str):
        """soft delete a user"""
        user = await self.get_by_id(user_id)
        if not user:
            return False
        await self.delete(user_id, soft=True)
        return True
    
    async def restore_user(self, user_id: str):
        """Restore a soft-deleted user."""
        user = await self.session.get(User, user_id)
        if not user or not hasattr(user, "is_deleted"):
            return False

        user.is_deleted = False
        return True
    
    async def get_user_by_phone_number(self, phonenumber: str):
        user = await self.get_by_phone_number(phonenumber)
        return user
    
    async def get_super_admin(self):
        result = await self.session.execute(select(User).where(User.is_super_admin == True))
        return result.scalar_one_or_none()
    
    