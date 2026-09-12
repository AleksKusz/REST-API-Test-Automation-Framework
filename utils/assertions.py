def assert_status_code(response, expected_status):
    assert response.status_code == expected_status, (f"Expected status code {expected_status}, but got {response.status_code}")

def assert_json_content_type(response):
    content_type = response.headers.get("Content-Type", "")
    assert "application/json" in content_type.lower(), (f"Expected JSON content type, but got {content_type!r}"
    )

def assert_type(response,expected_type):
    assert isinstance(response,expected_type), f"Expected type {expected_type}, but got {expected_type(response)}"