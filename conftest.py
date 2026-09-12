import pytest
import os   
import requests
import json

@pytest.fixture
def base_url():
    return os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com/")

@pytest.fixture
def api_session():
    api_session=requests.Session()
    api_session.headers.update({"Accept": "application/json"})

    yield api_session
    api_session.close()

@pytest.fixture
def user_payload_mark(file_path):
    with open(f"test_data/{file_path}") as file:
            payload = json.load(file)
            return payload

@pytest.fixture
def user_payload():
    with open(f"test_data/user.json") as file:
            payload = json.load(file)
            return payload


#######################################

@pytest.fixture
def post_payload():
    with open(f"test_data/posts.json") as file:
            payload = json.load(file)
            return payload


