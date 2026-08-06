from typing import Any, Dict, Optional, Union
from requests import Response

from endpoints.base_endpoint import BaseEndpoint
from models.user_model import CreateUserRequest


class UserEndpoint(BaseEndpoint):
    """Service layer for User API endpoints (/users)."""

    ENDPOINT_PATH = "/users"

    def get_all_users(self, params: Optional[Dict[str, Any]] = None) -> Response:
        """Fetch all users list."""
        return self.client.get(self.ENDPOINT_PATH, params=params)

    def get_user_by_id(self, user_id: int) -> Response:
        """Fetch a single user by ID."""
        return self.client.get(f"{self.ENDPOINT_PATH}/{user_id}")

    def create_user(self, payload: Union[Dict[str, Any], CreateUserRequest]) -> Response:
        """Create a new user."""
        json_data = payload.model_dump() if isinstance(payload, CreateUserRequest) else payload
        return self.client.post(self.ENDPOINT_PATH, json_data=json_data)

    def update_user(self, user_id: int, payload: Dict[str, Any]) -> Response:
        """Update an existing user via PUT."""
        return self.client.put(f"{self.ENDPOINT_PATH}/{user_id}", json_data=payload)

    def patch_user(self, user_id: int, payload: Dict[str, Any]) -> Response:
        """Partially update user via PATCH."""
        return self.client.patch(f"{self.ENDPOINT_PATH}/{user_id}", json_data=payload)

    def delete_user(self, user_id: int) -> Response:
        """Delete a user by ID."""
        return self.client.delete(f"{self.ENDPOINT_PATH}/{user_id}")
