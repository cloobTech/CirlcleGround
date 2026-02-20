# Delete Space Amenities

**Endpoint:** `DELETE /api/v1/space_amenities/{space_amenity_id}`
**Description:** This endpoint allows users to delete  multiple space amenities from the database in a  request.
**Content-Type:** `application/json`


### Request Parameters

| Name        | Type   | Required | Description                                     |
| ----------- | ------ | -------- | ----------------------------------------------- |
| `space_amenity_id`  | list | Yes      | space_amenity_id of the different amenities               |


## Response

### Success Response
- **Status Code:** `200 OK`
```json
{
    "message": "space amenities successfully deleted",
    "total_rows_deleted": "deleted_space_amenities"
}
```

### Error Response

#### Bad Request
- **Status Code:** `404 Bad Request`

```json
{
  "detail": "space_amenity_id cannot be empty"
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
  "detail": "You do not have permission to delete space amenities"
}
```

#### Not Found
- **Status Code:** `404 Not Found`
```json
{
  "detail": "Space Amenity not found"
}
```

#### Internal Server Error
- **Status Code:** `500 Internal Server Error`
```json
{
  "detail": "An error occurred while deleting the space amenities"
}
```
