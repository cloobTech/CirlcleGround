# Delete Review

**Endpoint:** `DELETE /api/v1/reviews/{review_id}`
**Description:** This endpoint allows user to delete  a review from a space and logs the activity for the user.
**Content-Type:** `application/json`




### Request Parameters

| Name        | Type   | Required | Description                                     |
| ----------- | ------ | -------- | ----------------------------------------------- |
| `review_id`  | string | Yes      | review_id of the review to be deleted               |


## Response

### Success Response
- **Status Code:** `200 OK`
```json
{
    "message": "review successfully deleted"
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
  "detail": "You do not have permission to delete review"
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
  "detail": "An error occurred while deleting the review"
}
```
