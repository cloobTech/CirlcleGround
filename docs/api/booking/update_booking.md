# Update Booking

**Endpoint:** `PATCH /api/v1/bookings/{booking_id}`
**Description:** This endpoint allows an authenticateed user to update a booking they created and log the activity for the guest user.
**Content-Type:** `application/json`


### Request Parameters

| Name          | Type   | Required | Description                                     |
|---------------| ------ | -------- | ----------------------------------------------- |
| `booking_id`  | string | Yes      | booking_id of the booking to be updated.        |

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
    "message": "booking updated successfully",
    "start_time": "2026-02-21T14:00:00Z",
    "end_time": "2026-02-21T16:00:00Z",
    "addon_ids": [
        "addon_01",
        "addon_03"
    ]
}
```

### Error Response

#### Bad Request
- **Status Code:** `404 Bad Request`

```json
{
  "detail": "booking_id cannot be empty"
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
  "detail": "Only guest can update this booking"
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
  "detail": "An error occurred while updating the booking"
}

```

#### Conflict error
- **Status Code:** `509 conflict`
```json
{
  "detail": "Only Pending bookings can be updated"
}
```