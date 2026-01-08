from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from src.model_schemas.user_schema import CreateUserSchema, UserLoginSchema
from src.auth.services import AuthService
from src.unit_of_work.unit_of_work import UnitOfWork
from src.storage import db

user_router = APIRouter(prefix="/api/v1/users", tags=["Users"])

@user_router.post("/")
async def add_user(
    user_data: CreateUserSchema,
    session: AsyncSession = Depends(db.get_session)
):
    async with UnitOfWork(session) as uow:
        auth_service = AuthService(uow)
        response = await auth_service.create_user(user_data=user_data)
        return response
    
@user_router.post("/login")
async def get_user(
    login_details: UserLoginSchema,
    session: AsyncSession = Depends(db.get_session)
):
    async with UnitOfWork(session) as uow:
        auth_service = AuthService(uow)
        response = await auth_service.login(login_details=login_details)
        return response