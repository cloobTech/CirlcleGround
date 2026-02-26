# Get User Profile

## Endpoint
`GET /api/v1/user/me`

---

## Description
This endpoint returns the wishlist of the currently authenticated based on the provided bearer access token.



## Authentication
This endpoint requires **OAuth2 Bearer Token authentication**.

Include the access token in the request header:

---

## Request Parameters

### Headers

| Name            | Required | Description                      |
|-----------------|----------|----------------------------------|
| Authorization   | Yes      | Bearer access token              |

---

## Response

### Success Response

- **Status Code:** `200 OK`
- **Body:** A JSON object containing the following details:

```json
{
  "status": "success",
  "message": "User's wishlist retrieved successfully",
  "data": [
        {
            "id": "wishlist_001", 
            "space": {
                "id": "space_123", 
                "name": "Conference Room A", 
                "status": "ACTIVE"
            } 
        },
        {
            "id": "wishlist_002", 
            "space": {
                "id": "space_456", 
                "name": "Private Office B", 
                "status": "INACTIVE" 
            }
        }
  ]
}
```
### Error Response
#### Unauthorized

- **Status Code:** `401 Unauthorized`
```json
{
  "detail": "Could not validate token"
}
```

#### Token Expired or Invalid

- **Status Code:** `401 Unauthorized`

```json
{
  "detail": "Invalid or expired token"
}
```

