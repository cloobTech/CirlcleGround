from datetime import datetime, timezone, timedelta
import secrets
import string
from src.schemas.user_schema import ReadUser
from src.core.exceptions import InvalidResetTokenError
from src.unit_of_work.unit_of_work import UnitOfWork
from src.models.user import User


class TokenUtils:
    def __init__(self, uow_factory: UnitOfWork) -> None:
        self.uow_factory = uow_factory

    def generate_token(self, length: int = 6):
        return ''.join(secrets.choice(string.digits) for _ in range(length))

    async def user_verification_token(self, user: User, expiry_time: int = 3):
        token = self.generate_token()
        user.verification_token = str(token)
        user.verification_token_expires_at = datetime.now(
            timezone.utc) + timedelta(minutes=expiry_time)
        return user.verification_token

    async def verify_token(self, token):
        user = await self.uow_factory.user_repo.verify_token(token)
        if not user:
            raise InvalidResetTokenError(message="Invalid token")

        expiry_time = user.verification_token_expires_at
        if not expiry_time:
            raise InvalidResetTokenError(message="Token has expired")

        if expiry_time < datetime.now(timezone.utc):
            raise InvalidResetTokenError(message="Token has expired")
        user.verification_token = None
        user.verification_token_expires_at = None
        return user



    # async def verify_token(self, token: str):
    # async with self.uow_factory:
    #     user = await self.uow_factory.user_repo.verify_token(token)

    #     if not user:
    #         raise InvalidResetTokenError(message="Invalid token")

    #     expiry_time = user.verification_token_expires_at
    #     if not expiry_time:
    #         raise InvalidResetTokenError(message="Token has expired")

    #     if expiry_time < datetime.now(timezone.utc):
    #         raise InvalidResetTokenError(message="Token has expired")

    #     user.verification_token = None
    #     user.verification_token_expires_at = None

    #     return user