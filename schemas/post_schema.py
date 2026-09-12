post_schema = {
    "title": "Post",
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
    },
    "required": ["userId", "id", "title", "body"],
}

