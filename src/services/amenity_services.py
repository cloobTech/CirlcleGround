from src.models.amenities import Amenity
from src.schemas.amenities_schema import CreateAmenity
from src.core.exceptions import PermissionDeniedError,  AmenityNotFoundError, SpaceAmenityNotFoundError
from src.unit_of_work.unit_of_work import UnitOfWork
from src.enums.enums import UserRole
from src.models.user import User


class AmenityService:
    def __init__(self, uow_factory: UnitOfWork) -> None:
        self.uow_factory = uow_factory

    async def add_amenities(self, amenities_data: CreateAmenity, user: User):
        "to add or update amenities"
        if user.role not in [UserRole.ADMIN, UserRole.SUPER_ADMIN]:
            raise PermissionDeniedError(
                message="Permission Denied",
                details={
                    "recommendation": "You must be an admin or super admin to add amenities"
                }
            )
        async with self.uow_factory as uow:
            created_amenities = []
            for item in amenities_data.amenities:
                name = item.name.strip().lower()
                existing_amenity = await uow.amenity_repo.check_by_name(name)
                if existing_amenity:
                    continue

                amenity = Amenity(
                    name=name,
                    category=item.category
                )

                new_amenity = await uow.amenity_repo.create(amenity)

                created_amenities.append(new_amenity)
            return created_amenities
        
    async def delete_amenity(self, user: User, amenity_id: str):
        "to delete an amenity"
        if user.role not in [UserRole.ADMIN, UserRole.SUPER_ADMIN]:
            raise PermissionDeniedError(
                message="Permission Denied",
                details={
                    "recommendation": "You must be an admin or super admin to delete amenity"
                }
            )
        amenity = await self.uow_factory.amenity_repo.get_by_id(amenity_id)
        if not amenity:
            raise AmenityNotFoundError(
                message="Amenity not found",
                details={
                    "recommendation": "Make sure user is passing the correct amenity ID"
                }
            )
        await self.uow_factory.amenity_repo.delete(amenity_id)
        return{
            "message": "amenity successfully deleted"
        }
    

    async def delete_multiple_amenities(self, user: User, amenities_id: list[str]):
        """to delete multiple amenities"""
        if user.role not in [UserRole.ADMIN, UserRole.SUPER_ADMIN]:
            raise PermissionDeniedError(
                message="Permission Denied",
                details={
                    "recommendation": "You must be an admin or super admin to delete amenity"
                }
            )
        deleted_amenities = await self.uow_factory.amenity_repo.delete_multiple_amenities(amenities_id)
        return {
            "message": "amenities successfully deleted",
            "total_rows_deleted": deleted_amenities
        }