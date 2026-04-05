# Upload Space Images

**Endpoint:** `POST /api/v1/spaces/{space_id}/images`
**Description:** The Upload Space Images endpoint allows users to upload multiple images for a specific space. Images are processed asynchronously in the background, allowing for quick response times even with large files.
**Content-Type:** `multipart/form-data`

#### Request Parameters

| Parameter | Type   | Required | Description                       |
|-----------|--------|----------|-----------------------------------|
| `files`   | file[] | Yes      | One or more image files to upload |

## Response

### Success Response

**200 OK**
```json
{
  "message": "Images upload started",
  "img_ids": ["string"]
}
```

### Error Response

#### Bad Request
- **Status Code:** `400 Bad Request`

```json
{
  "detail": "No files provided"
}
```

#### Forbidden
- **Status Code:** `403 Forbidden`

```json
{
    "detail": "You do not have permission to upload images for this space"
}
```


#### Space Not Found
- **Status Code:** `404 Not Found`

```json
{
    "detail": "Space not found"
}
```

#### Unsupported file format
- **Status Code:** `415 unsupported file format`
```json
{
  "detail": "Unsupported file type. Allowed types: JPEG, JPG, PNG, WEBP, GIF"
}
```

#### Insufficient Storage
- **Status Code:** `507 insufficient storage`
```json
{
  "detail": "Storage quota exceeded for this space"
}
```
