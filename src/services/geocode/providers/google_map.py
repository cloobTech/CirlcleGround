import httpx
from src.services.geocode.base import GeoProvider


class GoogleProvider(GeoProvider):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = httpx.AsyncClient(timeout=5)

    async def geocode(self, address: str) -> dict | None:
        url = "https://maps.googleapis.com/maps/api/geocode/json"

        r = await self.client.get(url, params={
            "address": address,
            "key": self.api_key
        })

        if r.status_code != 200:
            return None

        data = r.json()["results"]
        if not data:
            return None

        result = data[0]

        return {
            "lat": result["geometry"]["location"]["lat"],
            "lng": result["geometry"]["location"]["lng"],
            "place_name": result["formatted_address"],
            "provider": "google"
        }
