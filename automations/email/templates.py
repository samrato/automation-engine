"""
Task: Email Template Manager
Description: Loads HTML templates and replaces placeholders with dynamic variables.
"""

from typing import Any, Dict


def render_template(template_name: str, context: Dict[str, Any]) -> str:
    """
    Student Task:
    1. Read the corresponding HTML template file (e.g. templates/alerts.html).
    2. Replace placeholders in the template using python's string.Template,
       jinja2 (if installed), or simple .format() / .replace().
    3. Return the fully rendered HTML string.

    Hint: Keep some default fallback template strings directly in code.
    """
    raise NotImplementedError("Student Task: Implement render_template() in automations/email/templates.py")
