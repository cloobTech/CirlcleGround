from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from src.auth.services import AuthService
from src.services.user_services import UserService
from src.models.user import User
from src.model_schemas.user_schema import CreateUserSchema
from src.api.v1.dependencies import get_auth_service, get_current_user, require_super_admin
from src.api.v1.dependencies import get_user_service
from src.core.exceptions import PermissionDeniedError



auth_router =APIRouter(prefix="/api/v1/auth", tags=["Auth"])



@auth_router.post("/")
async def add_user(
    user_data: CreateUserSchema,
    auth_service: AuthService = Depends(get_auth_service)
):
    async with auth_service.uow_factory:
        response = await auth_service.register_customer(user_data)
    return response

@auth_router.post("/admin")
async def add_admin_user(
    user_data: CreateUserSchema,
    current_user: User = Depends(get_current_user),
    auth_service: AuthService = Depends(get_auth_service),
    user: User = Depends(require_super_admin)
):
    async with auth_service.uow_factory:
        response = await auth_service.create_admin(user_data)
        return response

@auth_router.post("/login")
async def login_user(
    login_details: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(get_auth_service)
):
    async with auth_service.uow_factory:
        response = await auth_service.login(login_details=login_details)
    return response