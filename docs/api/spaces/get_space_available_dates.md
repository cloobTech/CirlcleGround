# Get Space Available Dates

**Endpoint:** `GET /api/v1/spaces/{space_id}/available-dates`
**Description:** This endpoint allows users to get available dates for a particular space

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
  "success": true,
  "message": "Available dates retrieved successfully",
  "data": {
    "space_id": "a12d9f44-7c31-4a11-9bde-45f789c01234",
    "available_dates": [
      {
        "date": "2026-03-05",
        "available_slots": [
          {
            "start_time": "09:00",
            "end_time": "11:00"
          },
          {
            "start_time": "14:00",
            "end_time": "18:00"
          }
        ]
      },
      {
        "date": "2026-03-06",
        "available_slots": [
          {
            "start_time": "10:00",
            "end_time": "16:00"
          }
        ]
      }
    ]
  }
}
```

### Error Response


#### Unauthorized

- **Status Code:** `401 Unauthorized`
```json
{
  "detail": "Could not validate credentials"
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
  "detail": "An error occurred while getting available dates for space"
}
```
