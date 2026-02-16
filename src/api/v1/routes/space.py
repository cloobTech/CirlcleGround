from fastapi import Depends, APIRouter, UploadFile
from src.schemas.space_schema import CreateSpaceSchema, UpdateSpaceAtCreation
from src.schemas.space_image_schema import DeleteSpaceImage
from src.models.user import User
from src.services.space_services import SpaceService
from src.services.space_image_service import SpaceImageService
from src.services.booking_services import BookingService
from src.api.v1.dependencies import get_space_service, get_current_user, get_uow
from src.unit_of_work.unit_of_work import UnitOfWork
from src.tasks.image_upload import upload_image


space_router = APIRouter(prefix="/api/v1/spaces", tags=["Spaces"])


@space_router.post("/")
async def create_new_space(space_data: CreateSpaceSchema, service: SpaceService = Depends(get_space_service), user: User = Depends(get_current_user)):
    response = await service.create_space(host_id=user.id, data=space_data)
    return response


@space_router.put("/{space_id}")
async def update_new_space(space_id: str, update_data: UpdateSpaceAtCreation, service: SpaceService = Depends(get_space_service), user: User = Depends(get_current_user)):
    response = await service.update_new_space(space_id=space_id, data=update_data)
    return response


@space_router.post("/{space_id}/images")
async def upload_images(files: list[UploadFile], space_id: str, uow: UnitOfWork = Depends(get_uow)):
    space_image_service = SpaceImageService(uow)
    response = await space_image_service.create_space_image(space_id=space_id, files=files)
    if not response:
        return
    for space_image, temp_path in response:
        upload_image.delay(temp_path=temp_path, image_id=space_image.id)
    return {
        "message": "Images upload started",
        "img_ids": [space_image.id for space_image, _ in response]
    }


@space_router.delete("/{space_id}/images")
async def delete_multiple_images(data: DeleteSpaceImage, uow: UnitOfWork = Depends(get_uow)):
    space_image_service = SpaceImageService(uow)
    response = await space_image_service.delete_multiple_images(image_ids=data.image_ids)
    return response


@space_router.delete("/{space_id}/images/{image_id}")
async def delete_space_image(image_id: str,  uow: UnitOfWork = Depends(get_uow)):
    space_image_service = SpaceImageService(uow)
    response = await space_image_service.delete_single_space_image(image_id)
    return response


@space_router.get("/{space_id}/bookings")
async def get_space_bookings(space_id: str, uow: UnitOfWork = Depends(get_uow), current_user: User = Depends(get_current_user)):
    booking_service = BookingService(uow)
    response = await booking_service.get_space_bookings(space_id=space_id, user_id=current_user.id)
    return response


@space_router.get("/{space_id}/available-dates")
async def get_all_spaces(space_id: str, uow: UnitOfWork = Depends(get_uow)):
    booking_service = BookingService(uow)
    response = await booking_service.get_space_available_dates(space_id=space_id)
    return response


# TODO: add pagination
# TODO: add calendar  view
