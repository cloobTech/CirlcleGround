from datetime import datetime, timezone, timedelta
from pydantic import EmailStr
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException
from src.events.user_events import UserCreatedEvent, RequestPasswordResetEvent
from src.models.user import User
from src.auth.schema import TokenResponse
from src.schemas.user_schema import CreateUserSchema, LoginUser, ReadUser
from src.unit_of_work.unit_of_work import UnitOfWork
from src.core.exceptions import InvalidCredentialsError
from src.auth.security import verify_password, hash_password
from src.auth.jwt import retrieve_token
from src.services.user_services import UserService
from src.enums.enums import UserRole
from src.core.exceptions import PermissionDeniedError, UserNotFound, UserAlreadyExistsError
from src.utils.token_utils import TokenUtils


class AuthService:
    """Authentication service"""
    def __init__(self, uow_factory: UnitOfWork) -> None:
        self.uow_factory = uow_factory
        self.service = UserService(uow_factory)

    async def create_user(self, user_data: CreateUserSchema):
        """Register a new user"""
        async with self.uow_factory:
            token_utils = TokenUtils(self.uow_factory)
            user = await self.uow_factory.user_repo.get_user_by_email(email=user_data.email)
            if user:
                raise UserAlreadyExistsError(message="Email already exists in database", details={
                    "recommendation": "user should provide a different email"
                })

            user_data.password = hash_password(user_data.password)
            data = user_data.model_dump()
            user = User(**data)
            verification_token = await token_utils.user_verfication_token(user, expiry_time=10)
            created_user = await self.uow_factory.user_repo.create(user)
            # celery task (send verification token to user via mail)
            if verification_token:
                self.uow_factory.collect_event(UserCreatedEvent(
                    first_name=user.first_name, last_name=user.last_name, email=user.email, token=verification_token, event_type="NEW_USER_CREATED"))

            return ReadUser.model_validate(created_user)

    async def create_admin(self, user_data: CreateUserSchema, current_user: User):
        """To create admin"""
        async with self.uow_factory:
            if current_user.role != UserRole.SUPER_ADMIN:
                raise PermissionDeniedError(message="Access denied: Only Super admins can create an admin", details={
                    "recommendation": "Make sure you're passing the correct super admin_id"
                })
            user_data.role = UserRole.ADMIN
            return await self.create_user(user_data)

    async def login(self, login_details: LoginUser):
        """Login"""
        async with self.uow_factory:
            password = login_details.password
            user = None

            if login_details.email:
                user = await self.uow_factory.user_repo.get_user_by_email(email=login_details.email)
            else:
                if not login_details.phone_number:
                    raise InvalidCredentialsError(
                        details={"recommendations": "Phone number is required"}
                    )
                try:
                    num = phonenumbers.parse(login_details.phone_number, "NG")
                    if phonenumbers.is_valid_number(num):
                        phonenumber = phonenumbers.format_number(
                            num, phonenumbers.PhoneNumberFormat.E164)
                        user = await self.uow_factory.user_repo.get_user_by_phone_number(phonenumber)
                except NumberParseException as exc:
                    raise InvalidCredentialsError(
                        details={
                            "recommendations": "Phone number could not be parsed"}
                    ) from exc

            if not user:
                raise InvalidCredentialsError(
                    details={"recommendations": "Ensure user passes the correct credentials"})
            if not verify_password(password, user.password):
                raise InvalidCredentialsError(details={
                    "recommendations": "Ensure user passes the correct password"
                })

            user.last_login = datetime.now(timezone.utc)
            access_token = retrieve_token(user)
            return TokenResponse(
                access_token=access_token
            )

    async def verify_user_email(self, token: str):
        """Verify user email"""
        async with self.uow_factory:
            token_utils = TokenUtils(self.uow_factory)
            verified_user = await token_utils.verify_token(token)
            if not verified_user:
                return False
            verified_user.is_email_verified = True
            return True

    async def request_password_reset(self, email: EmailStr):
        """Request password reset"""
        async with self.uow_factory:
            token_utils = TokenUtils(self.uow_factory)
            user = await self.uow_factory.user_repo.get_user_by_email(email)
            if not user:
                raise UserNotFound(details={
                    "recommendations": "Ensure user passes the correct email"
                })
            verification_token = await token_utils.user_verification_token(user)
            self.uow_factory.collect_event(RequestPasswordResetEvent(
                    first_name=user.first_name, last_name=user.last_name, email=user.email, token=verification_token, event_type="PASSWORD_RESET"))
            expires_at = datetime.now(timezone.utc) + timedelta(minutes=15)
            updated_data = {
                "verification_token": verification_token,
                "verification_token_expires_at": expires_at
            }

            await self.uow_factory.user_repo.update(id=user.id, data=updated_data)
            return {
                "status": "success",
                "message": "Token successfully sent"
            }

    async def reset_password(self, user_id, new_password):
        """Reset password"""
        async with self.uow_factory:
            user = await self.uow_factory.user_repo.get_by_id(user_id)
            if not user:
                raise UserNotFound(message="User not found")
            password = hash_password(new_password)
            await self.uow_factory.user_repo.update(id=user_id, data={"password": password})
            return {
                "status": "success",
                "message": "Your password has been updated successfully"
            }
        