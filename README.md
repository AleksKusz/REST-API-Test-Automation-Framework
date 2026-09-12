# REST-API-Test-Automation-Framework

REST API Test Automation Framework

A lightweight REST API test automation framework built with Python, pytest, requests, and jsonschema. The current test suite validates the JSONPlaceholder /users and /posts endpoints.

What it covers
GET, POST, PUT, and DELETE requests
Positive and negative API scenarios
JSON schema and email-format validation
Parameterized tests with pytest
Reusable API clients, fixtures, test data, and assertions
Configurable base URL through the BASE_URL environment variable
Project structure
api/         API client classes
schemas/     JSON schemas used for response validation
test_data/   JSON request payloads
tests/       pytest test cases
utils/       reusable assertions
conftest.py  shared pytest fixtures
pytest.ini   pytest configuration
Setup
python -m venv .venv

Activate the virtual environment, then install the dependencies:

pip install pytest requests jsonschema
Run tests
pytest

By default, tests run against https://jsonplaceholder.typicode.com/. To use another API, set BASE_URL before running the tests.
