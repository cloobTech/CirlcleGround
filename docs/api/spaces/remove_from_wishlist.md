# Remove from wishlist

## Endpoint

`DELETE /api/v1/spaces/{space_id}/wishlist`

---

## Description

This endpoint allows user to remove a space from wishlist

---

## Request

The request should be made with `Content-Type: application/json` and include the following parameters:

---

### Request Body Parameters

| Parameter          | Type   | Required |                             |Example/Notes          |
|--------------------|--------|----------|-----------------------------|-----------------------|
| `space_id`         | string | Yes      | ID of the space             |`"uuid4-12345"`        |

### Headers

| Name            | Required | Description                      |
|-----------------|----------|----------------------------------|
| Authorization   | Yes      | Bearer access token              |






### Example Request Body

```json
{
    "space_id": "uuid4-12345",
    "start_time": "2026-03-16T14:00:00Z",
    "end_time": "2026-04-16T14:00:00Z",
    "currency": "NGN",
    "addon_ids": [
    "uuid4-23455",
    "uuid4-56789"
    ]
}
```
## Response

### Success Response

- **Status Code:** `201 CREATED`
- **Body:** A JSON object containing the newly added wishlist details:

```json
{
  "status": "success", 
  "message": "Space removed from wishlist successfully", 
  "data": {
     "wishlist_id": "wishlist_12345"
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

#### Not Found
- **Status Code:** `404 Not Found`
```json
{
  "detail": "Space not found"
}
```
