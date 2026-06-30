"""
Task: Scheduler Customizer
Description: Registers complex scheduler patterns (e.g. daily at 10:00, Mondays only).
"""

from core.logger import logger
from engine import register_task


@register_task(
    name="schedule",
    category="scheduler",
    description="Schedules a task to run at complex intervals (e.g., every Monday, daily at 10 AM).",
)
def configure_complex_schedule(task_name: str, interval: str, time_of_day: str = None):
    """
    Student Task:
    1. Resolve task_name against the AutomationEngine task registry.
    2. Setup job scheduling based on 'interval' (e.g., 'daily', 'weekly', 'hourly').
    3. If time_of_day is provided and interval is 'daily' or 'weekly', specify the time (e.g. .at(time_of_day)).
    4. Start the scheduler runner to run the task on schedule.
    """
    logger.info(f"Configuring schedule for '{task_name}': every '{interval}' at '{time_of_day}'")
    raise NotImplementedError(
        "Student Task: Implement configure_complex_schedule() in automations/scheduler/schedule.py"
    )
