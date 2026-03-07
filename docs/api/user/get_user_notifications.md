# Get User Notifications

**Endpoint:** `GET /api/v1/users/me/notifications`
**Description:** This endpoint allows users to get all their notifications

**Content_Type:** `application/json`

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
    "message": "User notifications successfully retrieved",
    "notifications": [
        {
            "notification_id": "uuid-1234",
            "message": "A new space 'Executive Hotels2' has been created by host user_12345.",
            "is_read": false,
            "created_at": "2026-03-07T12:20:00Z"
            },
        {
            "notification_id": "uuid-4567",
            "message": "A new space 'Executive Hotels2' has been created by host user_12345.",
            "is_read": true,
            "created_at": "2026-03-06T09:15:00Z"
        }
    ]
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
  "detail": "You do not have permission to get user's notifications"
}
```
#### Internal Server Error
- **Status Code:** `500 Internal Server Error`
```json
{
  "detail": "An error occurred while getting notifications"
}
```