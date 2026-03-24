# Delete Space Reviews

**Endpoint:** `DELETE /api/v1/reviews/{space_id}`
**Description:** This endpoint allows user to delete  reviews that belong to a particular space.
**Content-Type:** `application/json`


### Headers

| Name            | Required | Description                      |
|-----------------|----------|----------------------------------|
| Authorization   | Yes      | Bearer access token              |

---

### Request Parameters

| Name        | Type   | Required | Description                                     |
| ----------- | ------ | -------- | ----------------------------------------------- |
| `space_id`  | string | Yes      | space_id of the space               |


## Response

### Success Response
- **Status Code:** `200 OK`
```json
{
    "message": "space reviews successfully deleted"
}
```

### Error Response

#### Bad Request
- **Status Code:** `404 Bad Request`

```json
{
  "detail": "space_id cannot be empty"
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
  "detail": "You do not have permission to delete space reviews"
}
```

#### Not Found
- **Status Code:** `404 Not Found`
```json
{
  "detail": "Space reviews not found"
}
```

#### Internal Server Error
- **Status Code:** `500 Internal Server Error`
```json
{
  "detail": "An error occurred while deleting the space reviews"
}
```
