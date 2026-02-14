from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.user import User
from src.schemas.location_schema import LocationSchema
from src.services.location_service import LocationService
from src.api.v1.dependencies import get_location_service, get_current_user

location_router = APIRouter(prefix="/api/v1/locations", tags=["Locations"])


@location_router.post("/")
async def create_location(location_data: LocationSchema, service: LocationService = Depends(get_location_service), user: User = Depends(get_current_user)):
    response = await service.add_location(location_data)
    return response


@location_router.get("/search")
async def search_location(search_string: str, service: LocationService = Depends(get_location_service), user: User = Depends(get_current_user)):
    response = await service.search_location(search_string)
    return response
