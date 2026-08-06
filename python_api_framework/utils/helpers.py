import random
import string
from datetime import datetime


class HelperUtils:
    """Helper utilities for test data generation."""

    @staticmethod
    def generate_random_string(length: int = 8) -> str:
        """Generates a random string of lowercase letters."""
        return "".join(random.choices(string.ascii_lowercase, k=length))

    @staticmethod
    def generate_random_email(domain: str = "example.com") -> str:
        """Generates a unique random email address."""
        username = HelperUtils.generate_random_string(8)
        timestamp = datetime.now().strftime("%H%M%S")
        return f"user_{username}_{timestamp}@{domain}"

    @staticmethod
    def generate_random_phone() -> str:
        """Generates a random 10-digit phone number."""
        num = "".join(random.choices(string.digits, k=9))
        return f"1-{num[:3]}-{num[3:6]}-{num[6:]}"
