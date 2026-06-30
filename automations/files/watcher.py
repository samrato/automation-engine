"""
Task: Folder Watcher
Description: Watches a directory for new files using python-watchdog and logs their addition.
"""

from core.logger import logger
from engine import register_task


@register_task(
    name="watch",
    category="files",
    description="Starts a directory watcher that logs file creation events in real-time.",
)
def watch_directory(directory_path: str):
    """
    Student Task:
    1. Import `watchdog.observers` and `watchdog.events`.
    2. Write a custom event handler that logs when a new file is created.
    3. Initialize the observer to watch directory_path.
    4. Start the observer and run it in a loop (using a try/except block to catch KeyboardInterrupt).
    5. Ensure proper resource cleanup when stopping.
    """
    logger.info(f"Setting up directory watcher on {directory_path}...")
    raise NotImplementedError("Student Task: Implement watch_directory() in automations/files/watcher.py")
