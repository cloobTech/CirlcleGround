from fastapi import Depends, APIRouter
from src.api.v1.dependencies import get_current_user, get_auth_service, get_user_service
from src.models.user import User
from src.services.user_services import UserService

user_router = APIRouter(prefix="/api/v1/users", tags=["Users"])


@user_router.get("/me")
async def get_user_profile(current_user: User = Depends(get_current_user)):
    return current_user


@user_router.post("/update")
async def update_user_profile(user_id: str,  user_data: dict, current_user: User = Depends(get_current_user), auth_service: UserService = Depends(get_user_service)):

    response = await auth_service.update_user(user_id, user_data)
    return response
