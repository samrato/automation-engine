"""
Task: Docker Run
Description: Runs a specified Docker container with ports and environment variables.
"""

from typing import Dict

from core.logger import logger
from engine import register_task


@register_task(
    name="run",
    category="docker",
    description="Starts a docker container with environment variables and port mapping.",
)
def run_container(
    image_tag: str,
    container_name: str,
    environment: Dict[str, str] = None,
    ports: Dict[str, int] = None,
):
    """
    Student Task:
    1. Initialize the docker client using `docker.from_env()`.
    2. Call client.containers.run(image_tag, name=container_name, detach=True, environment=environment, ports=ports).
    3. Log the status and container ID.
    4. Return the container metadata.
    """
    logger.info(f"Running Docker image '{image_tag}' as '{container_name}'...")
    raise NotImplementedError("Student Task: Implement run_container() in automations/docker/run.py")
