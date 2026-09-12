# REST API Test Automation Framework

[![API Tests](https://github.com/AleksKusz/REST-API-Test-Automation-Framework/actions/workflows/tests.yml/badge.svg)](https://github.com/AleksKusz/REST-API-Test-Automation-Framework/actions/workflows/tests.yml)

A small REST API test automation framework built with **Python**, **pytest**, **requests**, and **jsonschema**.

This is a learning project created to practice API test automation, Python, reusable test architecture, schema validation, mocking, and CI with GitHub Actions.

The test suite uses the public [JSONPlaceholder](https://jsonplaceholder.typicode.com/) REST API and currently covers the `/users` and `/posts` resources.

## Features

- Automated testing of `GET`, `POST`, `PUT`, and `DELETE` requests
- Positive and negative API test scenarios
- JSON Schema validation
- Email format validation with `jsonschema.FormatChecker`
- Parameterized pytest tests
- Query-parameter testing
- Shared pytest fixtures
- Reusable API client classes
- Reusable assertion helpers
- External JSON test data
- Configurable request timeouts
- Mocked timeout testing with `monkeypatch`
- Custom exception handling
- Configurable API base URL through an environment variable
- GitHub Actions CI
- JUnit XML test reports uploaded as CI artifacts

## Project Structure

```text
REST-API-Test-Automation-Framework/
├── .github/
│   └── workflows/
│       └── tests.yml
├── api/
│   ├── posts_api.py
│   └── users_api.py
├── schemas/
│   ├── post_schema.py
│   ├── post_user_schema.py
│   └── user_schema.py
├── test_data/
│   ├── post_user.json
│   ├── posts.json
│   ├── user.json
│   └── wrong_user.json
├── tests/
│   ├── test_posts.py
│   └── test_users.py
├── utils/
│   ├── assertions.py
│   └── exceptions.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Test Coverage

### Users

The `/users` tests include:

- retrieving individual users
- validating user responses against a JSON Schema
- checking invalid user IDs
- retrieving all users
- filtering users with query parameters
- creating users from different JSON payloads
- checking valid and invalid payload schemas
- updating a user
- deleting users

### Posts

The `/posts` tests include:

- retrieving individual posts
- retrieving and validating the full posts collection
- creating a post
- checking whether the referenced user exists before creating a post
- updating a post
- deleting a post
- verifying timeout handling with a mocked request

## Requirements

- Python 3.14+
- `pip`

Project dependencies are listed in `requirements.txt`:

```text
pytest
requests
jsonschema
```

## Installation

Clone the repository:

```bash
git clone https://github.com/AleksKusz/REST-API-Test-Automation-Framework.git
cd REST-API-Test-Automation-Framework
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

On Linux or macOS:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the Tests

Run the complete test suite:

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

Run only the user tests:

```bash
pytest tests/test_users.py
```

Run only the post tests:

```bash
pytest tests/test_posts.py
```

Run a single test:

```bash
pytest tests/test_posts.py::test_request_timeout -v
```

## Configuration

By default, the test suite uses:

```text
https://jsonplaceholder.typicode.com/
```

The base URL can be overridden with the `BASE_URL` environment variable.

Windows PowerShell:

```powershell
$env:BASE_URL="https://example.com/"
pytest
```

Linux/macOS:

```bash
BASE_URL="https://example.com/" pytest
```

## Continuous Integration

GitHub Actions automatically runs the test suite on:

- pushes
- pull requests

The workflow:

1. starts an Ubuntu runner
2. checks out the repository
3. installs Python
4. installs dependencies from `requirements.txt`
5. runs the pytest suite
6. generates a JUnit XML report
7. uploads the test report as a GitHub Actions artifact





