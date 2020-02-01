import requests
from typing import Tuple


class Post:
    def __init__(self, url: str, sanitized_string: str) -> None:
        self.success, self.response = self._send_request(url, sanitized_string)

    @staticmethod
    def _send_request(url: str, string: str) -> Tuple[bool, str]:
        response = requests.post(url, string)
        print(response)
        return (True, response.text) if response else (False, str(response.status_code))
