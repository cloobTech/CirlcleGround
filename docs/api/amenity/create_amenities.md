# Create Amenities

## Endpoint

`POST /api/v1/amenity/`

---

## Description

This endpoint allows admin and super admin users to add one or multiple amenities to the system. Each amenity must have a name and can optionally belong to a predefined category. Duplicate amenities (by name) are ignored.

---

## Request

The request should be made with `Content-Type: application/json` and include the following parameters:

---

### Request Body Parameters

| Parameter          | Type   | Required | Description                                  |
|--------------------|--------|----------|----------------------------------------------|
| `amenities`        | array  | Yes      | list of amenities to create                  |
| `name`             | string | Yes      | Name of the amenity                          |
| `category`         | string | Yes      | Category of the amenity                      |




### Example Request Body


## Response

### Success Response

- **Status Code:** `201 CREATED`
- **Body:** A JSON object containing the newly created user details:

```json
{
    "status": "success",
    "message": "Guest user registered successfully",
    "amenities": [
        {
            "name": "WiFi", 
            "category": "connectivity" 
        },
        {
            "name": "Projector", 
            "category": "facilities"
        } 
    ]
}
```


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

#### Forbidden
- **Status Code:** `403 Forbidden`
```json
{
  "detail": "Only admin or super admin can create bookings"
}
```



