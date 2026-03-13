from fastapi import Depends, APIRouter
from src.schemas.space_amenity_schema import  MultipleSpaceAmenities
from src.services.space_amenity_service import SpaceAmenityService
from src.api.v1.dependencies import get_space_amenity_service, get_current_user
from src.models.user import User


space_amenities_router = APIRouter(prefix="/api/v1/space_amenities", tags=["Space Amenities"])


@space_amenities_router.delete("/bulk")
async def bulk_delete_space_amenities(
    space_amenities_id: MultipleSpaceAmenities,
    current_user: User = Depends(get_current_user),
    space_amenity_service: SpaceAmenityService = Depends(get_space_amenity_service)
):
    response = await space_amenity_service.delete_multiple_space_amenities(space_amenities_id.get_ids(), user=current_user)
    return response


@space_amenities_router.delete("/{space_amenity_id}")
async def delete_space_amenity(
    space_amenity_id: str,
    current_user: User = Depends(get_current_user),
    space_amenity_service: SpaceAmenityService = Depends(get_space_amenity_service)
):
    response = await space_amenity_service.delete_space_amenity(space_amenity_id, user=current_user)
    return response


