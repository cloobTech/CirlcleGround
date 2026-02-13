
## Reset Password

## Endpoint
`POST /auth/reset-password`

---

### Description
This endpoint allows user to change password after token must have been verified

---

## Request

**Content-Type:** `application/json`

## Form Data Parameters

| Parameter      | Type   | Required | Description                     |Example/Notes             |
|------------|--------|----------|---------------------------------|--------------------------|
| `emal`     | string | Yes      |Registered email of the user     |`"johndoe@gmail.com"`     |


---


##  Response

### Success Response

-**Status Code:** `200 OK`
- **Body:** A JSON object containing the following keys:

```json
{
  "message": "Password reset token sent successfully"
}
```

### Error Resonse
#### Invalid email format

```json
{
  "detail": "Invalid email format"
}
```


