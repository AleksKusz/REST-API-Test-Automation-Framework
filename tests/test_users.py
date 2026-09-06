import pytest, requests, json
from jsonschema import validate
from schemas.user_schema import user_schema
from api.users_api import usersapi




response= requests.get("https://jsonplaceholder.typicode.com/users/1")
print(response.json())



#test data sourced from https://jsonplaceholder.typicode.com/

#schema for user data

@pytest.mark.parametrize("user_id, expected_status", [(1, 200) , (2, 200), (3, 200), (4, 200), (5, 200), (6, 200)])


def test_user_schema_validation(base_url, api_session, user_id, expected_status):
    user_api = usersapi(base_url, api_session)
    response = user_api.get_user(user_id)
    assert response.status_code == expected_status, f"Expected status code {expected_status}, but got {response.status_code}"
    user_data = response.json()
    
    # Validate the user data against the schema
    validate(instance=user_data, schema=user_schema)