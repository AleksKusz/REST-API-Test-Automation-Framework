import pytest, requests, json, logging
from jsonschema import validate
from schemas.user_schema import user_schema
from api.users_api import usersapi
from utils.assertions import assert_status_code




response= requests.get("https://jsonplaceholder.typicode.com/users/1")
print(response.json())



#test data sourced from https://jsonplaceholder.typicode.com/

#schema for user data

@pytest.mark.parametrize("user_id, expected_status", [(1, 200) , (2, 200), (3, 200), (4, 200), (5, 200), (6, 200), (7, 200), (8, 200), (9, 200), (10, 200)])


def test_user_schema_validation(base_url, api_session, user_id, expected_status):
    user_api = usersapi(base_url, api_session)
    response = user_api.get_user(user_id)
    assert response.status_code == expected_status, f"Expected status code {expected_status}, but got {response.status_code}"
    user_data = response.json()
    
    # Validate the user data against the schema
    validate(instance=user_data, schema=user_schema)

@pytest.mark.parametrize("user_id, expected_status", [(0,404),(99999,404), ("a",404), ("b", 404), ("abcd", 404)])

def test_user_negative_status(base_url, api_session, user_id, expected_status):
    user_api = usersapi(base_url, api_session) 
    response = user_api.get_user(user_id)
    assert_status_code(response,expected_status)
    assert response.status_code == expected_status, f"Expected status code {expected_status}, but got {response.status_code}"


def test_user_post(base_url,api_session):
    user_api= usersapi(base_url, api_session)
    with open("test_data/user.json") as file:
        payload = json.load(file)

    

    response = user_api.post_user(payload)
    assert_status_code(response,201)
    data = response.json()
    validate(instance=data, schema=user_schema)
    assert data["name"] == payload["name"]
    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]  #and for all of them
    print(data["id"])
