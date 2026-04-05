# Delete Space Reviews

**Endpoint:** `DELETE /api/v1/messages/{message_id}`
**Description:** This endpoint allows an authenticated user to delete  a message.
**Content-Type:** `application/json`


### Headers

| Name            | Required | Description                      |
|-----------------|----------|----------------------------------|
| Authorization   | Yes      | Bearer access token              |

---

### Request Parameters

| Name        | Type   | Required | Description                                     |
| ----------- | ------ | -------- | ----------------------------------------------- |
| `message_id`  | string | Yes      | message_id of the message               |


## Response

### Success Response
- **Status Code:** `200 OK`
```json
{
    "message": "message successfully deleted"
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
  "detail": "You do not have permission to delete message"
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
  "detail": "An error occurred while deleting the message"
}
```
