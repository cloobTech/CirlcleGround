from src.models.user import User
from src.model_schemas.user_schema import CreateUserSchema, UserLoginSchema
from src.unit_of_work.unit_of_work import UnitOfWork
from src.core.exceptions import UserAlreadyExistsError, InvalidCredentialsError
from src.auth.security import verify_password, get_password_hash
from src.auth.jwt import retrieve_token
from datetime import datetime, timezone
import phonenumbers 
from phonenumbers.phonenumberutil import NumberParseException
import re

class AuthService:
    def __init__(self, uow_factory: UnitOfWork) -> None:
        self.uow_factory = uow_factory
    
    async def create_user(self, user_data: CreateUserSchema):
        user = await self.uow_factory.user_repo.get_user_by_email(email=user_data.email)
        if user:
            raise UserAlreadyExistsError(message="Email already exists in database", details={
                "recommendation": "user should provide a different email"
            })
        data = user_data.model_dump()
        data.pop("confirm_password") 
        data['password'] = get_password_hash(user_data.password)
        user = User(**data)
        created_user = await self.uow_factory.user_repo.create(user)
        return created_user
        
    async def login(self, login_details: UserLoginSchema):
        username = login_details.username.strip()
        password = login_details.password

        user = None

        if "@" in username:
            user = await self.uow_factory.user_repo.get_user_by_email(email=username.lower())
        else:
            try:
                # provide a default region if your users are mostly in one country, e.g. "US"
                num = phonenumbers.parse(username, "NG")
                if phonenumbers.is_valid_number(num):
                    phonenumber = phonenumbers.format_number(num, phonenumbers.PhoneNumberFormat.E164)
                    user = await self.uow_factory.user_repo.get_user_by_phone_number(phonenumber)
            except NumberParseException:
                raise InvalidCredentialsError(
                    details={"recommendations": "Phone number could not be parsed"}
                )

        if not user: 
            raise InvalidCredentialsError(details={"recommendations": "Ensure user passes the correct credentials"})
        if not verify_password(password, user.password):
            raise InvalidCredentialsError(details={"recommendations": "Ensure user passes the correct password"})

        user.last_login = datetime.now(timezone.utc)
        access_token = retrieve_token(user)
        return access_token
        