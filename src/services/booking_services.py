from src.unit_of_work.unit_of_work import UnitOfWork
from src.schemas.booking_schema import CreateBookingSchema, UpdateBookingSchema, UpdateBookingSchemaByHost, BookingQueryParams
from src.core.exceptions import EntityNotFound, ConflictError, PermissionDeniedError
from src.models.booking import Booking
from src.schemas.activity_log_schema import ActivityLogSchema
from src.enums.enums import UserRole, BookingStatus, ResourceType, ActivityType
from src.notification_factory.booking_notification_factory import BookingNotificationFactory


class BookingService:
    def __init__(self, uow_factory: UnitOfWork) -> None:
        self.uow_factory = uow_factory

    async def get_user_bookings(self, guest_id: str, params: BookingQueryParams):
        async with self.uow_factory:
            return await self.uow_factory.booking_repo.get_user_bookings(guest_id, params)

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
            booking = Booking(
                **booking_data.model_dump(), guest_id=guest_id)

            # for addon_id in booking_data.addon_ids:
            #     await uow.booking_addon_repo.create(booking.id, addon_id)
            
            
            new_booking = await self.uow_factory.booking_repo.create(booking)
            uow.collect_event(BookingNotificationFactory.booking_requested(new_booking.id, guest_id, space, space.host_id))
            await self.uow_factory.activity_repo.log_activity(
                ActivityLogSchema(
                    user_id=new_booking.guest_id,
                    resource_type= ResourceType.BOOKING,
                    resource_id=new_booking.id,
                    activity=ActivityType.BOOKING_CREATED
                )
            )
            return new_booking

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
            deleted_booking = await self.uow_factory.booking_repo.delete(booking_id)
            await self.uow_factory.activity_repo.log_activity(
                ActivityLogSchema(
                    user_id=user_id,
                    resource_type= ResourceType.BOOKING,
                    resource_id=booking.id,
                    activity=ActivityType.BOOKING_DELETED
                )
            )
            return deleted_booking

    async def update_booking(self, booking_id: str, user_id: str, data: UpdateBookingSchema):
        async with self.uow_factory:
            booking = await self.uow_factory.booking_repo.get_by_id(booking_id)
            if not booking:
                raise EntityNotFound(
                    message="Booking not found", details={"recommendation": "Check booking details"}
                )
            if booking.guest_id != user_id:
                raise PermissionDeniedError(
                    message="Access denied: Only guest can update their bookings",
                    details={"recommendation": "Check user details"},
                )
            if booking.status != BookingStatus.PENDING:
                raise ConflictError(
                    message="Only pending bookings can be updated",
                    details={"recommendation": "Check booking details"},
                )
            await self.uow_factory.booking_repo.update(id=booking_id, data=data.model_dump(exclude_unset=True))
            await self.uow_factory.activity_repo.log_activity(
                ActivityLogSchema(
                    user_id=user_id,
                    resource_type= ResourceType.BOOKING,
                    resource_id=booking.id,
                    activity=ActivityType.BOOKING_UPDATED
                )
            )
            return {
                "message": "Booking updated successfully",
                "booking_id": booking_id
            }

    async def update_booking_by_host(self, booking_id: str, user_id: str, data: UpdateBookingSchemaByHost):
        async with self.uow_factory:
            booking = await self.uow_factory.booking_repo.get_by_id(booking_id)
            if not booking:
                raise EntityNotFound(
                    message="Booking not found", details={"recommendation": "Check booking details"}
                )
            space = await self.uow_factory.space_repo.get_by_id(booking.space_id)
            if not space:
                raise EntityNotFound(
                    message="Space not found", details={"recommendation": "Check space details"}
                )
            if space.host_id != user_id:
                raise PermissionDeniedError(
                    message="Access denied: Only host can update this bookings",
                    details={"recommendation": "Check user details"},
                )

            await self.uow_factory.booking_repo.update(id=booking_id, data=data.model_dump(exclude_unset=True))
            await self.uow_factory.activity_repo.log_activity(
                ActivityLogSchema(
                    user_id=user_id,
                    resource_type= ResourceType.BOOKING,
                    resource_id=booking.id,
                    activity=ActivityType.BOOKING_UPDATED
                )
            )
            return {
                "message": "Booking updated successfully",
                "booking_id": booking_id
            }

    async def get_space_available_dates(self, space_id: str):
        async with self.uow_factory:
            space = await self.uow_factory.space_repo.get_by_id(space_id)
            if not space:
                raise EntityNotFound(
                    message="Space not found", details={"recommendation": "Check space details"}
                )
            return await self.uow_factory.booking_repo.get_space_unavailable_dates(space_id)