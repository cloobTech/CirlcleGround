from src.models.location import Location
from src.model_schemas.location_schema import LocationSchema
from src.unit_of_work.unit_of_work import UnitOfWork
from src.core.exceptions import LocationAlreadyExistsError


class LocationService:
    def __init__(self, uow_factory: UnitOfWork) -> None:
        self.uow_factory = uow_factory

    async def add_location(self, location_data: LocationSchema):
       async with self.uow_factory:
            existing_location = await self.uow_factory.location_repo.check_by_region(
            country=location_data.country,
            state=location_data.state,
            city=location_data.city
            )
            if existing_location:
                raise LocationAlreadyExistsError(details={
                    "recommendation": "provide a different data"
                })
            data = location_data.model_dump()
            location = Location(**data)
            created_location = await self.uow_factory.location_repo.create(location)
            return created_location
