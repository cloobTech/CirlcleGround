# Update Review

**Endpoint:** `PATCH /api/v1/reviews/{review_id}`
**Description:** This endpoint allows an authenticated user with an ID that matches the reviewer ID on the review to update the review and the system logs the activity for the user. The update window is only open for a specific period of time after which the user won't be able to update the review.
**Content-Type:** `application/json`


### Request Parameters

| Name          | Type   | Required | Description                                     |
|---------------| ------ | -------- | ----------------------------------------------- |
| `review_id`  | string | Yes      | review_id of the review to be updated.        |

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
    "message": "review updated successfully",
    "data": {
        "rating": 5.0,
        "comment": "Good experience and will love to book again"
    }
}
```

### Error Response

#### Bad Request
- **Status Code:** `404 Bad Request`

```json
{
  "detail": "review_id cannot be empty"
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
  "detail": "Only reviewer can update this review"
}
```

#### Not Found
- **Status Code:** `404 Not Found`
```json
{
  "detail": "Review not found"
}
```

#### Internal Server Error
- **Status Code:** `500 Internal Server Error`
```json
{
  "detail": "An error occurred while updating the Review"
}

```
