# Update Review

**Endpoint:** `PATCH /api/v1/messages/{message_id}`
**Description:** This endpoint allows an authenticated user to update a message the same user has sent
**Content-Type:** `application/json`


### Request Parameters

| Name          | Type   | Required | Description                                     |
|---------------| ------ | -------- | ----------------------------------------------- |
| `message_id`  | string | Yes      | message_id of the message to be updated.        |

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
    "message": "message updated successfully",
    "data": {
        "content": "Good afternoon"
    }
}
```

### Error Response

#### Bad Request
- **Status Code:** `404 Bad Request`

```json
{
  "detail": "message_id cannot be empty"
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
  "detail": "Only message sender can update this message"
}
```

#### Not Found
- **Status Code:** `404 Not Found`
```json
{
  "detail": "Message not found"
}
```

#### Internal Server Error
- **Status Code:** `500 Internal Server Error`
```json
{
  "detail": "An error occurred while updating the message"
}

```

