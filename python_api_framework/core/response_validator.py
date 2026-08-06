from typing import Any, Dict, List, Type, Union
from pydantic import BaseModel, ValidationError
from requests import Response
from core.logger import logger


class ResponseValidator:
    """Helper methods for asserting response code, schema, performance, and contents."""

    @staticmethod
    def assert_status_code(response: Response, expected_status: Union[int, List[int]]) -> Response:
        """Asserts response status code matches expected status."""
        expected_list = [expected_status] if isinstance(expected_status, int) else expected_status
        actual_status = response.status_code
        
        assert actual_status in expected_list, (
            f"Status code mismatch! Expected: {expected_list}, Got: {actual_status}. "
            f"Response Body: {response.text[:300]}"
        )
        logger.info(f"✔ Status code verified: {actual_status}")
        return response

    @staticmethod
    def assert_schema(response: Response, model: Type[BaseModel]) -> Union[BaseModel, List[BaseModel]]:
        """Asserts response JSON matches a Pydantic model schema."""
        try:
            data = response.json()
        except ValueError:
            raise AssertionError(f"Response is not valid JSON. Content: {response.text[:300]}")

        try:
            if isinstance(data, list):
                validated_data = [model.model_validate(item) for item in data]
                logger.info(f"✔ Validated {len(validated_data)} items against model '{model.__name__}'")
            else:
                validated_data = model.model_validate(data)
                logger.info(f"✔ Validated response schema against model '{model.__name__}'")
            return validated_data
        except ValidationError as e:
            logger.error(f"Schema Validation Failed for {model.__name__}:\n{e}")
            raise AssertionError(f"Response schema validation failed for {model.__name__}:\n{e}")

    @staticmethod
    def assert_json_value(response: Response, key_path: str, expected_value: Any) -> Response:
        """
        Asserts a nested JSON key matches expected_value.
        Example key_path: 'address.city' or 'id'
        """
        data = response.json()
        keys = key_path.split(".")
        current = data
        for k in keys:
            if isinstance(current, dict) and k in current:
                current = current[k]
            elif isinstance(current, list) and k.isdigit():
                current = current[int(k)]
            else:
                raise KeyError(f"Key path '{key_path}' (failed at '{k}') not found in response: {data}")

        assert current == expected_value, (
            f"Value mismatch for key '{key_path}'! Expected: {expected_value}, Got: {current}"
        )
        logger.info(f"✔ Key '{key_path}' verified equal to '{expected_value}'")
        return response

    @staticmethod
    def assert_response_time_under(response: Response, max_milliseconds: float) -> Response:
        """Asserts that response latency is below specified threshold."""
        elapsed_ms = response.elapsed.total_seconds() * 1000
        assert elapsed_ms <= max_milliseconds, (
            f"Response time too slow! Expected <= {max_milliseconds} ms, Got: {elapsed_ms:.2f} ms"
        )
        logger.info(f"✔ Response time verified: {elapsed_ms:.2f} ms <= {max_milliseconds} ms")
        return response
