# Delete User Notification

## Endpoint
`DELETE /api/v1/notification_recipient/{notification_id}`

---

## Description

This endpoint allows an authenticated user to **delete a notification from their notification list**.

The system removes the corresponding **NotificationRecipient** record associated with the authenticated user and the specified notification.

Deleting a notification only removes it **for the current user**.  
Other users who received the same notification will still have access to it.

---

## Headers

| Name          | Required | Description         |
|---------------|----------|---------------------|
| Authorization | Yes      | Bearer access token |

---

## Path Parameters

| Parameter         | Type   | Required | Description                                | Example |
|-------------------|--------|----------|--------------------------------------------|--------|
| `notification_id` | string | Yes | The ID of the notification to delete | `"uuid-1234"` |

---

## Response

### Success Response
- **Status Code:** `200 OK`
```json
{
  "message": "Notification deleted successfully"
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
  "detail": "You do not have permission to delete user notification"
}
```
#### Internal Server Error
- **Status Code:** `500 Internal Server Error`
```json
{
  "detail": "An error occurred while deleting user notification"
}
```


