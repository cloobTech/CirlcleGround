# Get Space Bookings

**Endpoint:** `GET /api/v1/spaces/{space_id}/bookings`
**Description:** This endpoint allows admin and super admin to get all bookings for a particular space

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
    "guest_id": "uuid4-12345",
    "space_id": "uuid4-12345",
    "status": "pending",
    "start_time": "2026-03-16T14:00:00Z",
    "end_time": "2026-03-16T16:30:00Z",
    "cancelled_time": "",
    "currency": "NGN",
    "total_price": 5000,
    "payment_status":"paid"
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
  "detail": "You do not have permission to get space bookings"
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
  "detail": "An error occurred while getting space bookings"
}
```
