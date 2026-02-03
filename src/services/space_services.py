from src.models.space import Space
from src.model_schemas.space_schema import CreateSpaceSchema
from src.unit_of_work.unit_of_work import UnitOfWork
from src.core.exceptions import StoreAlreadyExistsError


class SpaceService:
    def __init__(self, uow_factory: UnitOfWork) -> None:
        self.uow_factory = uow_factory
    
    async def create_space(self, space_data: CreateSpaceSchema):
       async with self.uow_factory:
            data = space_data.model_dump()
            space_id = data.get("id")
            space = await self.uow_factory.space_repo.get_space_by_id(space_id)
            if space:
                raise StoreAlreadyExistsError(message="Store already exists in database", details= {
                    "recommendation": "admin should provide another space details"
                })
            new_space = Space(**data)
            created_space = await self.uow_factory.space_repo.create(new_space)
            return created_space

    