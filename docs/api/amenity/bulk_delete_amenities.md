# Bulk Delete Amenities

**Endpoint:** `DELETE /api/v1/amenities/`
**Description:** This endpoint allows users to delete  multiple amenities from the database in a  request.
**Content-Type:** `application/json`


### Request Parameters

| Name        | Type   | Required | Description                                     |
| ----------- | ------ | -------- | ----------------------------------------------- |
| `amenities_id`  | list | Yes      | amenity_id of the different amenities                |


## Response

### Success Response
- **Status Code:** `200 OK`
```json
{
  "message": "Amenities deleted successfully",
  "total_rows_deleted": "total rows of deleted amenities"
}
```

### Error Response

#### Bad Request
- **Status Code:** `404 Bad Request`

```json
{
  "detail": "amenity_id cannot be empty"
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
  "detail": "You do not have permission to delete amenities"
}
```

#### Not Found
- **Status Code:** `404 Not Found`
```json
{
  "detail": "Amenities not found"
}
```

#### Internal Server Error
- **Status Code:** `500 Internal Server Error`
```json
{
  "detail": "An error occurred while deleting amenities"
}
```
