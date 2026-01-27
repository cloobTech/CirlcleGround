from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from src.model_schemas.space_schema import CreateSpaceSchema
from src.models.user import User
from src.services.space_services import SpaceService
from src.api.v1.dependencies import require_admin, get_space_service



space_router = APIRouter(prefix="/api/v1/spaces", tags=["Spaces"])

@space_router.post("/")
async def list_space(space_data: CreateSpaceSchema, service: SpaceService = Depends(get_space_service), user: User = Depends(require_admin)):
    response = await service.create_space(space_data)
    return response