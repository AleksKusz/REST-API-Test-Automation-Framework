import pytest, requests, json
from jsonschema import ValidationError, validate, FormatChecker
from schemas.post_schema import post_schema
from api.posts_api import PostApi
from api.users_api import UsersApi
from utils.assertions import assert_status_code, assert_json_content_type, assert_type
from utils.exceptions import InvalidPostUserError

pytestmark = [
    pytest.mark.api,
    pytest.mark.regression,
]
@pytest.mark.smoke
@pytest.mark.parametrize("post_id", range(1,10))
def test_get_post(base_url,api_session, post_id):
    post_api=PostApi(base_url,api_session)
    response=post_api.get_post(post_id)
    assert_status_code(response,200)
    assert_json_content_type(response)
    data=response.json()
    validate(instance=data, schema=post_schema)
    
@pytest.mark.smoke
def test_get_posts(base_url,api_session):
    post_api=PostApi(base_url,api_session)
    response=post_api.get_posts()
    assert_status_code(response,200)
    assert_json_content_type(response)
    expected_length=100
    data=response.json()
    assert_type(data,list)
    assert len(data) == expected_length
    for item in data:
        validate(instance=item,schema=post_schema)

def test_post_post(base_url,api_session,post_payload):
    post_api=PostApi(base_url,api_session)
    user_api=UsersApi(base_url,api_session) 

    user_id_check=user_api.get_users()
    assert_status_code(user_id_check,200)
    assert_json_content_type(user_id_check)

    data_user_id=user_id_check.json()
    id_list=set()
    for item in data_user_id:
        id_list.add(item["id"])

    if post_payload['userId'] in id_list:
        response=post_api.post_post(post_payload)
        assert_status_code(response,201)
        assert_json_content_type(response)
        data=response.json()
        validate(instance=data, schema=post_schema)

    else:
#       with pytest.raises(InvalidPostUserError):
        raise InvalidPostUserError(
            f"Cannot create post: user ID {post_payload['userId']} does not exist"
        )

def test_put_post(base_url, api_session, post_payload):
    post_api=PostApi(base_url, api_session)
    post_id=1

    response_before=post_api.get_post(post_id)
    assert_status_code(response_before, 200)
    assert_json_content_type(response_before)

    response=post_api.put_post(post_id, post_payload)
    assert_status_code(response, 200)
    assert_json_content_type(response)

    data_before=response_before.json()
    data=response.json()
    validate(instance=data_before, schema=post_schema)
    validate(instance=data, schema=post_schema)

    assert data["id"] == post_id
    assert data["title"] == post_payload["title"]
    assert data["body"] == post_payload["body"]

def test_delete_post(base_url, api_session):
    post_api=PostApi(base_url, api_session)
    post_id=1

    response = post_api.delete_post(post_id)

    assert_status_code(response, 200)
    assert_json_content_type(response)

def test_request_timeout(base_url, api_session, monkeypatch):
    post_api = PostApi(base_url, api_session, timeout=0.0001)

    def fake_get(*args, **kwargs):
        raise requests.exceptions.Timeout

    monkeypatch.setattr(api_session, "get", fake_get)

    with pytest.raises(requests.exceptions.Timeout):
        post_api.get_post(1)
        




 
