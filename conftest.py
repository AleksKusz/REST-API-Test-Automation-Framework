import pytest
import os   
import requests

@pytest.fixture
def base_url():
    return os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com/")

@pytest.fixture
def api_session():
    api_session=requests.Session()
    api_session.headers.update({"Accept": "application/json"})

    yield api_session
    api_session.close()
