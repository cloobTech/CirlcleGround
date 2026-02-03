from datetime import datetime, timezone, timedelta
from pydantic import EmailStr
import phonenumbers 
from phonenumbers.phonenumberutil import NumberParseException
from src.models.user import User
from src.auth.schema import TokenResponse
from src.model_schemas.user_schema import CreateUserSchema, LoginUser, ReadUser
from src.unit_of_work.unit_of_work import UnitOfWork
from src.core.exceptions import InvalidCredentialsError
from src.auth.security import verify_password, hash_password
from src.auth.jwt import retrieve_token
from src.services.user_services  import UserService
from src.enums.enums import UserRole
from src.core.exceptions import PermissionDeniedError, PasswordMismatchError, UserNotFound, UserAlreadyExistsError
from src.utils.token_utils import TokenUtils
from src.utils.email_service import email_service
from src.utils.email_templates import request_reset_password_template, verify_email_template




class AuthService:
    def __init__(self, uow_factory: UnitOfWork) -> None:
        self.uow_factory = uow_factory
        self.service = UserService(uow_factory)
    
    async def create_user(self, user_data: CreateUserSchema,  background_tasks, role: UserRole):
        async with self.uow_factory:
            token_utils = TokenUtils(self.uow_factory)
            user = await self.uow_factory.user_repo.get_user_by_email(email=user_data.email)
            if user:
                raise UserAlreadyExistsError(message="Email already exists in database", details={
                    "recommendation": "user should provide a different email"
                })
        
            data = user_data.model_dump()
            data["role"] = role
            data.pop("confirm_password")
            data['password'] = hash_password(user_data.password)
            user = User(**data)
            created_user = await self.uow_factory.user_repo.create(user)
            verification_token = await token_utils.user_verfication_token(user)
            background_tasks.add_task(
            email_service.send_email,
            to=user.email,
            subject="Verify Password",
            contents= verify_email_template(user, verification_token)
        )
            return ReadUser.model_validate(created_user)
    
    
    async def create_admin(self, user_data: CreateUserSchema, current_user: User, background_tasks)->list[User]: 
        async with self.uow_factory:
            if current_user.role !=UserRole.SUPER_ADMIN:
                raise PermissionDeniedError(message="Access denied: Only Super admins can create an admin", details={
                    "recommendation": "Make sure you're passing the correct super admin_id"
                })
            return await self.create_user(user_data, role=UserRole.ADMIN)
        
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
            
            return TokenResponse(
                token=access_token
            )
    async def verify_user_email(self, token: str):
        async with self.uow_factory:
            token_utils = TokenUtils(self.uow_factory)
            verified_user = await token_utils.verify_token(token)
            if not verified_user:
                return False
            verified_user.is_email_verfied = True


    async def request_password_reset(self, email: EmailStr, background_tasks):
       async with self.uow_factory:
            token_utils = TokenUtils(self.uow_factory)
            user = await self.uow_factory.user_repo.get_user_by_email(email)
            if not user:
                raise UserNotFound(details={
                    "recommendations": "Ensure user passes the correct email"
                })
            token = await token_utils.user_verfication_token(user)
            expires_at = datetime.now(timezone.utc) + timedelta(minutes=15)
            updated_data = {
                "reset_token": token,
                "reset_token_expires_at": expires_at
            }

            await self.uow_factory.user_repo.update(user.id, updated_data)
            background_tasks.add_task(
                email_service.send_email,
                to=user.email,
                subject="Reset Password",
                contents= request_reset_password_template(user, token)
            )
            return{
                "status": "success",
                "message": "Token successfully sent"
            }
    
    async def reset_password(self, user_id, new_password, confirm_password):
        async with self.uow_factory:
            user = await self.uow_factory.user_repo.get_by_id(user_id)
            if not user:
                raise UserNotFound(message="User not found")
            if confirm_password != new_password:
                raise PasswordMismatchError(message="Password mismatch")
            password = hash_password(new_password)
            await self.uow_factory.user_repo.update(user_id, {"password": password})
            return{
                    "status": "success",
                    "message": "Your password has been updated successfully"
                }