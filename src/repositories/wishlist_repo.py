from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.wish_list import WishList
from sqlalchemy import select
from sqlalchemy.orm import selectinload


class WishListRepository(BaseRepository[WishList]):
    def __init__(self, session: AsyncSession):
        super().__init__(WishList, session)

    async def create(self, user_id: str, space_id: str):
        wish_list = WishList(user_id=user_id, space_id=space_id)
        return await super().create(wish_list)

    async def get_wishlist(self, user_id: str, space_id: str):
        stmt = select(WishList).where(
            WishList.user_id == user_id,
            WishList.space_id == space_id
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def list_user_wishlist(self, user_id: str) -> list[WishList]:
        stmt = (
            select(WishList)
            .where(WishList.user_id == user_id)
            .options(selectinload(WishList.space))
        )
        result = await self.session.execute(stmt)
        return list(result.scalars().all())
