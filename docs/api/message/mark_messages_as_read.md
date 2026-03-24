# Mark Message As Read

## Enpoint `POST /api/v1/messages/read`

## Description
This endpoint allows user's message to be marked as read when the message has been read by the recipient

It extracts the conversation_id from the dict sent and marks the conversation as read.


## Request Body Parameters

| Parameter               | Type   | Required | Description                                  |Example/Notes          |
|--------------------|--------|----------|----------------------------------------------|-----------------------|
| `conversation_id`       | string | Yes      | ID of the conversation to be marked                   |`"uuid4-12345"`           |


## Example Request Body

```json
{
    "conversation_id": "uuid4-12345"
}
```

## Response
### Success Response

```json
{
    "message": "Messages marked as read"
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

#### Not Found
- **Status Code:** `404 Not Found`
```json
{
  "detail": "Conversation not found"
}
```
