# Create a Space

**Endpoint:** `POST /spaces`  
**Description:** Create a new space with all related data (pricings, addons, use cases, rules, amenities).  
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
| `space.status`                | enum (lowercase) | ❌       | Status of space                 | `"draft"`, `"pending"`, `"available"`, `"published"`, `"rejected` (default `"draft"`) |
| `space.is_verified`           | boolean          | ❌       | Whether the space is verified   | `false` (default)                                                     |
| `space.square_feet`           | int              | ✅       | Total area in square feet       | `400`                                                                 |
| `space.length`                | int              | ✅       | Length of the space             | `20`                                                                  |
| `space.width`                 | int              | ✅       | Width of the space              | `20`                                                                  |
| `space.num_of_bathrooms`      | int              | ❌       | Number of bathrooms             | `1` (default `0`)                                                     |
| `space.num_of_toilets`        | int              | ❌       | Number of toilets               | `1` (default `0`)                                                     |
| `space.num_of_parking_spaces` | int              | ❌       | Number of parking spots         | `1` (default `0`)                                                     |
| `pricings`                    | list of objects  | ✅       | List of pricing rules           | See `SpacePricingSchema` below                                        |
| `pricings.price_type`         | enum (lowercase) | ✅       | Type of pricing                 | `"hourly"`, `"daily"`, `"weekly"`, `"monthly"`                        |
| `pricings.price`              | float            | ✅       | Price for this period           | `500`                                                                 |
| `pricings.currency`           | string           | ❌       | Currency code                   | `"NGN"` (default)                                                     |
| `pricings.start_date`         | datetime         | ✅       | Start of pricing period         | `"2026-02-12T09:00:00Z"`                                              |
| `pricings.end_date`           | datetime         | ✅       | End of pricing period           | `"2026-02-12T17:00:00Z"`                                              |
| `addons`                      | list of objects  | ❌       | Extra services for the space    | See `SpaceAddonSchema`                                                |
| `addons.name`                 | string           | ✅       | Name of addon                   | `"Breakfast"`                                                         |
| `addons.description`          | string           | ❌       | Description of addon            | `"Continental breakfast included"`                                    |
| `addons.price`                | float            | ✅       | Price for the addon             | `1000`                                                                |
| `addons.currency`             | string           | ❌       | Currency code                   | `"NGN"` (default)                                                     |
| `use_cases`                   | list of objects  | ❌       | defined use cases               | See `SpaceUseCaseSchema`                                              |
| `use_cases.name`              | string           | ✅       | Name of use case                | `"Business Trip"`                                                     |
| `use_cases.description`       | string           | ❌       | Description of use case         | `"Perfect for short business trips"`                                  |
| `rules`                       | list of objects  | ❌       | Rules for the space             | See `SpaceRuleSchema`                                                 |
| `rules.title`                 | string           | ✅       | Title of the rule               | `"No Smoking"`                                                        |
| `rules.description`           | string           | ❌       | Rule description                | `"Smoking is strictly prohibited inside the space."`                  |
| `custom_amenities`            | list of objects  | ❌       | Custom amenities added by owner | See `SpaceCustomAmenitySchema`                                        |
| `custom_amenities.name`       | string           | ✅       | Name of custom amenity          | `"Smart TV with Netflix"`                                             |
| `amenity_ids`                 | list of strings  | ❌       | IDs of main amenities from DB   | `["amenity-uuid-1", "amenity-uuid-2"]`                                |

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
    "status": "draft",
    "is_verified": false,
    "square_feet": 400,
    "length": 20,
    "width": 20,
    "num_of_bathrooms": 1,
    "num_of_toilets": 1,
    "num_of_parking_spaces": 1
  },
  "pricings": [
    {
      "price_type": "hourly",
      "price": 500,
      "currency": "NGN",
      "start_date": "2026-02-12T09:00:00Z",
      "end_date": "2026-02-12T17:00:00Z"
    },
    {
      "price_type": "daily",
      "price": 3000,
      "currency": "NGN",
      "start_date": "2026-02-12T00:00:00Z",
      "end_date": "2026-02-12T23:59:59Z"
    }
  ],
  "addons": [
    {
      "name": "Breakfast",
      "description": "Continental breakfast included",
      "price": 1000,
      "currency": "NGN"
    },
    {
      "name": "Airport Pickup",
      "description": "Pickup from the airport",
      "price": 2000,
      "currency": "NGN"
    }
  ],
  "use_cases": [
    {
      "name": "Business Trip",
      "description": "Perfect for short business trips"
    },
    {
      "name": "Vacation",
      "description": "Ideal for leisure travelers"
    }
  ],
  "rules": [
    {
      "title": "No Smoking",
      "description": "Smoking is strictly prohibited inside the space."
    },
    {
      "title": "No Pets",
      "description": "Pets are not allowed in the space."
    }
  ],
  "custom_amenities": [
    {
      "name": "Pet-Friendly Sofa"
    },
    {
      "name": "Smart TV with Netflix"
    }
  ],
  "amenity_ids": ["amenity-uuid-1", "amenity-uuid-2", "amenity-uuid-3"]
}
```
