import pytest
from config.config import Config
from core.api_client import APIClient
from endpoints.user_endpoint import UserEndpoint


def pytest_addoption(parser):
    """Add custom command-line options to pytest."""
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Target test environment: dev, staging, prod",
    )


@pytest.fixture(scope="session")
def api_config(request) -> Config:
    """Fixture providing Config instance for selected environment."""
    env = request.config.getoption("--env")
    return Config(env=env)


@pytest.fixture(scope="session")
def api_client(api_config) -> APIClient:
    """Fixture providing APIClient instance."""
    client = APIClient(cfg=api_config)
    yield client
    client.session.close()


@pytest.fixture(scope="function")
def user_endpoint(api_client) -> UserEndpoint:
    """Fixture providing UserEndpoint service object."""
    return UserEndpoint(client=api_client)


# Customizing Pytest HTML Report
def pytest_html_report_title(report):
    report.title = "API Automation Test Report"


def pytest_configure(config):
    if hasattr(config, "_metadata"):
        config._metadata["Project"] = "Python API Framework"
        config._metadata["Framework"] = "Pytest + Requests + Pydantic"
