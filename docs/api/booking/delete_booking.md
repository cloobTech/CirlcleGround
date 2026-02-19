# Delete Booking

**Endpoint:** `DELETE /api/v1/bookings/{booking_id}`
**Description:** This endpoint allows users to delete a booking from a space in a  request.
**Content-Type:** `application/json`


### Request Parameters

| Name        | Type   | Required | Description                                     |
| ----------- | ------ | -------- | ----------------------------------------------- |
| `booking_id`  | string | Yes      | booking_id of the booking to be deleted.                |


## Response

### Success Response
- **Status Code:** `200 OK`
```json
{
    "status": "success",
    "message": "Booking deleted successfully",
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
  "detail": "You do not have permission to delete this booking"
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
  "detail": "An error occurred while deleting the booking"
}
```
