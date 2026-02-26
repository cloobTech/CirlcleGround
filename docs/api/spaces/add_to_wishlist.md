# Add to wishlist

## Endpoint

`POST /api/v1/spaces/{space_id}/wishlist`

---

## Description

This endpoint allows user to add a space to wishlist and makes sure that a host does not add his own space to wishlist

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



## Response

### Success Response

- **Status Code:** `201 CREATED`
- **Body:** A JSON object containing the newly added wishlist details:

```json
{
  "status": "success", 
  "message": "Space added to wishlist successfully", 
  "data": {
     "space_id": "space_12345", 
     "user_id": "user_67890"
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
- **Status Code:** `403 Forbidden`
```json
{
  "detail": "Space host can't add his own space to wishlist"
}
```

#### Not Found
- **Status Code:** `404 Not Found`
```json
{
  "detail": "Space not found"
}
```
