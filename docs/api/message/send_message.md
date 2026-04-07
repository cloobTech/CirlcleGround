# WebSocket Messaging 

**Endpoint:** `/api/v1/websocket/messages`

## Description

This WebSocket endpoint enables **real-time messaging** between users within a conversation.  
It supports:

- Authentication via token
- Fetching recent message history
- Sending messages in real-time
- Managing active WebSocket connections

---





---

## Query Parameters

| Parameter         | Type   | Required | Description                          |
|------------------|--------|----------|--------------------------------------|
| token            | string | Yes      | Authentication token                 |
| conversation_id  | string | Yes      | ID of the conversation to join       |

---

## Connection Flow

### 1. Client connects

- WebSocket connection is accepted
- Query parameters are extracted:
  - `token`
  - `conversation_id`

---

### 2. Validation

- If `token` is missing → connection closed (`1008`)
- If `conversation_id` is missing → connection closed (`1008`)

---

### 3. Authentication

- A database session is created
- `UnitOfWork` is initialized
- `get_current_user()` is called manually using:
  - `token`
  - `uow`

---

### 4. Connection Registration

- User is registered with the WebSocket manager

### 5. Load Message History
- Loads the last 50 messages

### 6. Sends Initial Data
```json
{
  "type": "message_history",
  "conversation_id": "uuid1234",
  "messages": [
    {
      "id": "uuid2345",
      "sender_id": "uuid3456",
      "content": "Hello world",
      "created_at": "datetime",
      "is_edited": false
    }
  ]
}
```

### 7. Real time messaging loop
- Server listens continuosly
- Expected client payload:
```json
{
    "content": "Hello world"
}
```

## Disconnection Handling
### Unexpected errors:
-This leads to a clean up of active connections to prevent stale websocket references.