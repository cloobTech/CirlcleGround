# Delete Multiple Spaces Images

**Endpoint:** `DELETE /api/v1/spaces/{space_id}/images`
**Description:** This endpoint allows users to delete more than one image from a space in a single request. This is useful for bulk operations and cleaning up unwanted images.
**Content-Type:** `application/json`


### Request Parameters

| Name        | Type   | Required | Description                                     |
| ----------- | ------ | -------- | ----------------------------------------------- |
| `image_ids` | list   | Yes      | list of the image_id of the different images to be deleted from a space    |


## Response

### Success Response
- **Status Code:** `200 OK`
```json
{
  "message": "Images deleted successfully",
}
```

### Error Response

#### Bad Request
- **Status Code:** `404 Bad Request`

```json
{
  "detail": "image_ids cannot be empty"
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
  "detail": "You do not have permission to delete images from this space"
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
  "detail": "An error occurred while deleting the images"
}
```
