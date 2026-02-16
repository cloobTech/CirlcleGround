from fastapi import Depends, APIRouter
from src.api.v1.dependencies import get_current_user, get_user_service
from src.models.user import User
from src.schemas.user_schema import UpdateUserSchema
from src.services.user_services import UserService

user_router = APIRouter(prefix="/api/v1/users", tags=["Users"])


@user_router.get("/me")
async def get_user_profile(current_user: User = Depends(get_current_user)):
    return current_user


@user_router.put("/{user_id}")
async def update_user_profile(user_data: UpdateUserSchema, current_user: User = Depends(get_current_user), user_service: UserService = Depends(get_user_service)):

    response = await user_service.update_user(user_data, user_id=current_user.id)
    return response
