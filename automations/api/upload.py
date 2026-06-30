"""
Task: API Data Uploader
Description: Reads a local file and uploads its contents to a remote endpoint.
"""

from core.logger import logger
from engine import register_task


@register_task(
    name="upload",
    category="api",
    description="Reads a JSON or CSV file and POSTs its payload to a remote API.",
)
def upload_data(file_path: str, endpoint: str):
    """
    Student Task:
    1. Read the input file (JSON, CSV, or raw text).
    2. Format the payload for the request.
    3. Make a POST request with the file data/payload.
    4. Handle response errors and log the server output.
    5. Return the HTTP status code.
    """
    logger.info(f"Uploading file {file_path} to endpoint: {endpoint}")
    raise NotImplementedError("Student Task: Implement upload_data() in automations/api/upload.py")
