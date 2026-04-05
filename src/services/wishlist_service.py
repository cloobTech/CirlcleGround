from src.unit_of_work.unit_of_work import UnitOfWork
from src.enums.enums import ResourceType, ActivityType
from src.schemas.activity_log_schema import ActivityLogSchema
from src.core.exceptions import EntityNotFound, UniqueViolationError, PermissionDeniedError


class WishListService:
    def __init__(self, uow_factory: UnitOfWork) -> None:
        self.uow_factory = uow_factory

    async def add_wishlist(self, user_id: str, space_id: str):
        try:
            async with self.uow_factory:
                space = await self.uow_factory.space_repo.get_by_id(space_id)
                if not space:
                    raise EntityNotFound(
                        message="Space not found", details={"recommendation": "Check space details"}
                    )
                if space.host_id == user_id:
                    raise PermissionDeniedError(
                        message="You can not add your own space to wishlist",
                        details={   
                            "recommendation": "Pass a diferent user_id"
                        }
                    )
                wishlist = await self.uow_factory.wishlist_repo.create(user_id, space_id)
                await self.uow_factory.activity_repo.log_activity(
                ActivityLogSchema(
                    user_id=user_id,
                    resource_type= ResourceType.WISHLIST,
                    resource_id=wishlist.id,
                    activity=ActivityType.WISHLIST_ADDED
                )
            )
                return wishlist
        except UniqueViolationError:
            async with self.uow_factory:
                existing_wishlist = await self.uow_factory.wishlist_repo.get_wishlist(user_id, space_id)
                return existing_wishlist

    async def remove_wishlist(self, user_id: str, space_id: str):
        async with self.uow_factory:
            wishlist = await self.uow_factory.wishlist_repo.get_wishlist(user_id, space_id)
            if not wishlist:
                raise EntityNotFound(
                    message="Wishlist not found", details={"recommendation": "Check wishlist details"}
                )
            await self.uow_factory.wishlist_repo.delete(id=wishlist.id)
            new_activity = await self.uow_factory.activity_repo.log_activity(
                ActivityLogSchema(
                    user_id=user_id,
                    resource_type= ResourceType.WISHLIST,
                    resource_id=wishlist.id,
                    activity=ActivityType.WISHLIST_REMOVED
                )
            )
            return {
                "message": new_activity.activity,
                "wishlist_id": wishlist.id
            }
