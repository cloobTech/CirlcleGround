# Delete User Notification

## Endpoint
`DELETE /api/v1/users/me/notifications`

---

## Description

This endpoint allows an authenticated user to **delete multiple notifications from their notification list**.

The system removes the corresponding **NotificationRecipient** record associated with the authenticated user and the specified notifications.

Deleting these notifications only removes it **for the current user**.  
Other users who received the same notifications will still have access to them.

---

## Headers

| Name          | Required | Description         |
|---------------|----------|---------------------|
| Authorization | Yes      | Bearer access token |

---

## Path Parameters

| Parameter          | Type   | Required | Description                                      |
|--------------------|--------|----------|--------------------------------------------------|
| `notification_ids` | list   | Yes      | The IDs of the different notifications to delete |

---

## Response

### Success Response
- **Status Code:** `200 OK`
```json
{
  "message": "Notifications deleted successfully"
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
  "detail": "Notifications not found"
}
```

#### Forbidden
- **Status Code:** `403 Forbidden`
```json
{
  "detail": "You do not have permission to delete user notifications"
}
```
#### Internal Server Error
- **Status Code:** `500 Internal Server Error`
```json
{
  "detail": "An error occurred while deleting user notifications"
}
```


