# Search Location

## Enpoint

`GET /api/v1/locations/search`

## Description

The Search Location endpoint allows you to search for geographical locations and addresses using the Nominatim geocoding service. This endpoint converts address strings into geographic coordinates and detailed location information.

## Request

This request should be made with `Content-Type: application/json` header and include the following parameters:

### Form Data Parameters

| Name      | Type   | Required | Description                       |
| --------- | ------ | -------- | --------------------------------- |
| `search_sting` | string | Yes      | User-provided address or location to search for |

## Response

### Success Response

- **Status Code:** `200 OK`
- **Body:** A JSON object containing the following details:

```json
{
  "lat": 0.01,
  "lng": 0.002,
  "place_name": "Amakohia ",
  "address": {
    "country": "string",
    "state": "string",
    "city": "string"
  }
}
```

### Error Response

#### Location not found

- **Status Code:** `404 Not Found`

```json
{
  "detail": "Location not found for the provided address"
}
```

#### Invalid address format

- **Status Code:** `422 Unprocessable Entity`

```json
{
  "detail": ""
}
```

#### Internal Server Error

- **Status Code:** `500 Internal Server Error`

```json
{
  "detail": "An error occurred while processing your request"
}
```
