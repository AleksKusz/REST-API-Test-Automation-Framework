# REST API Test Automation Framework

```text
THIS PROJECT IS MOSTLY FOR EDUCATIONAL PURPOSES
```
A lightweight REST API test automation framework built with **Python**, **pytest**, **requests**, and **jsonschema**.

The current test suite validates the JSONPlaceholder `/users` and `/posts` endpoints.

## What it covers

- GET, POST, PUT, and DELETE requests
- Positive and negative API scenarios
- JSON schema and email-format validation
- Parameterized tests with pytest
- Reusable API clients, fixtures, test data, and assertions
- Configurable base URL through the `BASE_URL` environment variable

## Project structure

```text
api/         API client classes
schemas/     JSON schemas used for response validation
test_data/   JSON request payloads
tests/       pytest test cases
utils/       reusable assertions
conftest.py  shared pytest fixtures
pytest.ini   pytest configuration
```

## Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it, then install the dependencies:

```bash
pip install pytest requests jsonschema
```

## Run tests

```bash
pytest
```

By default, tests run against:

```text
https://jsonplaceholder.typicode.com/
```

To use another API, set the `BASE_URL` environment variable before running the tests.
