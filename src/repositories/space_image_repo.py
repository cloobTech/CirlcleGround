from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.space_image import SpaceImage
from sqlalchemy import select, delete, update, func


class SpaceImageRepository(BaseRepository[SpaceImage]):
    def __init__(self, session: AsyncSession):
        super().__init__(SpaceImage, session)

    async def get_last_order(self, space_id: str):
        """Get the last order number"""
        last_order_result = await self.session.execute(
            select(SpaceImage.order).where(SpaceImage.space_id ==
                                           space_id).order_by(SpaceImage.order.desc())
        )

        last_order = last_order_result.scalars().first() or 0
        return last_order

    async def create(self, space_id: str, order: int):
        space_image = SpaceImage(space_id=space_id, order=order)
        return await super().create(space_image)

    async def delete_single__space_image(self, image_id: str):
        result = await self.session.execute(
            select(SpaceImage.space_id, SpaceImage.order)
            .where(SpaceImage.id == image_id)
        )
        row = result.first()

        if not row:
            return

        space_id, deleted_order = row

        # delete image
        await self.session.execute(
            delete(SpaceImage)
            .where(SpaceImage.id == image_id)
        )

        # shift orders down
        await self.session.execute(
            update(SpaceImage)
            .where(
                SpaceImage.space_id == space_id,
                SpaceImage.order > deleted_order
            )
            .values(order=SpaceImage.order - 1)
        )

    # async def delete_multiple_images(self, image_ids: list[str]):

    #     # fetch deleted images info
    #     result = await self.session.execute(
    #         select(SpaceImage.space_id, SpaceImage.order)
    #         .where(SpaceImage.id.in_(image_ids))
    #     )
    #     rows = result.all()

    #     if not rows:
    #         return

    #     space_id = rows[0].space_id
    #     deleted_orders = [row.order for row in rows]

    #     # delete selected images
    #     await self.session.execute(
    #         delete(SpaceImage)
    #         .where(SpaceImage.id.in_(image_ids))
    #     )

    #     # subquery: count how many deleted orders are before each image
    #     subq = (
    #         select(func.count())
    #         .where(func.unnest(deleted_orders) < SpaceImage.order)
    #         .scalar_subquery()
    #     )

    #     # shift remaining images once
    #     await self.session.execute(
    #         update(SpaceImage)
    #         .where(
    #             SpaceImage.space_id == space_id,
    #             SpaceImage.order > min(deleted_orders)
    #         )
    #         .values(order=SpaceImage.order - subq)
    #     )


    async def delete_multiple_images(self, image_ids: list[str]):

        result = await self.session.execute(
            select(SpaceImage.space_id, SpaceImage.order)
            .where(SpaceImage.id.in_(image_ids))
        )
        rows = result.all()

        if not rows:
            return

        space_id = rows[0].space_id
        deleted_orders = sorted([row.order for row in rows])

        await self.session.execute(
            delete(SpaceImage).where(SpaceImage.id.in_(image_ids))
        )

        for order in deleted_orders:
            await self.session.execute(
                update(SpaceImage)
                .where(
                    SpaceImage.space_id == space_id,
                    SpaceImage.order > order
                )
                .values(order=SpaceImage.order - 1)
            )
