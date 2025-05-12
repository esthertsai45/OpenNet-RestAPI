import logging

from module.base import ApiClient, RequestMethod

logger = logging.getLogger(__name__)


class Mail(ApiClient):
    uri = "/api/email"

    def __init__(self, base_url: str, headers: dict = {}):
        super().__init__(base_url)
        self.headers = headers

    def verify_email(self, email: str):
        return self._send_request(
            uri=f"{self.uri}/{email}", method=RequestMethod.GET, headers=self.headers
        )
