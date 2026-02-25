from sqlalchemy import select, exists
from sqlalchemy.orm import selectinload, with_loader_criteria
from src.models.space import Space
from src.models.booking import Booking
from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.space_schema import SpaceSchema, SpaceQueryParams


class SpaceRepository(BaseRepository[Space]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Space, session)

    async def create_space(self, host_id: str, data: SpaceSchema) -> Space:
        print("host_id")
        space = Space(host_id=host_id, **data.model_dump())
        print(space.created_at)
        created_space = await self.create(space)
        return created_space

    async def get_user_spaces(self, user_id: str, params: SpaceQueryParams):
        stmt = select(Space).where(Space.host_id == user_id)

        if params.include_bookings and params.booking_status:
            stmt = stmt.where(
                exists().where(
                    (Booking.space_id == Space.id) &
                    (Booking.status == params.booking_status)
                )
            )

        if params.include_bookings:
            stmt = stmt.options(
                selectinload(Space.bookings),
                with_loader_criteria(
                    Booking,
                    Booking.status == params.booking_status,
                    include_aliases=True,
                )
            )

        if params.space_status:
            stmt = stmt.where(Space.status == params.space_status)

        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_space_by_id(self, space_id: str):
        space = await self.get_by_id(space_id)
        return space

    # async def update_space(self, space_id: str, data: dict):
    #     updated_space = await self.update(id=space_id, data=data)
    #     return updated_space
