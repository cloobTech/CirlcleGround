from src.schemas.space_schema import CreateSpaceSchema
from src.unit_of_work.unit_of_work import UnitOfWork
from src.core.exceptions import StoreAlreadyExistsError


class SpaceService:
    def __init__(self, uow_factory: UnitOfWork) -> None:
        self.uow_factory = uow_factory

    async def create_space(self, host_id: str, data: CreateSpaceSchema):
        space_data = data.space
        async with self.uow_factory as uow:
            space = await uow.space_repo.get_space_by_id(space_data.id)
            if space:
                raise StoreAlreadyExistsError(message="Spcae already exists in database", details={
                    "recommendation": "kindly check space details again"
                })
            new_space = await uow.space_repo.create_space(host_id=host_id, data=space_data)

            print(new_space.id)

            # create addons
            for addon in data.addons:
                await uow.space_addon_repo.create(new_space.id, addon)

            # create usecases
            for usecase in data.use_cases:
                await uow.space_usecase_repo.create(new_space.id, usecase)

            # create rules
            for rule in data.rules:
                await uow.space_rule_repo.create(new_space.id, rule)

            # create pricings
            for pricing in data.pricings:
                await uow.space_pricing_repo.create(new_space.id, pricing)

            # create custom_amenities
            for custom_amenity in data.custom_amenities:
                await uow.custom_amenity_repo.create(new_space.id, custom_amenity)

            # create amenity_ids
            for amenity_id in data.amenity_ids:
                await uow.space_amenity_repo.create(new_space.id, amenity_id)

        return {
            "id": new_space.id,
            "message": "Space created successfully  "
        }
