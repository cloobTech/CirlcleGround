from src.schemas.space_schema import CreateSpaceSchema, UpdateSpaceAtCreation
from src.unit_of_work.unit_of_work import UnitOfWork
from src.core.exceptions import StoreAlreadyExistsError, PermissionDeniedError
from src.notification_factory.space_notification_factory import SpaceNotificationFactory
from src.enums.enums import UserRole

class SpaceService:
    def __init__(self, uow_factory: UnitOfWork) -> None:
        self.uow_factory = uow_factory

    async def create_space(self, host_id: str, data: CreateSpaceSchema):
        space_data = data.space
        async with self.uow_factory as uow:
            new_space = await uow.space_repo.create_space(host_id=host_id, data=space_data)


        return {
            "id": new_space.id,
            "message": "Space created successfully "
        }

    async def update_new_space(self, user_id: str, space_id: str, data: UpdateSpaceAtCreation):
        """Update a new space with addons"""
        async with self.uow_factory as uow:

            space = await uow.space_repo.get_space_by_id(space_id)
            if not space:
                raise StoreAlreadyExistsError(message="Space not found in database", details={
                    "recommendation": "kindly check space details again"
                })
            user = await uow.user_repo.get_by_id(id=user_id)
            if space.host_id != user_id or user.role not in [UserRole.ADMIN, UserRole.HOST, UserRole.SUPER_ADMIN]:
                raise PermissionDeniedError(
                    message="Access denied: Only host or admin can update new space",
                    details={"recommendation": "Check user details"},
                )
            # create addons
            for addon in data.addons:
                await uow.space_addon_repo.create(space.id, addon)

            # create usecases
            for usecase in data.use_cases:
                await uow.space_usecase_repo.create(space.id, usecase)

            # create rules
            for rule in data.rules:
                await uow.space_rule_repo.create(space.id, rule)

            # create pricings
            for pricing in data.pricings:
                await uow.space_pricing_repo.create(space.id, pricing)

            # create custom_amenities
            for custom_amenity in data.custom_amenities:
                await uow.custom_amenity_repo.create(space.id, custom_amenity)

            # create amenity_ids
            for amenity_id in data.amenity_ids:
                await uow.space_amenity_repo.create(space.id, amenity_id)

            # create operation hours
            if len(data.operation_hours) < 7:
                raise ValueError(
                    "Operation hours must be provided for all days of the week")
            for operation_hour in data.operation_hours:
                await uow.space_operating_hour_repo.create(space.id, operation_hour)

            space.status = data.status
            uow.collect_event(SpaceNotificationFactory.space_created(space, space.host_id))

        return {
            "id": space.id,
            "message": "Space updated successfully"
        }

    async def search_spaces(self, query: str, limit: int = 10):
        """Search for spaces based on a query string."""
        async with self.uow_factory as uow:
            spaces = await uow.space_repo.search_spaces(query=query, limit=limit)
        return spaces
