## Endpoint

`POST /auth/reset-password`

## Description

This endpoint validates a password reset token and updates the user’s password.

## Request

This request should be made with `Content-Type: application/json` and include the following parameters:

### Form Data Parameters


| Parameter       | Type   | Required | Description                     |Example/Note
|---------------- |--------|----------|---------------------------------|-----------------------|
| `user_id`       | string |Yes       | Registered email address        | `"johndoe@gmail.com"` |
| `new_password`  | string |Yes       | New password of the user        |`"strongPassword&65"`  |




## Response

### Success Response

-  **Status Code:** `200 OK`
- **Body:** A JSON object containing the following details:

```json
{
  "message": "Password updated successfully"
}
```

### Error


#### Validation Error
- **Status Code:** `422 Unprocessable Entity`

```json
{
  "detail": "Invalid input data"
}
```
