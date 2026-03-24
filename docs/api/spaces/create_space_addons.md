# Creating Booking

## Endpoint

`POST /api/v1/spaces/{space_id}/addons`

---

## Description

This endpoint allows user to create space addons.

---

## Request

The request should be made with `Content-Type: application/json` and include the following parameters:

---

### Request Body Parameters

| Parameter               | Type   | Required | Description                                  |Example/Notes          |
|--------------------|--------|----------|----------------------------------------------|-----------------------|
| `space_id`       | string | Yes      | ID of the space                   |`"uuid4-12345"`           |




### Example Request Body

```json
{
    "space_id": "uuid4-12345",
    "name": "",
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
  "message": "Space addons created successfully",
  "data": {
    "space_id": "uuid4-123456",
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
    ]
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



#### Not Found
- **Status Code:** `404 Not Found`
```json
{
  "detail": "Space not found"
}
```


