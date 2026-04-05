from src.core.exceptions import PermissionDeniedError, SpaceAmenityNotFoundError
from src.unit_of_work.unit_of_work import UnitOfWork
from src.enums.enums import UserRole
from src.models.user import User


class SpaceAmenityService:
    def __init__(self, uow_factory: UnitOfWork) -> None:
        self.uow_factory = uow_factory

    async def delete_space_amenity(self, space_amenity_id: str, user: User,):
        async with self.uow_factory:
            if user.role not in [UserRole.ADMIN, UserRole.SUPER_ADMIN]:
                raise PermissionDeniedError(
                    message="Permission Denied",
                    details={
                        "recommendation": "You must be an admin or super admin to delete amenity"
                    }
                )
            space_amenity = await self.uow_factory.space_amenity_repo.get_by_id(space_amenity_id)
            if not space_amenity:
                raise SpaceAmenityNotFoundError(
                    message="Space amenity not found",
                    details={
                        "recommendation": "Make sure you pass the correct space amenity ID"
                    }
                )
            await self.uow_factory.space_amenity_repo.delete(space_amenity_id)
            return {
                "message": "space amenity successfully deleted",
            }

    async def delete_multiple_space_amenities(self, space_amenity_ids: list[str], user: User):
        """to delete multiple space amenities"""
        async with self.uow_factory:
            if user.role not in [UserRole.ADMIN, UserRole.SUPER_ADMIN]:
                raise PermissionDeniedError(
                    message="Permission Denied",
                    details={
                        "recommendation": "You must be an admin or super admin to delete space amenities"
                    }
                )
            deleted_space_amenities = await self.uow_factory.space_amenity_repo.delete_multiple_space_amenities(space_amenity_ids)
            return {
                "message": "space amenities successfully deleted",
                "total_rows_deleted": deleted_space_amenities
            }
