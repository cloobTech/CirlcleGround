import secrets
import string
from src.model_schemas.user_schema import CreateUserSchema, ReadUser
from datetime import datetime, timezone, timedelta
from src.core.exceptions import InvalidResetTokenError
from src.unit_of_work.unit_of_work import UnitOfWork


class TokenUtils:
    def __init__(self, uow_factory: UnitOfWork) -> None:
        self.uow_factory = uow_factory
        
    
    async def generate_token(self, length: int = 6):
        return ''.join(secrets.choice(string.digits) for _ in range(length))

    async def user_verfication_token(self, user):
        token = await self.generate_token()
        user.verification_token = str(token)
        user.verification_token_expires_at = datetime.now(timezone.utc) + timedelta(minutes=15)
        return user.verification_token

    async def verify_token(self, token):
        user= await self.uow_factory.user_repo.verify_token(token)
        if not user:
            raise InvalidResetTokenError(message="Invalid token")
        if isinstance(user.verification_token_expires_at, str):
            expiry_time = datetime.fromisoformat(user.verification_token_expires_at.replace('Z', '+00:00'))
        else:
            expiry_time = user.verification_token_expires_at
    
        if expiry_time < datetime.now(timezone.utc):
            raise InvalidResetTokenError(message="Token has expired")
        user.verification_token = None
        user.verification_token_expires_at = None
        return ReadUser.model_validate(user)
    
