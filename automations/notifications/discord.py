"""
Task: Discord Notifier
Description: Dispatches alerts to a Discord channel using webhooks.
"""

from core.logger import logger
from engine import register_task


@register_task(
    name="discord",
    category="notifications",
    description="Sends notification messages and embeds to a Discord channel via webhook.",
)
def send_discord_notification(message: str, username: str = "AutomationBot", embeds: list = None):
    """
    Student Task:
    1. Retrieve the discord webhook URL from settings.
    2. Construct request payload with content message, custom username, and optional embeds.
    3. Send POST request to Discord webhook endpoint using requests/httpx.
    4. Validate status code.
    5. Return status boolean.
    """
    logger.info(f"Preparing Discord notification: {message}")
    raise NotImplementedError(
        "Student Task: Implement send_discord_notification() in automations/notifications/discord.py"
    )
