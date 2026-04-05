# Register Guest User

## Endpoint

`POST /api/v1/auth/`

---

## Description

This endpoint handles user registration using the local authentication strategy.
It validates user input, ensures password confirmation matches, creates a new
user account,persists the user data in the database and logs the activity for that user.

---

## Request

The request should be made with `Content-Type: application/json` and include the following parameters:

---

### Request Body Parameters

| Parameter               | Type   | Required | Description                                  |Example/Notes          |
|--------------------|--------|----------|----------------------------------------------|-----------------------|
| `first_name`       | string | Yes      | The first name of the user                   |`"Emmanuel"`           |
| `last_name`        | string | Yes      | The last name of the user                    |`"Nwokoma"`            |
| `phone_number`     | string | Yes      | The phone number of the user                 |`"09098765443"`        |
| `password`         | string | Yes      | The password of the user                     |`"strongpassword6%43"` |
| `location`         | string | No       | The user’s location (derived from lat & lon) |
| `latitude`         | float  | No       | The user’s location latitude                 |
| `longitude`        | float  | No       | The user’s location longitude                |



### Example Request Body

```json
{
  "status": "success",
  "message": "Guest user registered successfully"
  "first_name": "John",
  "last_name": "Doe",
  "phone_number": "+2348012345678",
  "password": "strongpassword",
  "location": "Lagos, Nigeria",
  "latitude": 0.724363,
  "longitude": 3.758866,
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
  "is_active": true
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