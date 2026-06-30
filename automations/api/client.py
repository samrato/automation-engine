"""
Base HTTP API Client
Provides a class structure for students to build custom API requests.
"""

from config import settings
from core.logger import logger


class BaseAPIClient:
    """
    Student Task:
    1. Implement initializer that configures headers (e.g. Auth Tokens) and baseUrl.
    2. Implement methods for GET, POST, PUT, DELETE with error handling and retries.
    3. Use requests or httpx to send requests.
    """

    def __init__(self, base_url: str | None = None, api_key: str | None = None):
        self.base_url = base_url or settings.EXTERNAL_API_URL
        self.api_key = api_key or settings.EXTERNAL_API_KEY
        logger.info(f"Initialized API Client targeting: {self.base_url}")

    def request(self, method: str, endpoint: str, **kwargs) -> dict:
        """Sends an HTTP request and parses json response."""
        raise NotImplementedError("Student Task: Implement request() in automations/api/client.py")
