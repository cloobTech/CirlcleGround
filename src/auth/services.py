from datetime import datetime, timezone, timedelta
from pydantic import EmailStr
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException
from src.events.user_events import UserCreatedEvent
from src.models.user import User
from src.auth.schema import TokenResponse
from src.schemas.user_schema import CreateUserSchema, LoginUser, ReadUser
from src.schemas.activity_log_schema import ActivityLogSchema
from src.unit_of_work.unit_of_work import UnitOfWork
from src.core.exceptions import InvalidCredentialsError
from src.auth.security import verify_password, hash
from src.auth.jwt import retrieve_token
from src.services.user_services import UserService
from src.enums.enums import UserRole, ResourceType, ActivityType
from src.core.exceptions import PermissionDeniedError, UserNotFound, UserAlreadyExistsError, InvalidResetTokenError
from src.utils.token_utils import TokenUtils
from src.schemas.wallet_schema import CreateWallet
from src.enums.enums import Currency
from src.utils.numbers import normalize_phone_numbers


class AuthService:
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

            user_data.password = hash(user_data.password)
            data = user_data.model_dump()
            user = User(**data)
            verification_token = await token_utils.user_verfication_token(user, expiry_time=10)
            created_user = await self.uow_factory.user_repo.create(user)
            if user.role == UserRole.HOST:
                if not user_data.wallet_pin:
                    raise ValueError("Wallet pin is required for host users")
                phone_number = normalize_phone_numbers(user.phone_number)
                data = CreateWallet(
                    user_id=user.id,
                    currency=Currency.NGN,
                    account_number=phone_number,
                    wallet_pin=hash(user_data.wallet_pin)
                )  
                await self.uow_factory.wallet_repo.create_wallet(data)
            await self.uow_factory.activity_repo.log_activity(
                ActivityLogSchema(
                    user_id=created_user.id,
                    resource_type= ResourceType.USER,
                    resource_id=created_user.id,
                    activity=ActivityType.USER_CREATED
                )
            )
        
            # celery task (send verification token to user via mail)
            if verification_token:
                self.uow_factory.collect_event(UserCreatedEvent(
                    first_name=user.first_name, last_name=user.last_name, email=user.email, token=verification_token, event_type="NEW_USER_CREATED"))            
            return ReadUser.model_validate(created_user)

    async def create_admin(self, user_data: CreateUserSchema, current_user: User):

        if current_user.role != UserRole.SUPER_ADMIN:
            raise PermissionDeniedError(message="Access denied: Only Super admins can create an admin", details={
                "recommendation": "Make sure you're passing the correct super admin_id"
            })
        user_data.role = UserRole.ADMIN
        
        created_user = await self.create_user(user_data)
        
        return created_user

    async def login(self, login_details: LoginUser):
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
            await self.uow_factory.activity_repo.log_activity(
                ActivityLogSchema(
                    user_id=user.id,
                    resource_type= ResourceType.USER,
                    resource_id=user.id,
                    activity=ActivityType.USER_LOGIN.value
                )
            )
            return TokenResponse(
                access_token=access_token
            )

    async def verify_user_email(self, token: str):
        async with self.uow_factory:
            verified_user = await self.verify_token(token)
            if not verified_user:
                return False
            verified_user.is_email_verified = True
            return verified_user

    async def request_verification_token(self, email: EmailStr):
        async with self.uow_factory:
            token_utils = TokenUtils(self.uow_factory)
            user = await self.uow_factory.user_repo.get_user_by_email(email)
            if not user:
                raise UserNotFound(
                    message="User with the provided email does not exist",
                    details={
                        "recommendations": "Ensure user passes the correct email"
                    })
            token = await token_utils.user_verfication_token(user)
            updated_data = {
                "verification_token": token,
                "verification_token_expires_at": user.verification_token_expires_at
            }

            await self.uow_factory.user_repo.update(id=user.id, data=updated_data)

            return {
                "status": "success",
                "message": "Token successfully sent"
            }

    async def reset_password(self, user_id: str, new_password: str):
        async with self.uow_factory:
            user = await self.uow_factory.user_repo.get_by_id(user_id)
            if not user:
                raise UserNotFound(message="User not found")
            password = hash(new_password)
            await self.uow_factory.user_repo.update(id=user_id, data={"password": password})
            return {
                "status": "success",
                "message": "Your password has been updated successfully"
            }
    
    async def verify_token(self, token):
        user = await self.uow_factory.user_repo.verify_token(token)
        if not user:
            raise InvalidResetTokenError(message="Invalid token")

        expiry_time = user.verification_token_expires_at
        if not expiry_time:
            raise InvalidResetTokenError(message="Token has expired")

        
        if expiry_time.tzinfo is None:
            expiry_time = expiry_time.replace(tzinfo=timezone.utc)

        if expiry_time < datetime.now(timezone.utc):
            raise InvalidResetTokenError(message="Token has expired")
        
        user.verification_token = None
        user.verification_token_expires_at = None
        return user