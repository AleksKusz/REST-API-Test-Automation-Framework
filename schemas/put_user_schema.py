put_user_schema = {
    "title": "User",
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "address": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "street": {"type": "string"},
                "suite": {"type": "string"},
                "city": {"type": "string"},
                "zipcode": {"type": "string"},
                "geo": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "lat": {"type": "string"},
                        "lng": {"type": "string"},
                    },
                    "optional": ["lat", "lng"],
                },
            },
            "optional": ["street", "suite", "city", "zipcode", "geo"],
        },
        "phone": {"type": "string"},
        "website": {"type": "string"},
        "company": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "name": {"type": "string"},
                "catchPhrase": {"type": "string"},
                "bs": {"type": "string"},
            },
            "optional": ["name", "catchPhrase", "bs"],
        },
    },
    "required": [
        "id",
        "name",
        "username",
        "email"
    ],
    "optional": [
        "address",
        "phone",
        "website",
        "company"
    ]
}
