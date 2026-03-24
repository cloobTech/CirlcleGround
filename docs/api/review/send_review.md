# Send Review

## Endpoint

`POST /api/v1/reviews/`

---

## Description

This endpoint allows user to review a space and for a space host to review a user.


---


### Headers

| Name            | Required | Description                      |
|-----------------|----------|----------------------------------|
| Authorization   | Yes      | Bearer access token              |

---

## Request

The request should be made with `Content-Type: application/json` and include the following parameters:

---

### Request Body Parameters

| Parameter               | Type   | Required | Description                                  |Example/Notes          |
|--------------------|--------|----------|----------------------------------------------|-----------------------|
| `booking_id`       | string | Yes      | ID of the space                   |`"uuid4-12345"`           |
| `rating`        | float | Yes      | Rating of the space                    |`5`            |
| `comment`     | string | Yes      | Comment by user or host                  |`"Very good experience"`        |
      |

    

### Example Request Body

```json
{
    "review_id": "99412c32-502e-4056-a109-05270659fe4b",
    "comment": "Very good experience",
    "rating": 4.0
}
```

## Response

### Success Response

- **Status Code:** `201 CREATED`
- **Body:** A JSON object containing the newly created user details:

```json
{
  "staus": "success",
  "message": "Review sent successfully",
  "data": {
    "rating": 4.0,
    "comment": "Very good experience",
    "reviewer_name": "Miracle Gini",
    "reviewee_name": "Olamide Bello"
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
  "detail": "Only users with completed bookings on a space can review that space"
}
```

#### Not Found
- **Status Code:** `404 Not Found`
```json
{
  "detail": "Booking not found"
}
```


