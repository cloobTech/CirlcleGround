# Update User Notification
## Endpoint
1`POST /api/v1/notification_recipient/{notification_id}/update-notification`

## Description

This endpoint allows the backend to update a notification whenever the user views it.

### Headers

| Name            | Required | Description                      |
|-----------------|----------|----------------------------------|
| Authorization   | Yes      | Bearer access token              |


## Request
This should be made with `Content-Type: application/json` and include the following parameters:


| Parameter               | Type   | Required | Description                             |Example/Notes          |
|-------------------------|--------|----------|-----------------------------------------|-----------------------|
|`notification_id`        |string  |Yes       |ID of the notification                  |`"uuid-1234"`            |



## Response

### Success Response
- **Status Code:** `200 OK`
```json
{
    "status": "success",
    "message": "Notification successfully updated",
    "data": {
        "recipient_id": "uuid-1234",
        "notification_id": "uuid-1234",
        "is_read": true,
        "read_at": "2026-03-07T14:21:00Z"
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
- **Status Code:** `404 Not Found`
```json
{
  "detail": "Notification not found"
}
```

#### Forbidden
- **Status Code:** `403 Forbidden`
```json
{
  "detail": "You do not have permission to update user notification"
}
```
#### Internal Server Error
- **Status Code:** `500 Internal Server Error`
```json
{
  "detail": "An error occurred while updating user notification"
}
```

