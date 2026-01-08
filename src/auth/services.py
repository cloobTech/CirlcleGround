from src.models.user import User
from src.model_schemas.user_schema import CreateUserSchema, UserLoginSchema
from src.unit_of_work.unit_of_work import UnitOfWork
from src.core.exceptions import UserAlreadyExistsError, InvalidCredentialsError
from src.auth.security import verify_password
from src.auth.jwt import retrieve_token
from datetime import datetime, timezone
import re

class AuthService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
    
    async def create_user(self, user_data: CreateUserSchema):
        async with self.uow as uow:
            user = await uow.user_repo.get_user_by_email(email=user_data.email)
            if user:
                raise UserAlreadyExistsError(message="Email already exists in database", details={
                    "recommendation": "user should provide a different email"
                })
            user = User(**user_data.model_dump())
            created_user = await uow.user_repo.create(user)
            return created_user
        
    async def login(self, login_details: UserLoginSchema):
        if "@" in login_details.identifier:
            user = await self.uow.user_repo.get_user_by_email(email=login_details.identifier)
        # elif re.fullmatch(r"^\+?\d{7,15}$", login_details.identifier.strip()):
        #     user = await self.uow.user_repo.get_by_phone(login_details.identifier.strip())
    
        if not user or not verify_password(login_details.password, user.password):
            raise InvalidCredentialsError(details={
                "recommendations": "Ensure user passes the correct credentials"
            })
        user.last_login = datetime.now(timezone.utc)
        access_token = retrieve_token(user)
        return access_token