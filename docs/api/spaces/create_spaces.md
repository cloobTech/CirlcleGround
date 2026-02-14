# Create a Space

**Endpoint:** `POST /spaces`  
**Description:** Create a new space with basic initial data
**Content-Type:** `application/json`

### Request Parameters

| Parameter                     | Type             | Required | Description                     | Example / Notes                                                       |
| ----------------------------- | ---------------- | -------- | ------------------------------- | --------------------------------------------------------------------- |
| `space.id`                    | string           | ✅       | Unique ID of the space          | `"space-uuid-1234"`                                                   |
| `space.location_id`           | string           | ✅       | ID of the location              | `"location-uuid-5678"`                                                |
| `space.name`                  | string           | ✅       | Name of the space               | `"Cozy Studio Apartment"`                                             |
| `space.description`           | string           | ✅       | Description of the space        | `"A modern studio apartment in the heart of the city."`               |
| `space.price`                 | float            | ✅       | Base price of the space         | `5000`                                                                |
| `space.max_guests`            | int              | ✅       | Maximum number of guests        | `"3"`                                                                 |
| `space.space_type`            | enum (lowercase) | ❌       | Type of space                   | `"apartment"`, `"house"`, `"others"` (default `"others"`)             |
| `space.category`              | enum (lowercase) | ❌       | Category of space               | `"residential"`, `"commercial"`, `"others"` (default `"others"`)      |
| `space.is_verified`           | boolean          | ❌       | Whether the space is verified   | `false` (default)                                                     |
| `space.square_feet`           | int              | ✅       | Total area in square feet       | `400`                                                                 |
| `space.length`                | int              | ✅       | Length of the space             | `20`                                                                  |
| `space.width`                 | int              | ✅       | Width of the space              | `20`                                                                  |
| `space.num_of_bathrooms`      | int              | ❌       | Number of bathrooms             | `1` (default `0`)                                                     |
| `space.num_of_toilets`        | int              | ❌       | Number of toilets               | `1` (default `0`)                                                     |
| `space.num_of_parking_spaces` | int              | ❌       | Number of parking spots         | `1` (default `0`)                                                     |

**Request Body:**

```json
{
  "space": {
    "id": "space-uuid-1234",
    "location_id": "location-uuid-5678",
    "name": "Cozy Studio Apartment",
    "description": "A modern studio apartment in the heart of the city.",
    "price": 5000,
    "max_guests": 3,
    "space_type": "others",
    "category": "others",
    "is_verified": false,
    "square_feet": 400,
    "length": 20,
    "width": 20,
    "num_of_bathrooms": 1,
    "num_of_toilets": 1,
    "num_of_parking_spaces": 1
  },
  
}
```
