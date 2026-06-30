"""
Task: Docker Cleanup
Description: Stops and removes stopped containers and deletes dangling images.
"""

from core.logger import logger
from engine import register_task


@register_task(
    name="cleanup",
    category="docker",
    description="Prunes stopped containers, unused networks, and dangling volumes/images.",
)
def docker_cleanup(unused_images: bool = True):
    """
    Student Task:
    1. Initialize the docker client using `docker.from_env()`.
    2. Retrieve all stopped containers and remove them.
    3. If unused_images is True, clean up dangling images (e.g. using client.images.prune()).
    4. Log the amount of containers/images cleaned up.
    5. Return counts of removed resources.
    """
    logger.info("Executing Docker cleanup operations...")
    raise NotImplementedError("Student Task: Implement docker_cleanup() in automations/docker/cleanup.py")
