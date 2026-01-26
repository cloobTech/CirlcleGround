from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from src.model_schemas.user_schema import CreateUserSchema, LoginUser, UpdateUser
from src.unit_of_work.unit_of_work import UnitOfWork
from src.storage import db
from src.api.v1.dependencies import get_current_user, get_auth_service
from src.models.user import User
from src.enums.enums import UserRole
from src.auth.services import AuthService

user_router = APIRouter(prefix="/api/v1/users", tags=["Users"])



@user_router.get("/me")
async def get_user_profile(current_user: User = Depends(get_current_user)):
    return current_user

@user_router.post("/update")
async def update_user_profile(user_id: str,  user_data: UpdateUser, current_user: User = Depends(get_current_user), auth_service: AuthService = Depends(get_auth_service)):
    if current_user.id != user_id and current_user.role not in [UserRole.ADMIN, UserRole.SUPER_ADMIN]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to update this user"
        )
    async with auth_service.uow_factory:
        response = await auth_service.service.update_user(user_id, user_data)
        return response

