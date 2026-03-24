# Get Space Reviews

**Endpoint:** `GET /api/v1/reviews/{space_id}`
**Description:** This endpoint allows users to see all reviews on a particular space


**Content-Type:** `application/json`


### Request Parameters

| Name        | Type   | Required | Description                                     |
| ----------- | ------ | -------- | ----------------------------------------------- |
| `space_id` | list   | Yes      | ID of the space    |




## Response

### Success Response
- **Status Code:** `200 OK`
```json
{
    "status": "success",
    "message": "Space Reviews successfully retrieved",
    "data":{
        "reviewer_name": "Emmanuel Nwokoma",
        "reviewee_name": "Olamide Bello",
        "comment": "Very nice experience",
        "rating": 5.0
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
  "detail": "An error occurred while getting space reviews"
}
```
