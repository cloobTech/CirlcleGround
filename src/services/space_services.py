from src.models.space import Space
from src.model_schemas.space_schema import CreateSpaceSchema
from src.unit_of_work.unit_of_work import UnitOfWork
from src.core.exceptions import StoreAlreadyExistsError


class SpaceService:
    def __init__(self, uow_factory: UnitOfWork) -> None:
        self.uow_factory = uow_factory
    
    async def create_space(self, store_data: CreateSpaceSchema):
        store = await self.uow_factory.space_repo.get_space_by_id(store_data.id)
        if store:
            raise StoreAlreadyExistsError(message="Store already exists in database", details= {
                "recommendation": "admin should provide another store details"
            })
        data = store_data.model_dump()
        new_store = CreateSpaceSchema(**data)
        created_store = await self.uow_factory.space_repo.create(new_store)
        return created_store

    