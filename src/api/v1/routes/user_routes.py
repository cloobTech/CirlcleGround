from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from src.model_schemas.user_schema import CreateUserSchema, UserLoginSchema
from src.auth.services import AuthService
from src.unit_of_work.unit_of_work import UnitOfWork
from src.storage import db
from src.api.v1.dependencies import get_current_user, get_uow, get_auth_service
from src.models.user import User


user_router = APIRouter(prefix="/api/v1/users", tags=["Users"])

@user_router.post("/")
async def add_user(
    user_data: CreateUserSchema,
    auth_service: AuthService = Depends(get_auth_service)
):
    async with auth_service.uow_factory:
        response = await auth_service.create_user(user_data=user_data)
    return response
    
@user_router.post("/login")
async def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(get_auth_service)
):
    async with auth_service.uow_factory:
        response = await auth_service.login(login_details=form_data)
    return response
    
@user_router.get("/profile")
async def get_user_profile(current_user: User = Depends(get_current_user)):
    return current_user

