"""
Task: Docker Build
Description: Builds a Docker image from a local path containing a Dockerfile.
"""

from core.logger import logger
from engine import register_task


@register_task(
    name="build",
    category="docker",
    description="Builds a docker image from a specified build context containing a Dockerfile.",
)
def build_image(path: str, tag: str):
    """
    Student Task:
    1. Import the `docker` SDK package.
    2. Initialize a client with `docker.from_env()`.
    3. Call the client's images build method: client.images.build(path=path, tag=tag).
    4. Stream build logs and print/log them.
    5. Return the image ID.
    """
    logger.info(f"Building Docker image in path: {path} with tag: {tag}")
    raise NotImplementedError("Student Task: Implement build_image() in automations/docker/build.py")
