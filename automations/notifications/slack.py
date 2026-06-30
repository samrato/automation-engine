"""
Task: Slack Notifier
Description: Dispatches alerts and summaries to a Slack channel using webhooks or client SDK.
"""

from core.logger import logger
from engine import register_task


@register_task(
    name="slack",
    category="notifications",
    description="Sends notification messages and blocks payloads to a Slack channel.",
)
def send_slack_notification(message: str, channel: str = None, blocks: list = None):
    """
    Student Task:
    1. Retrieve the slack webhook URL or client API token from settings.
    2. Construct request payload (text message or rich blocks).
    3. Send POST request to Slack webhook endpoint using requests/httpx
       OR initialize Slack WebClient and use chat_postMessage.
    4. Handle API error responses.
    5. Return status boolean.
    """
    logger.info(f"Preparing Slack notification: {message}")
    raise NotImplementedError("Student Task: Implement send_slack_notification() in automations/notifications/slack.py")
