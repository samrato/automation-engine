"""
Task: API Health Check
Description: Sends a request to a health endpoint and verifies the status.
"""

from core.logger import logger
from engine import register_task


@register_task(
    name="health",
    category="api",
    description="Checks the health of a target API and logs status code and latency.",
)
def check_api_health(url: str):
    """
    Student Task:
    1. Send a GET request to the target URL.
    2. Measure the response time (latency).
    3. Check if the status code is 200 OK.
    4. Log the health status (healthy / unhealthy) along with response code and latency.
    5. Return a dictionary containing health status info.
    """
    logger.info(f"Checking health for: {url}")
    raise NotImplementedError("Student Task: Implement check_api_health() in automations/api/health.py")
