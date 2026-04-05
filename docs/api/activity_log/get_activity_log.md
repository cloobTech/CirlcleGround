# Get User Activity Log

**Endpoint:** `GET /api/v1/activity_logs/me/activity_log`
**Description:** This endpoint allows users to get their activity log.


**Content-Type:** `application/json`


### Headers

| Name            | Required | Description                      |
|-----------------|----------|----------------------------------|
| Authorization   | Yes      | Bearer access token              |




## Response

### Success Response
- **Status Code:** `200 OK`
```json
{
    "status": "success",
    "message": "Space Reviews successfully retrieved",
    "data":{
        "activity": "user_login",
        "user_id": "user_12345",
        "resource_id": "user_12345",
        "created_at": "2026-04-03T22:32:44.492003",
        "id": "a6121246-6827-4dba-88f1-69ec48fd63b3",
        "resource_type": "user",
        "updated_at": "2026-04-03T22:32:44.492003"
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
  "detail": "Activity log not found"
}
```

#### Internal Server Error
- **Status Code:** `500 Internal Server Error`
```json
{
  "detail": "An error occurred while getting activity log"
}
```
