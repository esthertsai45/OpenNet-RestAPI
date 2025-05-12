import logging
from enum import Enum
from typing import Any, Optional

import requests

logger = logging.getLogger(__name__)


class RequestMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    PATCH = "PATCH"
    PUT = "PUT"


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def _send_request(
        self,
        method: RequestMethod,
        uri: str,
        headers: dict[str, str] = {"Content-Type": "application/json"},
        params: dict[str, str] = {},
        json: Optional[dict[str, Any]] = None,
        timeout: int = 10,
    ) -> requests.Response:

        url = f"{self.base_url}{uri}"
        logger.warning(f"request URL is: {url}")

        res = requests.request(
            method=method.value,
            url=url,
            headers=headers,
            timeout=timeout,
            params=params,
            json=json,
        )

        logger.warning(res.text)

        return res
