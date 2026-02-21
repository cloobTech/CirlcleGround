from fastapi import Depends, APIRouter
from src.api.v1.dependencies import get_current_user, get_uow, get_booking_service
from src.schemas.booking_schema import CreateBookingSchema
from src.unit_of_work.unit_of_work import UnitOfWork
from src.services.booking_services import BookingService
from src.models.user import User


booking_router = APIRouter(prefix="/api/v1/bookings", tags=["Bookings"])


@booking_router.post("/")
async def create_booking(booking_data: CreateBookingSchema, current_user: User = Depends(get_current_user), uow: UnitOfWork = Depends(get_uow)):

    booking_service = BookingService(uow)
    response = await booking_service.create_booking(booking_data=booking_data, guest_id=current_user.id)
    return response


@booking_router.get("/me")
async def get_user_bookings(current_user: User = Depends(get_current_user), booking_service: BookingService = Depends(get_booking_service)):
    response = await booking_service.get_user_bookings(guest_id=current_user.id)
    return response


@booking_router.delete("/{booking_id}")
async def delete_booking(booking_id: str, current_user: User = Depends(get_current_user), booking_service: BookingService = Depends(get_booking_service)):
    
    response = await booking_service.delete_booking(booking_id=booking_id, user_id=current_user.id)
    return response


@booking_router.put("/{booking_id}")
async def update_booking(booking_id: str, data: dict, current_user: User = Depends(get_current_user), booking_service: BookingService = Depends(get_booking_service)):
    response = await booking_service.update_booking(booking_id=booking_id, user=current_user.id, data=data)
    return response

@booking_router.get("/my-pending-bookings")
async def my_pending_bookings(
    booking_service: BookingService = Depends(get_booking_service),
    current_user: User = Depends(get_current_user)
):
    response = await booking_service.get_my_pending_bookings(guest_id=current_user.id)
    return response

@booking_router.get("/my-completed-bookings")
async def my_completed_bookings(
    booking_service: BookingService = Depends(get_booking_service),
    current_user: User = Depends(get_current_user)
):
    response = await booking_service.get_my_completed_bookings(guest_id=current_user.id)
    return response


@booking_router.get("/{guest_id}/user-pending-bookings")
async def user_pending_bookings(
    guest_id: str,
    booking_service: BookingService = Depends(get_booking_service),
    current_user: User = Depends(get_current_user)
):
    response = await booking_service.get_user_pending_bookings(guest_id: str, user=current_user)
    return response
