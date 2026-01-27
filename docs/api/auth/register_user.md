## Endpoint

`POST /auth/register`

---

## Description

This endpoint handles user registration using the local authentication strategy.
It validates user input, ensures password confirmation matches, creates a new
user account, and persists the user data in the database.

---

## Request

The request should be made with `Content-Type: application/json` and include the following parameters:

---

### Request Body Parameters

| Name               | Type   | Required | Description                                  |
|--------------------|--------|----------|----------------------------------------------|
| `name`             | string | Yes      | The full name of the user                    |
| `phone_number`     | string | Yes      | The phone number of the user                 |
| `password`         | string | Yes      | The password of the user                     |
| `confirm_password` | string | Yes      | Must match the `password` field              |
| `location`         | string | Yes      | The user’s location                          |



### Example Request Body

```json
{
  "name": "John Doe",
  "phone_number": "+2348012345678",
  "password": "strongpassword",
  "confirm_password": "strongpassword",
  "location": "Lagos, Nigeria"
}
```
## Response

### Success Response

- **Status Code:** `201 CREATED`
- **Body:** A JSON object containing the newly created user details:

```json
{
  "id": "string",
  "name": "string",
  "phone_number": "string",
  "location": "string",
  "is_active": true,
  "created_at": "datetime"
}
```

### Error Response

#### Password Mismatch
- **Status Code**: `400 Bad Request`

```json
{
  "detail": "Passwords do not match"
}
```

#### User Already Exists Error
- **Status Code**: `409 Conflict`

```json
{
  "detail": "User already exists"
}
```

#### Validation Error
- **Status Code**: `422 Unprocessed Entity`
```json
{
  "detail": "Invalid input data"
}
```
#### Internal Server Error
- **Status Code**: `500 Internal Server Error`
```json
{
  "detail": "An unexpected error occured"
}
```