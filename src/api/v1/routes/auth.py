from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import BackgroundTasks
from pydantic import EmailStr
from src.auth.services import AuthService
from src.models.user import User
from src.schemas.user_schema import CreateUserSchema, LoginUser
from src.auth.schema import TokenResponse
from src.api.v1.dependencies import get_auth_service, get_current_user, require_super_admin, get_token_utils
from src.utils.token_utils import TokenUtils


auth_router = APIRouter(prefix="/api/v1/auth", tags=["Auth"])


@auth_router.post("/")
async def create_customer(
    user_data: CreateUserSchema,
    auth_service: AuthService = Depends(get_auth_service)

):
    response = await auth_service.create_user(user_data)
    return response


@auth_router.post("/admin")
async def add_admin_user(
    background_tasks: BackgroundTasks,
    user_data: CreateUserSchema,
    current_user: User = Depends(get_current_user),
    auth_service: AuthService = Depends(get_auth_service),
    user: User = Depends(require_super_admin)
):
    response = await auth_service.create_admin(background_tasks, user_data, current_user=current_user)
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
    email: EmailStr,
    background_tasks: BackgroundTasks,
    auth_service: AuthService = Depends(get_auth_service)
):
    """forgot password"""
    response = await auth_service.request_password_reset(email, background_tasks)
    return response


@auth_router.post("/verify-reset-token")
async def verify_verification_token(
    token: str,
    token_utils: TokenUtils = Depends(get_token_utils)
):
    """Verify verification token"""
    response = await token_utils.verify_token(token)
    return response


@auth_router.post("/verify-email")
async def verify_email(
    token: str,
    auth_service: AuthService = Depends(get_auth_service)

):
    response = await auth_service.verify_user_email(token)
    return response

@auth_router.post("/reset-password")
async def reset_password(
    user_id: str,
    new_password: str,
    auth_service: AuthService = Depends(get_auth_service)
):
    response = await auth_service.reset_password(user_id, new_password)
    return response
    