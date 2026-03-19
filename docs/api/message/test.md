# 📡 WebSocket Messaging API Documentation

## Overview

This module provides real-time messaging using WebSockets. It supports:

* User authentication via JWT
* Conversation-based messaging
* Retrieving message history
* Sending and receiving messages in real-time

---

## 🔌 WebSocket Endpoint

```
ws://<host>/api/v1/websocket/messages
```

### Query Parameters

| Parameter         | Type   | Required | Description                    |
| ----------------- | ------ | -------- | ------------------------------ |
| `token`           | string | ✅ Yes    | JWT access token               |
| `conversation_id` | string | ✅ Yes    | ID of the conversation to join |

### Example

```
ws://localhost:8000/api/v1/websocket/messages?token=YOUR_TOKEN&conversation_id=CONV_ID
```

---

## 🔐 Authentication

* The `token` is extracted from query params.
* It is decoded and validated.
* The user is fetched from the database.
* Connection is rejected if authentication fails.

---

## 🔄 Connection Flow

1. Client connects to WebSocket
2. Server validates token
3. User is connected via `WebSocketManager`
4. Server sends message history
5. Client can send and receive messages in real-time

---

## 📨 Incoming Messages (Client → Server)

### Send Message

```json
{
  "conversation_id": "string",
  "content": "string"
}
```

### Behavior

* Message is saved to the database
* Message is broadcast to all participants in the conversation

---

## 📤 Outgoing Messages (Server → Client)

### 1. Message History

Sent immediately after connection.

```json
{
  "type": "message_history",
  "conversation_id": "string",
  "messages": [
    {
      "id": "string",
      "sender_id": "string",
      "content": "string",
      "created_at": "ISO8601 timestamp"
    }
  ]
}
```

---

### 2. New Message

Sent when a new message is created.

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

---

## ⚠️ Error Handling

| Scenario                | Behavior                        |
| ----------------------- | ------------------------------- |
| Missing token           | Connection closed (code 1008)   |
| Invalid token           | Connection closed               |
| Missing conversation_id | Connection closed               |
| Unexpected error        | Connection closed               |
| Client disconnect       | Removed from active connections |

---

## 🧠 WebSocket Manager Responsibilities

* Track active connections per user
* Handle connect/disconnect
* Send messages to specific users
* Broadcast messages

---

## 🧱 Architecture Notes

* **MessagingService** handles business logic:

  * Sending messages
  * Fetching messages
  * Starting conversations

* **Unit of Work (UoW)** manages database transactions

* **Repositories** handle database access:

  * Conversation repository
  * Message repository
  * Participant repository

---

## 🚀 Related HTTP Endpoint

### Start Conversation

```
POST /api/v1/messages/start
```

#### Request Body

```json
{
  "recipient_id": "string"
}
```

#### Response

```json
{
  "conversation_id": "string"
}
```

---

## 🧪 Testing with Insomnia

1. Create a WebSocket request
2. Connect using:

```
ws://localhost:8000/api/v1/websocket/messages?token=YOUR_TOKEN&conversation_id=CONV_ID
```

3. Send message:

```json
{
  "conversation_id": "CONV_ID",
  "content": "Hello world"
}
```

4. Observe incoming messages in real-time

---

## 🔄 Message Lifecycle

```
Client connects → Server authenticates → Sends message history
Client sends message → Server saves → Broadcasts to participants
Clients receive new_message → UI updates
```

---

## 📌 Notes

* WebSocket is stateful — connection must remain open
* Frontend should handle reconnection logic
* Messages are delivered in real-time but should also be persisted
* History is fetched only once on connection

---

## ✅ Summary

* Use HTTP to create conversations
* Use WebSocket for real-time messaging
* Always pass `token` and `conversation_id`
* Handle messages based on their `type`

---
