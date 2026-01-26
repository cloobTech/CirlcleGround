from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.user import User
from src.model_schemas.location_schema import LocationSchema
from src.services.location_service import LocationService
from src.api.v1.dependencies import require_admin, get_location_service

location_router = APIRouter(prefix="/api/v1/locations", tags=["Locations"])

@location_router.post("/")
async def create_location(location_data: LocationSchema, service: LocationService = Depends(get_location_service), user: User = Depends(require_admin)):
    response =await service.add_location(location_data)
    return response