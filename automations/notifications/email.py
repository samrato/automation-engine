"""
Task: Email Alert Dispatcher
Description: Wrapper task to trigger SMTP alert notifications.
"""

from core.logger import logger
from engine import register_task


@register_task(
    name="email",
    category="notifications",
    description="Sends system email alerts to administrators.",
)
def send_email_alert(subject: str, message: str, alert_level: str = "INFO"):
    """
    Student Task:
    1. Import `send_email` from the automations.email.sender module.
    2. Format the message body with alert_level (e.g. prefixing [ALERT: WARNING]).
    3. Retrieve the administrator emails from settings.
    4. Call send_email with admin recipient and formatted body.
    5. Return status boolean.
    """
    logger.info(f"Preparing Email alert [{alert_level}]: {subject}")
    raise NotImplementedError("Student Task: Implement send_email_alert() in automations/notifications/email.py")
