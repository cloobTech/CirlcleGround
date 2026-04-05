# Delete Space Image

**Endpoint:** `DELETE /api/v1/spaces/{space_id}/images/{image_id}`
**Description:** This endpoint allows users to delete  one image from a space in a  request.
**Content-Type:** `application/json`


### Request Parameters

| Name        | Type   | Required | Description                                     |
| ----------- | ------ | -------- | ----------------------------------------------- |
| `image_id`  | string | Yes      | image_id of image to e deleted from a space                |


## Response

### Success Response
- **Status Code:** `200 OK`
```json
{
  "message": "Image deleted successfully",
}
```

### Error Response

#### Bad Request
- **Status Code:** `404 Bad Request`

```json
{
  "detail": "image_id cannot be empty"
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
  "detail": "You do not have permission to delete image from this space"
}
```

#### Not Found
- **Status Code:** `404 Not Found`
```json
{
  "detail": "Space not found"
}
```

#### Internal Server Error
- **Status Code:** `500 Internal Server Error`
```json
{
  "detail": "An error occurred while deleting the image"
}
```
