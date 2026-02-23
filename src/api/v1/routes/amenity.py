from fastapi import Depends, APIRouter
from src.services.amenity_services import AmenityService
from src.api.v1.dependencies import get_amenity_service, get_current_user
from src.schemas.space_amenity_schema import BaseSpaceAmenity, MultipleSpaceAmenities
from src.schemas.amenities_schema import DeleteAmenity, DeleteMultipleAmenities
from src.models.user import User
from src.schemas.amenities_schema import CreateAmenity



amenity_router = APIRouter(prefix="/api/v1/amenities", tags=["Amenity"])

@amenity_router.post("/")
async def create_amenity(
    amenity_data: CreateAmenity,
    current_user: User = Depends(get_current_user),
    amenity_service: AmenityService = Depends(get_amenity_service)
):
    response = await amenity_service.add_amenities(amenity_data,user=current_user)
    return response


@amenity_router.delete("/bulk_delete_amenities")
async def bulk_delete_amenities(
    amenities_id: DeleteMultipleAmenities,
    current_user: User = Depends(get_current_user),
    amenity_service: AmenityService = Depends(get_amenity_service)
):
    response = await amenity_service.delete_multiple_amenities(amenities_id.get_ids(), user=current_user)
    return response

@amenity_router.delete("/{amenity_id}")
async def delete_amenity(
    amenity_id: str,
    current_user: User = Depends(get_current_user),
    amenity_service: AmenityService = Depends(get_amenity_service)
):
    response = await amenity_service.delete_amenity(amenity_id, user=current_user)
    return response




