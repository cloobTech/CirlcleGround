from src.unit_of_work.unit_of_work import UnitOfWork
from src.schemas.booking_schema import CreateBookingSchema
from src.core.exceptions import EntityNotFound, ConflictError, PermissionDeniedError
from src.models.booking import Booking
from src.enums.enums import UserRole


class BookingService:
    def __init__(self, uow_factory: UnitOfWork) -> None:
        self.uow_factory = uow_factory

    async def get_user_bookings(self, guest_id: str):
        async with self.uow_factory:
            return await self.uow_factory.booking_repo.get_user_bookings(guest_id)

    async def get_space_bookings(self, space_id: str, user_id: str):
        async with self.uow_factory as uow:
            space = await uow.space_repo.get_by_id(id=space_id)
            if not space:
                raise EntityNotFound(
                    message="Space not found", details={"recommendation": "Check space details"}
                )
            user = await uow.user_repo.get_by_id(id=user_id)
            if not user:
                raise EntityNotFound(
                    message="User not found", details={"recommendation": "Check user details"}
                )
            if space.host_id != user.id or user.role not in [UserRole.ADMIN, UserRole.HOST, UserRole.SUPER_ADMIN]:
                raise PermissionDeniedError(
                    message="Access denied: Only host or admin can get space bookings",
                    details={"recommendation": "Check user details"},
                )
            return await uow.booking_repo.get_space_bookings(space_id)

    async def create_booking(self, guest_id: str, booking_data: CreateBookingSchema):
        async with self.uow_factory as uow:
            space = await uow.space_repo.get_by_id(id=booking_data.space_id)
            if not space:
                raise EntityNotFound(
                    message="Space not found", details={"recommendation": "Check space details"}
                )
            if space.host_id == guest_id:
                raise EntityNotFound(
                    message="You can't book your own space",
                    details={"recommendation": "Check space details"},
                )
            conflict = await uow.booking_repo.has_conflict(
                space_id=booking_data.space_id,
                start=booking_data.start_time,
                end=booking_data.end_time,
            )
            if conflict:
                raise ConflictError(
                    message="Space already booked for this period",
                    details={"recommendation": "Check booking details"},
                )
            new_booking = Booking(
                **booking_data.model_dump(), guest_id=guest_id)
            
            for addon_id in booking_data.addon_ids:
                await uow.booking_addon_repo.create(new_booking.id, addon_id)

            return await self.uow_factory.booking_repo.create(new_booking)

    async def delete_booking(self, booking_id: str, user_id: str):
        async with self.uow_factory:
            booking = await self.uow_factory.booking_repo.get_by_id(booking_id)
            if not booking:
                raise EntityNotFound(
                    message="Booking not found", details={"recommendation": "Check booking details"}
                )
            if booking.guest_id != user_id:
                raise PermissionDeniedError(
                    message="Access denied: Only guest can delete booking",
                    details={"recommendation": "Check user details"},
                )
            return await self.uow_factory.booking_repo.delete(booking_id)

    async def update_booking(self, booking_id: str, data: dict):
        async with self.uow_factory:
            return await self.uow_factory.booking_repo.update(id=booking_id, data=data)

    async def get_space_available_dates(self, space_id: str):
        async with self.uow_factory:
            space = await self.uow_factory.space_repo.get_by_id(space_id)
            if not space:
                raise EntityNotFound(
                    message="Space not found", details={"recommendation": "Check space details"}
                )
            return await self.uow_factory.booking_repo.get_space_unavailable_dates(space_id)
