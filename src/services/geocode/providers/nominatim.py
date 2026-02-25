import httpx
from src.services.geocode.base import GeoProvider


class NominatimProvider(GeoProvider):
    async def geocode(self, address: str) -> dict | None:
        url = "https://nominatim.openstreetmap.org/search"

        async with httpx.AsyncClient(timeout=5) as client:
            r = await client.get(url, params={
                "q": address,
                "format": "json",
                "limit": 1,
                "addressdetails": 1
            })

            print(r)

        if r.status_code != 200:
            print(r.status_code)
            return None

        data = r.json()
        if not data:
            return None

        print(f"Nominatim found {len(data)} results for address: {address}")
        print(f"Nominatim found {data} results for address: {address}")

        result = data[0]

        return {
            "lat": float(result["lat"]),
            "lng": float(result["lon"]),
            "place_name": result["display_name"],
            "address": {
                "country": result["address"]["country"],
                # "state": result["address"]["state"],
                "city": result.get("address", {}).get("city") or result.get("address", {}).get("town") or result.get("address", {}).get("village") or result.get("address", {}).get("hamlet") or result.get("address", {}).get("suburb") or result.get("address", {}).get("municipality")
            },
            "provider": "nominatim"
        }
