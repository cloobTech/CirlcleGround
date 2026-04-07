# Start conversation
## Enpoint `POST /api/v1/messages/start_conversation`

## Overview

This module provides real-time messaging using WebSockets. It supports:

---
**Web socket endpoint:** `/api/v1/websocket/messages`


### Query Parameters

| Parameter         | Type   | Required | Description                    |
| ----------------- | ------ | -------- | ------------------------------ |
| `recipient_id`           | string | ✅ Yes    | ID of the recipient               |


### Headers

| Name            | Required | Description                      |
|-----------------|----------|----------------------------------|
| Authorization   | Yes      | Bearer access token              |

---

```json
{
  "recipient_id": "string",
}
```


## Response

### Success Response

```json
{
  "type": "new_message",
  "conversation_id": "string",
  "id": "string",
  "sender_id": "string",
  "content": "string",
  "created_at": "ISO8601 timestamp"
}

```

### Error Resoponse

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
  "detail": "Recipient not found"
}
```
#### Internal Server Error
- **Status Code:** `500 Internal Server Error`
```json
{
  "detail": "An error occurred while starting conversation"
}
```