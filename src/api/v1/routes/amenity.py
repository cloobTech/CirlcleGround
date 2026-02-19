from fastapi import Depends, APIRouter
from src.services.amenity_services import AmenityService
from src.api.v1.dependencies import get_amenity_service, get_current_user
from src.models.user import User
from src.schemas.amenities_schema import CreateAmenity



amenity_router = APIRouter(prefix="/api/v1/amenity", tags=["Amenity"])

@amenity_router.post("/")
async def create_amenity(
    amenity_data: CreateAmenity,
    current_user: User = Depends(get_current_user),
    amenity_service: AmenityService = Depends(get_amenity_service)
):
    response = await amenity_service.add_amenities(amenity_data,user=current_user)
    return response
