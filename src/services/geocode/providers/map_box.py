import httpx
from src.services.geocode.base import GeoProvider


class MapboxProvider(GeoProvider):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = httpx.AsyncClient(timeout=5)

    async def geocode(self, address: str) -> dict | None:
        url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{address}.json"

        r = await self.client.get(url, params={
            "access_token": self.api_key,
            "limit": 1
        })

        if r.status_code != 200:
            return None

        data = r.json()["features"]
        if not data:
            return None

        result = data[0]

        return {
            "lat": result["center"][1],
            "lng": result["center"][0],
            "place_name": result["place_name"],
            "provider": "mapbox"
        }