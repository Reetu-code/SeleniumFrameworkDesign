import json
import time
from typing import Any, Dict, Optional
import requests
from requests import Response

from config.config import Config, config as default_config
from core.logger import logger


class APIClient:
    """Wrapper around requests.Session providing logging, timing, and error management."""

    def __init__(self, cfg: Optional[Config] = None):
        self.config = cfg or default_config
        self.session = requests.Session()
        self.session.headers.update(self.config.default_headers)

    def request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Any] = None,
        json_data: Optional[Any] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[int] = None,
        **kwargs,
    ) -> Response:
        """Executes an HTTP request with automatic logging and latency tracking."""
        url = endpoint if endpoint.startswith("http") else f"{self.config.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        request_timeout = timeout or self.config.timeout

        # Merge headers if custom headers passed
        req_headers = dict(self.session.headers)
        if headers:
            req_headers.update(headers)

        # Log Request details
        logger.info(f"===> REQUEST: [{method.upper()}] {url}")
        if params:
            logger.info(f"Params: {params}")
        if req_headers:
            # Mask authorization header token in logs
            masked_headers = {
                k: ("***" if k.lower() == "authorization" else v)
                for k, v in req_headers.items()
            }
            logger.info(f"Headers: {masked_headers}")
        if json_data:
            logger.info(f"Payload (JSON): {json.dumps(json_data, indent=2)}")
        elif data:
            logger.info(f"Payload (Data): {data}")

        start_time = time.perf_counter()
        try:
            response = self.session.request(
                method=method.upper(),
                url=url,
                params=params,
                data=data,
                json=json_data,
                headers=req_headers,
                timeout=request_timeout,
                **kwargs,
            )
            duration_ms = round((time.perf_counter() - start_time) * 1000, 2)
            
            # Log Response details
            logger.info(f"<=== RESPONSE: [{response.status_code}] ({duration_ms} ms) URL: {response.url}")
            
            try:
                resp_json = response.json()
                # Truncate very large responses for cleaner logs
                json_str = json.dumps(resp_json, indent=2)
                if len(json_str) > 1000:
                    logger.info(f"Response Body (truncated): {json_str[:1000]}...\n[Total length: {len(json_str)} chars]")
                else:
                    logger.info(f"Response Body: {json_str}")
            except ValueError:
                logger.info(f"Response Content (non-JSON): {response.text[:500]}")

            return response

        except requests.exceptions.RequestException as exc:
            duration_ms = round((time.perf_counter() - start_time) * 1000, 2)
            logger.error(f"HTTP Request failed after {duration_ms} ms: {exc}")
            raise

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None, **kwargs) -> Response:
        return self.request("GET", endpoint, params=params, **kwargs)

    def post(self, endpoint: str, json_data: Optional[Any] = None, **kwargs) -> Response:
        return self.request("POST", endpoint, json_data=json_data, **kwargs)

    def put(self, endpoint: str, json_data: Optional[Any] = None, **kwargs) -> Response:
        return self.request("PUT", endpoint, json_data=json_data, **kwargs)

    def patch(self, endpoint: str, json_data: Optional[Any] = None, **kwargs) -> Response:
        return self.request("PATCH", endpoint, json_data=json_data, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> Response:
        return self.request("DELETE", endpoint, **kwargs)
