# Get User Bookings

**Endpoint:** `GET /api/v1/bookings/me`
**Description:** This endpoint allows users to get all available spaces

**Content-Type:** `application/json`


### Headers

| Name            | Required | Description                      |
|-----------------|----------|----------------------------------|
| Authorization   | Yes      | Bearer access token              |


## Response

### Success Response
- **Status Code:** `200 OK`
```json
{
    "status": "success",
     "message": "User bookings retrieved successfully", 
     "data": [
        {
            "booking_id": "bkg_123456", 
            "space": {
                "id": "space_001", 
                "name": "Conference Room A", 
                "location": "Lagos" 
            }, 
            "addons": [
                {
                    "id": "addon_01", 
                    "name": "Projector", 
                    "price": 2000 
                } 
            ],
            "start_time": "2026-02-20T10:00:00Z", 
            "currency": "NGN",
            "end_time": "2026-02-20T12:00:00Z", 
            "cancelled_time": "2026-02-20T11:00:00Z",
            "total_price": 12000, 
            "status": "pending", 
            "payment_status": "unpaid", 
            "created_at": "2026-02-19T11:30:00Z"
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
  "detail": "You do not have permission to get user's bookings"
}
```

#### Not Found
- **Status Code:** `404 Not Found`
```json
{
  "detail": "Booking not found"
}
```

#### Internal Server Error
- **Status Code:** `500 Internal Server Error`
```json
{
  "detail": "An error occurred while getting bookings"
}
```
