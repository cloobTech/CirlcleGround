from src.models.location import Location
from src.model_schemas.location_schema import LocationSchema
from src.unit_of_work.unit_of_work import UnitOfWork


class LocationService:
    def __init__(self, uow_factory: UnitOfWork) -> None:
        self.uow_factory = uow_factory

    