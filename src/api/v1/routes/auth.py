from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import BackgroundTasks
from pydantic import EmailStr
from src.auth.services import AuthService
from src.auth.schema import VerificationForm
from src.models.user import User
from src.schemas.user_schema import CreateUserSchema, LoginUser
from src.auth.schema import TokenResponse
from src.api.v1.dependencies import get_auth_service, get_current_user, require_super_admin, get_token_utils, get_user_service
from src.utils.token_utils import TokenUtils


auth_router = APIRouter(prefix="/api/v1/auth", tags=["Auth"])


@auth_router.post("/")
async def create_guest_user(
    user_data: CreateUserSchema,
    auth_service: AuthService = Depends(get_auth_service)

):
    response = await auth_service.create_user(user_data)
    return response


@auth_router.post("/admin")
async def add_admin_user(
    user_data: CreateUserSchema,
    current_user: User = Depends(require_super_admin),
    auth_service: AuthService = Depends(get_auth_service),
):
    response = await auth_service.create_admin(user_data, current_user)
    return response


@auth_router.post('/login', response_model=TokenResponse)
async def login_user(
    login_details: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(get_auth_service)
):
    username = login_details.username.strip()

    credentials = LoginUser(
        email=username if "@" in username else None,
        phone_number=None if "@" in username else username,
        password=login_details.password
    )

    return await auth_service.login(credentials)


@auth_router.post("/forgot-password")
async def forgot_password(
    email: VerificationForm,
    auth_service: AuthService = Depends(get_auth_service)
):
    response = await auth_service.request_password_reset_token(email.email)
    return response


@auth_router.post("/verify-verification-token")
async def verify_verification_token(
    token: str,
    auth_service: AuthService = Depends(get_auth_service)
):
    response = await auth_service.verify_token(token)
    return response


@auth_router.post("/request-verification-token")
async def request_verification_token(
    email: VerificationForm,
    auth_service: AuthService = Depends(get_auth_service)

):
    response = await auth_service.request_password_reset_token(email.email)
    return response


@auth_router.post("/verify-email")
async def verify_email(
    token: str,
    auth_service: AuthService = Depends(get_auth_service)

):
    response = await auth_service.verify_user_email(token)
    return response


@auth_router.post("/reset_password")
async def set_new_password(
    new_password: str,
    current_user: User = Depends(get_current_user),
    auth_service: AuthService = Depends(get_auth_service)
):
    response = await auth_service.reset_password(
        user_id=current_user.id,
        new_password=new_password
    )
    return response
