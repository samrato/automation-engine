"""
Task: Scheduler Job Runner
Description: Runs pre-defined runner routines periodically.
"""

from core.logger import logger
from engine import register_task


def sample_job():
    """A dummy job that logs a heartbeat message."""
    logger.info("[Scheduler Heartbeat] Performing scheduled maintenance...")


@register_task(
    name="run_jobs",
    category="scheduler",
    description="Runs tasks periodically as defined in the scheduling module.",
)
def run_jobs_loop(interval_seconds: int = 10):
    """
    Student Task:
    1. Import the `schedule` library.
    2. Register `sample_job` (or other tasks) to run at the given interval_seconds.
    3. Start an infinite loop that calls `schedule.run_pending()` and sleeps.
    4. Implement clean shutdown handling (e.g. catch KeyboardInterrupt).
    """
    logger.info(f"Starting scheduler loop. Running jobs every {interval_seconds} seconds...")
    raise NotImplementedError("Student Task: Implement run_jobs_loop() in automations/scheduler/jobs.py")
