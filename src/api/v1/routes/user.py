from fastapi import Depends, APIRouter
from src.api.v1.dependencies import get_current_user, get_user_service
from src.models.user import User
from src.schemas.space_schema import SpaceQueryParams
from src.schemas.user_schema import UpdateUserSchema
from src.schemas.booking_schema import BookingQueryParams
from src.services.user_services import UserService

user_router = APIRouter(prefix="/api/v1/users", tags=["Users"])


@user_router.get("/me")
async def get_user_profile(current_user: User = Depends(get_current_user)):

    return current_user


@user_router.put("")
async def update_user_profile(user_data: UpdateUserSchema, current_user: User = Depends(get_current_user), user_service: UserService = Depends(get_user_service)):

    response = await user_service.update_user(user_data, user_id=current_user.id)
    return response


@user_router.get("/me/spaces")
async def get_user_spaces(current_user: User = Depends(get_current_user), user_service: UserService = Depends(get_user_service), params: SpaceQueryParams = Depends()):

    response = await user_service.get_user_spaces(current_user.id, params)
    return response


@user_router.get("/me/bookings")
async def get_user_bookings(current_user: User = Depends(get_current_user), user_service: UserService = Depends(get_user_service), params: BookingQueryParams = Depends()):

    response = await user_service.get_user_bookings(guest_id=current_user.id, params=params)
    return response


@user_router.get("/me/wishlist")
async def get_user_wishlist(current_user: User = Depends(get_current_user), user_service: UserService = Depends(get_user_service)):

    response = await user_service.get_user_wishlist(user_id=current_user.id)
    return response


@user_router.get("/me/notifications")
async def get_user_notifications(current_user: User = Depends(get_current_user), user_service: UserService = Depends(get_user_service)):
    response = await user_service.get_user_notifications(user_id=current_user.id)
    return response

@user_router.patch("/{notification_id}")
def update_user_notification(
    notification_id: str,
    current_user: User = Depends(get_current_user),
    service: UserService = Depends(get_user_service)
):

    recipient_notification = service.update_notification(
        notification_id=notification_id,
        recipient_id=current_user.id
    )
    return recipient_notification

@user_router.delete("/{notification_id}")
def delete_user_notification(
    notification_id: str,
    current_user: User = Depends(get_current_user),
    service: UserService = Depends(get_user_service)
):
    deleted_recipient_notification = service.delete_user_notification(notification_id, recipient_id=current_user.id)
    return deleted_recipient_notification


@user_router.delete("/me/notifications")
def delete_multiple_user_notifications(
    notification_ids: list[str],
    current_user: User = Depends(get_current_user),
    service: UserService = Depends(get_user_service)
):
    deleted_recipient_notifications = service.delete_multiple_user_notifications(notification_ids, recipient_id=current_user.id)
    return deleted_recipient_notifications

