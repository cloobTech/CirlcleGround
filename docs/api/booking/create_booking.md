# Creating Booking

## Endpoint

`POST /api/v1/bookings/`

---

## Description

This endpoint allows user to create a booking for a space within a specified time range.
The system will automatically calculate the total price based on the space pricing

---

## Request

The request should be made with `Content-Type: application/json` and include the following parameters:

---

### Request Body Parameters

| Parameter               | Type   | Required | Description                                  |Example/Notes          |
|--------------------|--------|----------|----------------------------------------------|-----------------------|
| `space_id`       | string | Yes      | ID of the space                   |`"uuid4-12345"`           |
| `start_time`        | string | Yes      | Booking start time                    |`"2026-03-16T14:00:00Z"`            |
| `end_time`     | string | Yes      | Booking end time                  |`"2026-04-16T14:00:00Z"`        |
      |
| `addon_ids` | array[string] | Yes | List of IDs of different addons | `["uuid4-2345", "uuid4-56789"]` |





### Example Request Body

```json
{
    "space_id": "uuid4-12345",
    "start_time": "2026-03-16T14:00:00Z",
    "end_time": "2026-04-16T14:00:00Z",
    "currency": "NGN",
    "addon_ids": [
    "uuid4-23455",
    "uuid4-56789"
    ]
}
```
## Response

### Success Response

- **Status Code:** `201 CREATED`
- **Body:** A JSON object containing the newly created user details:

```json
{
  "staus": "success",
  "message": "Booking created successfully",
  "data": {
    "booking_id": "uuid4-123456",
    "user_id": "uuid4-45678",
    "addons": [
      {
        "id": "uuid4-23455",
        "name": "Extra Cleaning",
        "price": 5000,
        "currency": "NGN"
      },
      {
        "id": "uuid4-56789",
        "name": "Express Service",
        "price": 3000,
        "currency": "NGN"
      }
    ],
    "total_price": 18000,
    "status": "pending",
    "booking_date": "2026-02-20",
    "created_at": "2026-02-19T11:30:00Z"
  }
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
  "detail": "Only guest users can create bookings"
}
```

#### Not Found
- **Status Code:** `404 Not Found`
```json
{
  "detail": "Space not found"
}
```

#### Conflict error
- **Status Code:** `509 conflict`
```json
{
  "detail": "The selected time slot is not available"
}
```
