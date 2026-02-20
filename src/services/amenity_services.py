from src.models.amenities import Amenity
from src.schemas.amenities_schema import CreateAmenity
from src.core.exceptions import PermissionDeniedError
from src.unit_of_work.unit_of_work import UnitOfWork
from src.enums.enums import UserRole
from src.models.user import User


class AmenityService:
    def __init__(self, uow_factory: UnitOfWork) -> None:
        self.uow_factory = uow_factory

    async def add_amenities(self, amenities_data: CreateAmenity, user: User):
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
