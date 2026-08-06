# Python API Test Automation Framework

A modern, production-grade API Test Automation Framework built in Python using `pytest`, `requests`, `pydantic` v2, custom logging, and HTML reporting.

---

## 🚀 Features

- **Service Object Model**: Endpoint logic encapsulated in clean, reusable service objects (`endpoints/`).
- **Pydantic Schema Validation**: Automatic response JSON deserialization and strict schema assertion using Pydantic models (`models/`).
- **Environment Management**: Multi-environment support (`dev`, `staging`, `prod`) via `env.ini` and environment variables.
- **API Client Wrapper**: Centralized `requests.Session` management (`core/api_client.py`) with automatic timing, request/response logging, and error tracking.
- **Rich Logging**: Formatted console & file log output (`logs/api_test.log`) detailing HTTP methods, URLs, masked auth headers, status codes, and latency.
- **HTML Reporting**: Automatic self-contained HTML test report generation via `pytest-html`.
- **Dynamic Test Data**: Dynamic payload generators (`test_data/` and `utils/helpers.py`).

---

## 📁 Directory Structure

```text
python_api_framework/
├── config/
│   ├── config.py              # Environment configuration loader
│   └── env.ini                # Base URLs, timeouts, keys per environment
├── core/
│   ├── api_client.py          # Requests Session wrapper with logging & timing
│   ├── logger.py              # Centralized logging configuration
│   └── response_validator.py  # Response assertions (status code, schema, values, latency)
├── endpoints/
│   ├── base_endpoint.py       # Abstract endpoint base class
│   └── user_endpoint.py       # User API endpoint methods (GET, POST, PUT, PATCH, DELETE)
├── models/
│   └── user_model.py          # Pydantic v2 schemas for payload & response validation
├── test_data/
│   └── user_payloads.py       # Dynamic payload generators & static fixtures
├── tests/
│   ├── conftest.py            # Pytest fixtures and reporting hooks
│   └── test_users_api.py      # E2E User API test cases
├── utils/
│   └── helpers.py             # Random data generation helpers
├── logs/
│   └── api_test.log           # Test run log file
├── reports/
│   └── report.html            # Pytest HTML execution report
├── pytest.ini                 # Pytest configuration
├── requirements.txt           # Python dependencies
└── README.md                  # Framework documentation
```

---

## 🛠️ Getting Started

### 1. Prerequisites
- Python 3.10+ installed

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🧪 Running Tests

### Run All Tests
```bash
pytest
```

### Run Tests with HTML Report
```bash
pytest --html=reports/report.html --self-contained-html
```

### Run Specific Test Suite or Markers
```bash
# Smoke tests only
pytest -m smoke

# Regression tests only
pytest -m regression

# Specific test file
pytest tests/test_users_api.py
```

### Target Different Environments
```bash
# Run against DEV (default)
pytest --env dev

# Run against STAGING
pytest --env staging
```

---

## 📊 Reports & Logs

- **Logs**: Detailed execution logs are recorded in `logs/api_test.log` and displayed in the console during test execution.
- **HTML Report**: After test runs, open `reports/report.html` in any browser for visual test metrics and failure backtraces.
