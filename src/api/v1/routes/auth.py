from fastapi import Depends, APIRouter
from src.auth.services import AuthService
from src.services.user_services import UserService
from src.models.user import User
from src.model_schemas.user_schema import CreateUserSchema, LoginUser
from src.api.v1.dependencies import get_auth_service, get_current_user, require_super_admin
from src.enums.enums import UserRole
from src.api.v1.dependencies import get_user_service



auth_router =APIRouter(prefix="/api/v1/auth", tags=["Auth"])



@auth_router.post("/")
async def create_customer(
    user_data: CreateUserSchema,
    user_service: UserService = Depends(get_user_service)
):
    response = await user_service.create_user(user_data, role=UserRole.GUEST_USER)
    return response

@auth_router.post("/admin")
async def add_admin_user(
    user_data: CreateUserSchema,
    current_user: User = Depends(get_current_user),
    auth_service: AuthService = Depends(get_auth_service),
    user: User = Depends(require_super_admin)
):
    response = await auth_service.create_admin(user_data, current_user=current_user)
    return response

@auth_router.post("/login")
async def login_user(
    login_details: LoginUser,
    auth_service: AuthService = Depends(get_auth_service)
):
    response = await auth_service.login(login_details=login_details)
    return response