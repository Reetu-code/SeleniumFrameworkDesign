import pytest
from core.response_validator import ResponseValidator
from endpoints.user_endpoint import UserEndpoint
from models.user_model import UserModel, UserResponseModel
from test_data.user_payloads import get_random_user_payload, VALID_USER_DICT_PAYLOAD


@pytest.mark.smoke
@pytest.mark.user
class TestUsersAPI:
    """Test suite for User Management API endpoints."""

    def test_get_all_users_success(self, user_endpoint: UserEndpoint):
        """Verify GET /users returns 200 OK and valid schema list."""
        response = user_endpoint.get_all_users()
        
        ResponseValidator.assert_status_code(response, 200)
        users = ResponseValidator.assert_schema(response, UserModel)
        assert len(users) > 0, "Users list should not be empty"

    def test_get_user_by_id_success(self, user_endpoint: UserEndpoint):
        """Verify GET /users/{id} returns 200 OK and matches target user."""
        target_id = 1
        response = user_endpoint.get_user_by_id(target_id)
        
        ResponseValidator.assert_status_code(response, 200)
        user = ResponseValidator.assert_schema(response, UserResponseModel)
        
        assert user.id == target_id, f"Expected ID {target_id}, got {user.id}"
        ResponseValidator.assert_json_value(response, "id", target_id)

    @pytest.mark.regression
    def test_get_non_existent_user(self, user_endpoint: UserEndpoint):
        """Verify GET /users/{invalid_id} returns 404 Not Found."""
        invalid_id = 99999
        response = user_endpoint.get_user_by_id(invalid_id)
        
        ResponseValidator.assert_status_code(response, 404)

    def test_create_user_with_model_payload(self, user_endpoint: UserEndpoint):
        """Verify POST /users creates user successfully using Pydantic model."""
        payload = get_random_user_payload()
        response = user_endpoint.create_user(payload)
        
        ResponseValidator.assert_status_code(response, 201)
        created_user = ResponseValidator.assert_schema(response, UserResponseModel)
        
        assert created_user.name == payload.name
        assert created_user.email == payload.email
        assert created_user.id is not None

    def test_create_user_with_dict_payload(self, user_endpoint: UserEndpoint):
        """Verify POST /users creates user successfully using dictionary payload."""
        response = user_endpoint.create_user(VALID_USER_DICT_PAYLOAD)
        
        ResponseValidator.assert_status_code(response, 201)
        ResponseValidator.assert_json_value(response, "name", VALID_USER_DICT_PAYLOAD["name"])

    @pytest.mark.regression
    def test_update_user_full_put(self, user_endpoint: UserEndpoint):
        """Verify PUT /users/{id} replaces user details."""
        user_id = 1
        update_payload = {
            "name": "Updated John Doe",
            "username": "johndoe_updated",
            "email": "john.updated@example.com",
        }
        response = user_endpoint.update_user(user_id, update_payload)
        
        ResponseValidator.assert_status_code(response, 200)
        ResponseValidator.assert_json_value(response, "name", update_payload["name"])

    @pytest.mark.regression
    def test_patch_user_partial(self, user_endpoint: UserEndpoint):
        """Verify PATCH /users/{id} updates partial user attributes."""
        user_id = 1
        patch_payload = {"email": "new.patch.email@example.com"}
        response = user_endpoint.patch_user(user_id, patch_payload)
        
        ResponseValidator.assert_status_code(response, 200)
        ResponseValidator.assert_json_value(response, "email", patch_payload["email"])

    def test_delete_user_success(self, user_endpoint: UserEndpoint):
        """Verify DELETE /users/{id} removes the target user."""
        user_id = 1
        response = user_endpoint.delete_user(user_id)
        
        ResponseValidator.assert_status_code(response, [200, 204])

    @pytest.mark.regression
    def test_api_performance_latency(self, user_endpoint: UserEndpoint):
        """Verify response time for fetching users is under 3000 ms."""
        response = user_endpoint.get_all_users()
        ResponseValidator.assert_response_time_under(response, 3000)
