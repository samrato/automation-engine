"""
Domain-specific helper functions for the Automation Engine.
Unlike general utilities in utils.py, helpers.py contains functions tied
to the automation domain, such as generating standardized task reports,
formatting notification payloads, or parsing path arguments.
"""


def generate_standard_report_filename(category: str, task_name: str, extension: str = "json") -> str:
    """
    Generate a standardized timestamped report filename.
    Example: files_organizer_20260630_110000.json
    """
    import datetime

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # Clean the inputs
    clean_cat = category.lower().replace(" ", "_")
    clean_task = task_name.lower().replace(" ", "_")
    return f"{clean_cat}_{clean_task}_{timestamp}.{extension}"
