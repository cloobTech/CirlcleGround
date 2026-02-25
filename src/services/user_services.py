from src.schemas.user_schema import ReadUser, UpdateUserSchema
from src.schemas.booking_schema import BookingQueryParams
from src.schemas.space_schema import SpaceQueryParams
from src.unit_of_work.unit_of_work import UnitOfWork


class UserService:
    def __init__(self, uow_factory: UnitOfWork):
        self.uow_factory = uow_factory

    async def update_user(self, user_data: UpdateUserSchema, user_id: str):
        data = user_data.model_dump()
        async with self.uow_factory:
            user = await self.uow_factory.user_repo.update(user_id, data)
            return user_data

    async def get_user_spaces(self, user_id: str, params: SpaceQueryParams):
        async with self.uow_factory as uow:
            spaces = await uow.space_repo.get_user_spaces(user_id, params)
        return spaces

    async def get_user_bookings(self, guest_id: str, params: BookingQueryParams):
        async with self.uow_factory:
            return await self.uow_factory.booking_repo.get_user_bookings(guest_id, params)

    async def get_user_wishlist(self, user_id: str):
        async with self.uow_factory:
            return await self.uow_factory.wishlist_repo.list_user_wishlist(user_id)
