import pytest, requests, json
from jsonschema import ValidationError, validate, FormatChecker
from schemas.user_schema import user_schema
from schemas.post_user_schema import post_user_schema
from api.users_api import UsersApi
from utils.assertions import assert_status_code, assert_json_content_type, assert_type


#test data sourced from https://jsonplaceholder.typicode.com/


pytestmark = [
    pytest.mark.api,
    pytest.mark.regression,
]

@pytest.mark.parametrize("user_id, expected_status", [(1, 200) , (2, 200), (3, 200), (4, 200), (5, 200), (6, 200), (7, 200), (8, 200), (9, 200), (10, 200)])

@pytest.mark.smoke
def test_user_schema_validation(base_url, api_session, user_id, expected_status):
    user_api = UsersApi(base_url, api_session)
    response = user_api.get_user(user_id)
    assert_status_code(response, expected_status)
    assert_json_content_type(response)
    user_data = response.json()
    
    #Validate the user data against the schema
    validate(instance=user_data, schema=user_schema, format_checker=FormatChecker())

@pytest.mark.parametrize("user_id, expected_status", [(0,404),(99999,404), ("a",404), ("b", 404), ("abcd", 404)])


def test_user_negative_status(base_url, api_session, user_id, expected_status):
    user_api = UsersApi(base_url, api_session) 
    response = user_api.get_user(user_id)
    assert_status_code(response,expected_status)
    assert_json_content_type(response)

@pytest.mark.smoke
def test_get_all_users(base_url, api_session,):
    expected_length = 10
    user_api = UsersApi(base_url, api_session)
    response=user_api.get_users()
    response_list = response.json()
    assert_status_code(response,200)
    assert_json_content_type(response)
    assert_type(response_list, list)
    assert len(response_list) == expected_length, f"Expected {expected_length} users but got {len(response_list)} users instead"
    for item in response_list:
        validate(instance=item,schema= user_schema,format_checker=FormatChecker()) #email checked by FormatChecker()

@pytest.mark.parametrize("file_path", [("user.json"), ("post_user.json"), ("wrong_user.json")])

def test_user_post(base_url,api_session,file_path, user_payload_mark):
    user_api= UsersApi(base_url, api_session)
    payload=user_payload_mark #fixture in conftest.py, file_path passed
    response=user_api.post_user(payload)
    assert_status_code(response,201)
    assert_json_content_type(response)
    data=response.json()

    if file_path=="user.json":
        validate(instance=data, schema=user_schema, format_checker=FormatChecker()) #email checked by FormatChecker()

    if file_path=="post_user.json":
        validate(instance=data, schema=post_user_schema, format_checker=FormatChecker()) #email checked by FormatChecker()

    if file_path=="wrong_user.json":
        with pytest.raises(ValidationError):
            validate(instance=data, schema=post_user_schema, format_checker=FormatChecker()) #email checked by FormatChecker()

    highest_user_response=user_api.get_users()
    assert_status_code(highest_user_response,200)
    test_id_high = highest_user_response.json()
    highest_id=max(test_id_high, key=lambda test_id_high: test_id_high["id"])
    assert data["id"] == highest_id["id"]+1 #for jsonplaceholder.com POST isn't saved but still nice to have


@pytest.mark.parametrize("user_id", [("1"), ("2"), ("3"), ("4")])

def test_user_delete(base_url, api_session,user_id):
    user_api=UsersApi(base_url, api_session)
    response=user_api.delete_user(user_id)
    assert_status_code(response, 200)
    assert_json_content_type(response)

@pytest.mark.parametrize("params", [{"username": "Bret"}]) 
def test_get_param_user(base_url, api_session,params):
    user_api=UsersApi(base_url, api_session)
    response=user_api.get_users(params=params) #can search for any value using params value
    data=response.json()
    
    assert data, "No user returned" #FILTERING RETURNS A LIST!
    assert_json_content_type(response)
    assert all(user["username"] == params["username"] for user in data) #FILTERING RETURNS A LIST!


def test_put_user(base_url, api_session,user_payload):
    user_api=UsersApi(base_url, api_session)
    response_before=user_api.get_user(1)
  
    response=user_api.put_user(1,user_payload)
    data=response.json()
    data_before=response_before.json()
    validate(instance=data, schema=user_schema, format_checker=FormatChecker())
    validate(instance=data_before, schema=user_schema, format_checker=FormatChecker())
    assert_status_code(response,200)
    assert_json_content_type(response)
    assert data["id"]==1
    assert data["name"]!=data_before["name"]
    assert data["username"]!=data_before["username"]












