"""
Task: Email Sender
Description: Sends SMTP emails with support for HTML and attachments.
"""

from typing import List, Optional

from core.logger import logger
from engine import register_task


@register_task(
    name="send",
    category="email",
    description="Sends an email via SMTP to one or more recipients with optional attachment.",
)
def send_email(
    to_email: str,
    subject: str,
    body: str,
    is_html: bool = False,
    attachments: Optional[List[str]] = None,
):
    """
    Student Task:
    1. Import smtplib, MIMEText, MIMEMultipart, and MIMEApplication.
    2. Get SMTP configuration from config.settings (host, port, username, password).
    3. Build the email message body (plain text or HTML).
    4. Attach any specified files.
    5. Establish a secure SMTP connection (SSL or TLS starttls).
    6. Send the email and close connection.
    7. Return status boolean.
    """
    logger.info(f"Preparing email for: {to_email} with subject: {subject}")
    raise NotImplementedError("Student Task: Implement send_email() in automations/email/sender.py")
