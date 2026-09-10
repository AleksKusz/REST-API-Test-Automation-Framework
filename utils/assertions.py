def assert_status_code(response, expected_status):
    assert response.status_code == expected_status, (f"Expected status code {expected_status}, but got {response.status_code}")
