from core.api_client import APIClient


class BaseEndpoint:
    """Base class for API Endpoint Service Objects."""

    def __init__(self, client: APIClient):
        self.client = client
