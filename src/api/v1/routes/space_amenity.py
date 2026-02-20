from fastapi import Depends, APIRouter
from src.schemas.space_amenity_schema import BaseSpaceAmenity, MultipleSpaceAmenities
from src.services.space_amenity_service import SpaceAmenityService
from src.api.v1.dependencies import get_space_amenity_service, get_current_user
from src.models.user import User


space_amenity_router = APIRouter(prefix="/api/v1/space_amenities", tags=["Amenity"])

@auth_router.delete("/space_amenity_id")
async def delete_space_amenity(
    space_amenity_id: BaseSpaceAmenity,
    current_user: User = Depends(get_current_user),
    space_amenity_service: SpaceAmenityService = Depends(get_space_amenity_service)
):
    response = await space_amenity_service.delete_space_amenity(space_amenity_id, user=current_user)
    return response


@auth_router.delete("/bulk_delete_space_amenities")
async def bulk_delete_space_amenities(
    space_amenities_id: MultipleSpaceAmenities,
    current_user: User = Depends(get_current_user),
    space_amenity_service: SpaceAmenityService = Depends(get_space_amenity_service)
):
    response = await space_amenity_service.delete_multiple_space_amenities(user=current_user, space_amenities_id)
    return response