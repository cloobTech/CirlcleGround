# Get Space Bookings

**Endpoint:** `GET /api/v1/spaces/{space_id}/available-dates`
**Description:** This endpoint allows users to get all available spaces

**Content-Type:** `application/json`


### Request Parameters

| Name        | Type   | Required | Description                                     |
| ----------- | ------ | -------- | ----------------------------------------------- |
| `space_id` | list   | Yes      | ID of the space    |


## Response

### Success Response
- **Status Code:** `200 OK`
```json
{
    "status": "success",
    "message": "Spaces retrieved successfully",
    "spaces": [
        {
            "id": "b2f6c8c4-3d4c-4d89-8c9f-123456789abc",
            "name": "Modern Co-Working Hub",
            "description": "A comfortable workspace for teams and individuals",
            "location": "Lekki, Lagos",
            "status": "published",
            "capacity": 20,
            "created_at": "2026-01-10T12:00:00",
            "updated_at": "2026-01-15T10:30:00",
            "amenities": {
                "id": "a1",
                "name": "WiFi",
                "category": "technology"
            },
            "pricing": {
                "price_type": "hourly",
                "price": 2500,
                "currency": "NGN"
            }
        }
    ]
}
```

### Error Response

#### Bad Request
- **Status Code:** `404 Bad Request`

```json
{
  "detail": "Invalid request parameters"
}
```
#### Unauthorized

- **Status Code:** `401 Unauthorized`
```json
{
  "detail": "Could not validate credentials"
}
```

#### Forbidden
- **Status Code:** `403 Forbidden`
```json
{
  "detail": "You do not have permission to get all spaces"
}
```

#### Not Found
- **Status Code:** `404 Not Found`
```json
{
  "detail": "Spaces not found"
}
```

#### Internal Server Error
- **Status Code:** `500 Internal Server Error`
```json
{
  "detail": "An error occurred while getting spaces"
}
```
