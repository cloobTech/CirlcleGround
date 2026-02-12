from fastapi import Depends, APIRouter
from src.schemas.space_schema import CreateSpaceSchema
from src.models.user import User
from src.services.space_services import SpaceService
from src.api.v1.dependencies import get_space_service, get_current_user
from src.unit_of_work.unit_of_work import UnitOfWork


space_router = APIRouter(prefix="/api/v1/spaces", tags=["Spaces"])


@space_router.post("/")
async def create_new_space(space_data: CreateSpaceSchema, service: SpaceService = Depends(get_space_service), user: User = Depends(get_current_user)):
    response = await service.create_space(host_id=user.id, data=space_data)
    return response
