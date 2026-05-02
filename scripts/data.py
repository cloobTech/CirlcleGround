AMENITIES = [
    {"name": "WiFi", "category": "connectivity", "id": "wifi"},
    {"name": "Parking", "category": "facilities", "id": "parking"},
    {"name": "Air Conditioning", "category": "comfort", "id": "air_conditioning"},
    {"name": "Kitchen", "category": "facilities", "id": "kitchen"},
    {"name": "Pool", "category": "leisure", "id": "pool"},
]


REGISTER_USER = {
    "id": "user_12345",
    "first_name": "Olamide",
    "last_name": "Bello",
    "password": "password",
    "location": "123 Loc",
    "phone_number": "+233 6248 2022",
    "email": "belkid98@gmail.com"
}

REGISTER_ADMIN = {
    "id": "user_1234",
    "first_name": "Emmanuel",
    "last_name": "Nwokoma",
    "password": "password",
    "location": "123 Loc",
    "phone_number": "+233 6246 2022",
    "email": "emmanuelnwokoma364@gmail.com",
    "role": "admin"
}
REGISTER_SUPER_ADMIN = {
    "id": "user_123456",
    "first_name": "Miracle",
    "last_name": "Gini",
    "password": "password",
    "location": "123 Loc",
    "phone_number": "+233 6247 2022",
    "email": "germany@gmail.com",
    "role": "super_admin"
}


CREATE_SPACE = {
    "location_id": "loc_001",
    "price_per_hour": 30000,
    "name": "Modern Event Hall",
    "description": "A spacious and well-lit hall suitable for events, meetings, and celebrations.",
    "price": 50000,
    "max_guests": 150,
    "space_type": "hall",
    "category": "event",
    "status": "draft",
    "is_verified": False,
    "square_feet": 2000,
    "length": 50,
    "width": 40,
    "num_of_bathrooms": 2,
    "num_of_toilets": 4,
    "num_of_parking_spaces": 20

}


UPDATE_NEW_SPACE = {
    "use_cases": [
        {
            "name": "Wedding",
            "description": "Suitable for wedding ceremonies and receptions"
        },
        {
            "name": "Conference",
            "description": "Ideal for business meetings and corporate events"
        }
    ],
    "rules": [
        {
            "title": "No Smoking",
            "description": "Smoking is not allowed inside the hall"
        },
        {
            "title": "No Loud Music After 10PM",
            "description": "Music volume must be reduced after 10PM"
        }
    ],
    "pricings": [
        {
            "price_type": "hourly",
            "price": 10000,
            "currency": "NGN",
            "start_date": "2026-01-01T00:00:00",
            "end_date": "2026-12-31T23:59:59"
        },
        {
            "price_type": "daily",
            "price": 50000,
            "currency": "NGN",
            "start_date": "2026-01-01T00:00:00",
            "end_date": "2026-12-31T23:59:59"
        }
    ],
    "amenity_ids": [
        "wifi",
        "parking",
        "air_conditioning",

    ],
    "custom_amenities": [
        {
            "name": "Pet-Friendly Sofa"
        },
        {
            "name": "Smart TV with Netflix"
        }
    ],
    "operation_hours": [
        {
            "day_of_week": 0,
            "open_time": "09:00:00",
            "close_time": "17:00:00",
            "is_closed": False

        },
        {
            "day_of_week": 1,
            "open_time": "09:00:00",
            "close_time": "17:00:00",
            "is_closed": False

        },


        {
            "day_of_week": 2,
            "open_time": "09:00:00",
            "close_time": "17:00:00",
            "is_closed": False

        },
        {
            "day_of_week": 3,
            "open_time": "09:00:00",
            "close_time": "17:00:00",
            "is_closed": False

        },
        {
            "day_of_week": 4,
            "open_time": "09:00:00",
            "close_time": "17:00:00",
            "is_closed": False

        },
        {
            "day_of_week": 5,
            "open_time": "09:00:00",
            "close_time": "17:00:00",
            "is_closed": False

        },
        {
            "day_of_week": 6,
            "open_time": "09:00:00",
            "close_time": "17:00:00",
            "is_closed": False

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
    "status": "draft"

}


SPACE_IMAGE = [
    {
        "url": "https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80",
        "order": 1
    },
    {
        "url": "https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80",
        "order": 2
    },
]
