from fastapi import Depends, APIRouter
from src.api.v1.dependencies import get_current_user, get_uow
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
async def get_user_bookings(current_user: User = Depends(get_current_user), uow: UnitOfWork = Depends(get_uow)):
    booking_service = BookingService(uow)
    response = await booking_service.get_user_bookings(guest_id=current_user.id)
    return response


@booking_router.delete("/{booking_id}")
async def delete_booking(booking_id: str, current_user: User = Depends(get_current_user), uow: UnitOfWork = Depends(get_uow)):
    booking_service = BookingService(uow)
    response = await booking_service.delete_booking(booking_id=booking_id, user_id=current_user.id)
    return response


@booking_router.put("/{booking_id}")
async def update_booking(booking_id: str, data: dict, current_user: User = Depends(get_current_user), uow: UnitOfWork = Depends(get_uow)):
    booking_service = BookingService(uow)
    response = await booking_service.update_booking(booking_id=booking_id, data=data)
    return response


