from models.user_model import CreateUserRequest
from utils.helpers import HelperUtils


def get_random_user_payload() -> CreateUserRequest:
    """Returns a dynamic CreateUserRequest model populated with random data."""
    random_str = HelperUtils.generate_random_string(6).capitalize()
    return CreateUserRequest(
        name=f"Test User {random_str}",
        username=f"user_{random_str.lower()}",
        email=HelperUtils.generate_random_email(),
        phone=HelperUtils.generate_random_phone(),
        website=f"https://{random_str.lower()}.org",
    )


VALID_USER_DICT_PAYLOAD = {
    "name": "Jane Doe",
    "username": "janedoe",
    "email": "janedoe@example.com",
    "phone": "1-800-555-0199",
    "website": "janedoe.com",
}
