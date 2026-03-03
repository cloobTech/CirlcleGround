# Search Space

**Endpoint:** `GET /api/v1/spaces`
**Description:** It provides a search implementation for the space model. It smartly detects the database engine in use and applies either PostgreSQL full-text search (after converting user input into Postgres seach format) or SQLite fallback using case-insensitive pattern matching. It converts the user input to 

**Content-Type:** `application/json`

### Request Parameters

| Name        | Type   | Required | Description                                     |
| ----------- | ------ | -------- | ----------------------------------------------- |
| `search_string` | String   | Yes      | The user-provided search input    |
| `limit` | String   | Yes      | Maximum amount of results to return. Default is 10    |

## Response
### Success Response
- **Status Code:** `200 OK`
```json
{
  "success": true,
  "message": "Spaces retrieved successfully",
  "data": [
    {
      "id": "a12d9f44-7c31-4a11-9bde-45f789c01234",
      "name": "Creative Hub Downtown",
      "description": "A vibrant creative workspace designed for designers, developers, and startups.",
      "space_type": "coworking",
      "category": "creative",
      "price_per_hour": 30.0,
      "location": "San Francisco",
      "is_available": true,
      "created_at": "2026-03-02T14:10:45Z"
    },
    {
      "id": "f88c3b21-2e99-4d55-b7a1-78a123456def",
      "name": "The Creative Hub Studio",
      "description": "A flexible studio hub perfect for photography, podcasting, and content production.",
      "space_type": "studio",
      "category": "media",
      "price_per_hour": 45.0,
      "location": "Austin",
      "is_available": true,
      "created_at": "2026-02-27T09:30:00Z"
    }
  ]
}
```

### Eror Response

#### Bad Request
- **Status Code:** `404 Bad Request`

```json
{
  "detail": "Invalid  request parameters"
}
```

#### No Results Found
- **Status Code:** `200 OK`
```json
{
    "details": "No results found"
}
```

#### Invalid Limit  Value
- **Status Code:** `422 Unprocessable Entity`
```json
{
  "detail": "Unprocessable Entity"
}
```

#### Internal Server Error
- **Status Code:** `500 Internal Server Error`
```json
{
  "detail": "An error occurred while getting spaces"
}
```