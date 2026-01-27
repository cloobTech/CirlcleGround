
## Request Password Reset Token

## Endpoint
`POST /auth/request-password-token`

---

### Description
This endpoint initiates the password recovery flow.  
A reset token is generated and sent to the user’s registered email or phone number.

---

## Request

**Content-Type:** `application/json`

## Form Data Parameters

| Name  | Type   | Required | Description                     |
|-------|--------|----------|---------------------------------|
| email | string | Yes      | Registered email address        |

---

## Example Request

```json
{
  "email": "user@example.com"
}
```

##  Response

### Success Response

-**Status Code:** `200 OK`
- **Body:** A JSON object containing the following keys:

```json
{
  "message": "Password reset token sent successfully"
}
```

### Error Response

#### User Not Found

- **Status Code:** `404 Not Found`

```json
{
  "detail": "User not found"
}
```

#### Validation Error

- **Status Code:** `422 Unprocessable Entity`

```json
{
  "detail": "Invalid email format"
}
```

