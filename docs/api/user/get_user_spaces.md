# Get User Spaces

**Endpoint:** `GET /api/v1/users/me/spaces`
**Description:** This endpoint allows users to get all spaces they have booked

**Content-Type:** `application/json`


### Headers

| Name            | Required | Description                      |
|-----------------|----------|----------------------------------|
| Authorization   | Yes      | Bearer access token              |


### Request Parameters

| Name                | Type    | Required | Description                                                    |
|---------------------| --------| -------- | -------------------------------------------------------------- |
| `include_bookings`  | boolean | Optional       | Whether to include bookings associated with each space.        |
| `booking_status`    | string  | Optional       | filter bookings by status which only applies when include_bookings = true        |
| `space_status`  | string | Optional      | filter space by status.        |






## Response

### Success Response
- **Status Code:** `200 OK`
```json
{
    "status": "success", 
    "message": "User spaces retrieved successfully", 
    "data": [
        {
        "id": "space_123", 
        "name": "Conference Room A", 
        "status": "ACTIVE", 
        "bookings": [
            {
            "id": "booking_001", 
            "status": "CONFIRMED", 
            "start_time": "2026-03-01T10:00:00", 
            "end_time": "2026-03-01T12:00:00"
            } 
        ] 
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
  "detail": "You do not have permission to get user's spaces"
}
```

#### Not Found
- **Status Code:** `404 Not Found`
```json
{
  "detail": "Space not found"
}
```

#### Internal Server Error
- **Status Code:** `500 Internal Server Error`
```json
{
  "detail": "An error occurred while getting spaces"
}
```
