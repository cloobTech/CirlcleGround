# Update newly created a Space

**Endpoint:** `POST /spaces/{space_id}`  
**Description:** update a new space with all related data (pricings, addons, use cases, rules, amenities).  
**Content-Type:** `application/json`

### Request Parameters

| Parameter               | Type             | Required | Description                     | Example / Notes                                                                       |
| ----------------------- | ---------------- | -------- | ------------------------------- | ------------------------------------------------------------------------------------- |
| `pricings`              | list of objects  | ✅       | List of pricing rules           | See `SpacePricingSchema` below                                                        |
| `pricings.price_type`   | enum (lowercase) | ✅       | Type of pricing                 | `"hourly"`, `"daily"`, `"weekly"`, `"monthly"`                                        |
| `pricings.price`        | float            | ✅       | Price for this period           | `500`                                                                                 |
| `pricings.currency`     | string           | ❌       | Currency code                   | `"NGN"` (default)                                                                     |
| `pricings.start_date`   | datetime         | ✅       | Start of pricing period         | `"2026-02-12T09:00:00Z"`                                                              |
| `pricings.end_date`     | datetime         | ✅       | End of pricing period           | `"2026-02-12T17:00:00Z"`                                                              |
| `addons`                | list of objects  | ❌       | Extra services for the space    | See `SpaceAddonSchema`                                                                |
| `addons.name`           | string           | ✅       | Name of addon                   | `"Breakfast"`                                                                         |
| `addons.description`    | string           | ❌       | Description of addon            | `"Continental breakfast included"`                                                    |
| `addons.price`          | float            | ✅       | Price for the addon             | `1000`                                                                                |
| `addons.currency`       | string           | ❌       | Currency code                   | `"NGN"` (default)                                                                     |
| `use_cases`             | list of objects  | ❌       | defined use cases               | See `SpaceUseCaseSchema`                                                              |
| `use_cases.name`        | string           | ✅       | Name of use case                | `"Business Trip"`                                                                     |
| `use_cases.description` | string           | ❌       | Description of use case         | `"Perfect for short business trips"`                                                  |
| `rules`                 | list of objects  | ❌       | Rules for the space             | See `SpaceRuleSchema`                                                                 |
| `rules.title`           | string           | ✅       | Title of the rule               | `"No Smoking"`                                                                        |
| `rules.description`     | string           | ❌       | Rule description                | `"Smoking is strictly prohibited inside the space."`                                  |
| `custom_amenities`      | list of objects  | ❌       | Custom amenities added by owner | See `SpaceCustomAmenitySchema`                                                        |
| `custom_amenities.name` | string           | ✅       | Name of custom amenity          | `"Smart TV with Netflix"`                                                             |
| `amenity_ids`           | list of strings  | ❌       | IDs of main amenities from DB   | `["amenity-uuid-1", "amenity-uuid-2"]`                                                |
| `status`                | enum (lowercase) | ❌       | Status of space                 | `"draft"`, `"pending"`, `"available"`, `"published"`, `"rejected` (default `"draft"`) |

```json
{
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
  "amenity_ids": ["amenity-uuid-1", "amenity-uuid-2", "amenity-uuid-3"],
  "status": "draft"
}
```
