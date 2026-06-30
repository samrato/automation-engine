"""
Task: API Data Fetcher
Description: Fetches JSON data from an endpoint and saves it locally.
"""

from core.logger import logger
from engine import register_task


@register_task(
    name="fetch",
    category="api",
    description="Fetches data from a REST endpoint and saves it to a JSON file.",
)
def fetch_api_data(endpoint: str, output_filename: str):
    """
    Student Task:
    1. Instantiate BaseAPIClient or perform a direct requests/httpx get call.
    2. Retrieve json data.
    3. Save the retrieved data as a JSON file in the output folder.
    4. Handle timeouts and status code exceptions.
    5. Return the count of records fetched or success flag.
    """
    logger.info(f"Fetching data from endpoint: {endpoint} -> {output_filename}")
    raise NotImplementedError("Student Task: Implement fetch_api_data() in automations/api/fetch.py")
