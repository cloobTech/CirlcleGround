# Create Location

## Endpoint

`POST /api/v1/locations/`

## Description

This endpoint allows an administrator to create a new location in the system.
A location represents a geographical hierarchy consisting of a country, state, and city.

If a location with the same country, state, and city already exists, the request will be rejected.

🔐 Authentication Required: Yes (Super admin or Admin only)
🔑 Authorization: Bearer Token

---

## Request

The request should be made with `Content-Type: application/json` and include the following parameters:

| Parameter               | Type   | Required | Description                             |Example/Notes          |
|-------------------------|--------|----------|-----------------------------------------|-----------------------|
|`country`                |string  |Yes       |Country of the location                  |`"Nigeria"`            |
|`city`                  |string  |Yes        |City of the location                     |`"kano"`               |
|`state`                  |string  |Yes       |State of the location                    |`"state"`              |

### Example Request Body

```json
{
    "id": "location-uuid4-1234",
    "country": "Nigeria",
    "city": "kano",
    "state": "kano",
}
```

## Response
### Success Response
- **Status Code:** `200 OK`
```json
{
    "message": "Location successfully added"
}
```

### Error Response

#### Location Already Exist
- **Status Code:** `400 Bad Request`
```json
{
  "detail": "location already exist"
}
```