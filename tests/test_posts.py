import pytest, requests, json, logging
from jsonschema import ValidationError, validate, FormatChecker
from schemas.post_schema import post_schema
from api.posts_api import PostApi
from utils.assertions import assert_status_code, assert_json_content_type, assert_type

@pytest.mark.parametrize("post_id", range(1,10))
def test_get_post(base_url,api_session, post_id):
    post_api=PostApi(base_url,api_session)
    response=post_api.get_post(post_id)
    data=response.json()
    assert_status_code(response,200)
    validate(instance=data, schema=post_schema)

 


