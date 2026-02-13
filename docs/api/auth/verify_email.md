## Endpoint

`POST /auth/register`

---

## Description

This endpoint handles email verification

---

## Request

The request should be made with `Content-Type: application/json` and include the following parameters:


### Request Body Parameters

| Parameter               | Type   | Required | Description                             |Example/Notes          |
|-------------------------|--------|----------|-----------------------------------------|-----------------------|
|`token`                  |string  |Yes       |Token that was sent to user via email    |`"random token"`             |

### Example Request Body

```json
{
    "token": "random token"
}
```

## Response
### Success Response
- **Status Code:** `200 OK`
```json
{
    "message": "Email successfully verified"
}
```

### Error Response

#### Invalid token
- **Status Code**: `400 Bad Request`
```json
{
  "detail": "Invalid verification token"
}
```