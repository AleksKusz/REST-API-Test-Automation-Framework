import pytest, requests, json, logging
from jsonschema import ValidationError, validate
from schemas.user_schema import user_schema
from schemas.post_user_schema import put_user_schema
from api.users_api import UsersApi
from utils.assertions import assert_status_code




#test data sourced from https://jsonplaceholder.typicode.com/

#schema for user data

@pytest.mark.parametrize("user_id, expected_status", [(1, 200) , (2, 200), (3, 200), (4, 200), (5, 200), (6, 200), (7, 200), (8, 200), (9, 200), (10, 200)])


def test_user_schema_validation(base_url, api_session, user_id, expected_status):
    user_api = UsersApi(base_url, api_session)
    response = user_api.get_user(user_id)
    assert response.status_code == expected_status, f"Expected status code {expected_status}, but got {response.status_code}"
    user_data = response.json()
    
    # Validate the user data against the schema
    validate(instance=user_data, schema=user_schema)

@pytest.mark.parametrize("user_id, expected_status", [(0,404),(99999,404), ("a",404), ("b", 404), ("abcd", 404)])

def test_user_negative_status(base_url, api_session, user_id, expected_status):
    user_api = UsersApi(base_url, api_session) 
    response = user_api.get_user(user_id)
    assert_status_code(response,expected_status)
    assert response.status_code == expected_status, f"Expected status code {expected_status}, but got {response.status_code}"


def test_get_all_users(base_url, api_session,):
    expected_length = 10
    user_api = UsersApi(base_url, api_session)
    response=user_api.get_users()
    response_list = response.json()
    assert_status_code(response,200), f"Expected status code 200, but got {response.status_code}"
    assert isinstance(response_list, list), f"Expected Type List, but got type {type(response_list)}"
    assert len(response_list) == expected_length, f"Expected {expected_length} users but got {len(response_list)} users instead"
    for item in response_list:
        validate(instance=item,schema= user_schema)
        print(f"validation for {item["id"]} complete") 

@pytest.mark.parametrize("file_path", [("user.json"), ("post_user.json"), ("wrong_user.json")])

def test_user_post(base_url,api_session,file_path):
    user_api= UsersApi(base_url, api_session)
    with open(f"test_data/{file_path}") as file:
        payload = json.load(file)

    response=user_api.post_user(payload)
    assert_status_code(response,201)
    data=response.json()

    if file_path=="user.json":
        validate(instance=data, schema=user_schema)

    if file_path=="post_user.json":
        validate(instance=data, schema=put_user_schema)

    if file_path=="wrong_user.json":
        with pytest.raises(ValidationError):
            validate(instance=data, schema=put_user_schema)

    highest_user_response=user_api.get_users()
    assert_status_code(highest_user_response,200)
    test_id_high = highest_user_response.json()
    highest_id=max(test_id_high, key=lambda test_id_high: test_id_high["id"])
    assert data["id"] == highest_id["id"]+1








#             payload = json.load(file)
#Works but so stupid I can't even look at it
# #def test_user_post(base_url,api_session,file_path):
#     user_api= UsersApi(base_url, api_session)
#     for paths in file_path:
#         with open(f"test_data/{file_path}") as file:
#             payload = json.load(file)
#             if file_path=="user.json":
#                 response = user_api.post_user(payload)
#                 assert_status_code(response,201)
#                 data = response.json()
#                 validate(instance=data, schema=user_schema)
#             if file_path=="put_user.json":
#                 response=user_api.post_user(payload)
#                 assert_status_code(response,201)
#                 data = response.json()
#                 validate(instance=data, schema=put_user_schema)
#             if file_path=="put_wrong_user.json":
#                 response=user_api.post_user(payload)
#                 data=response.json()
#                 with pytest.raises(ValidationError):
#                     validate(instance=data, schema=put_user_schema)
#                 continue
#             highest_user_response=user_api.get_users()
#             assert_status_code(highest_user_response,200)
#             test_id_high = highest_user_response.json()
#             highest_id=max(test_id_high, key=lambda test_id_high: test_id_high["id"])
#             assert data["id"] == highest_id["id"]+1
            


    

    #data = response.json()
    #validate(instance=data, schema=put_user_schema)
    #highest_user_response=user_api.get_users()
    #assert_status_code(highest_user_response,200)
    #test_id_high = highest_user_response.json()
    #highest_id=max(test_id_high, key=lambda test_id_high: test_id_high["id"])
    #assert data["id"] == highest_id["id"]+1


