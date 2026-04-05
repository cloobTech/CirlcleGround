from abc import ABC, abstractmethod

class GeoProvider(ABC):
    @abstractmethod
    async def geocode(self, address: str) -> dict | None:
        pass

    # @abstractmethod
    # async def reverse_geocode(self, latitude: float, longitude: float) -> dict | None:
    #     pass