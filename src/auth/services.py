from datetime import datetime, timezone
import phonenumbers 
from phonenumbers.phonenumberutil import NumberParseException
from fastapi.security import OAuth2PasswordRequestForm
from src.models.user import User
from src.model_schemas.user_schema import CreateUserSchema, LoginUser
from src.unit_of_work.unit_of_work import UnitOfWork
from src.core.exceptions import UserAlreadyExistsError, InvalidCredentialsError
from src.auth.security import verify_password, get_password_hash
from src.auth.jwt import retrieve_token
from src.services.user_services  import UserService
from src.enums.enums import UserRole
from src.core.exceptions import PermissionDeniedError
import re



class AuthService:
    def __init__(self, uow_factory: UnitOfWork) -> None:
        self.uow_factory = uow_factory
        self.service = UserService(uow_factory)
    
    
    async def create_admin(self, user_data: CreateUserSchema, current_user: User)->list[User]: 
        async with self.uow_factory:
            if current_user.role !=UserRole.SUPER_ADMIN:
                raise PermissionDeniedError(message="Access denied: Only Super admins can create an admin", details={
                    "recommendation": "Make sure you're passing the correct super admin_id"
                })
            return await self.service.create_user(user_data, role=UserRole.ADMIN)
        
    async def login(self, login_details: LoginUser):
        async with self.uow_factory:
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
            raise InvalidCredentialsError(details={
                "recommendations": "Ensure user passes the correct password"
            })
        


        user.last_login = datetime.now(timezone.utc)
        access_token = retrieve_token(user)
        print(access_token)
        return {
            "access_token": access_token,
            "token_type": "bearer"
        }