"""
Task: Log/Temp Cleanup
Description: Deletes files older than a specified number of days in a target directory.
"""

from core.logger import logger
from engine import register_task


@register_task(
    name="cleanup",
    category="files",
    description="Deletes files in a directory that are older than X days.",
)
def cleanup_files(directory_path: str, days: int = 30):
    """
    Student Task:
    1. Validate if directory_path exists.
    2. Check the creation/modification time of each file in the directory.
    3. If the file is older than the given days threshold, delete it.
    4. Guard against deleting critical directories/files.
    5. Log the names of deleted files.
    6. Return the count of deleted files and total space freed.
    """
    logger.info(f"Cleaning up files in {directory_path} older than {days} days...")
    raise NotImplementedError("Student Task: Implement cleanup_files() in automations/files/cleanup.py")
