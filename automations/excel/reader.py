"""
Task: Excel Reader
Description: Reads data from an Excel workbook (.xlsx) and parses it.
"""

from core.logger import logger
from engine import register_task


@register_task(
    name="read",
    category="excel",
    description="Reads data from a sheet in an Excel workbook and prints/logs summaries.",
)
def read_excel(file_path: str, sheet_name: str = "Sheet1"):
    """
    Student Task:
    1. Open the Excel workbook at file_path using openpyxl or pandas.
    2. Check if the specified sheet_name exists.
    3. Read row data and convert it into a dictionary list or pandas DataFrame.
    4. Log the count of rows and columns found.
    5. Return the parsed records as a list of dicts.
    """
    logger.info(f"Reading excel sheet '{sheet_name}' from: {file_path}")
    raise NotImplementedError("Student Task: Implement read_excel() in automations/excel/reader.py")
