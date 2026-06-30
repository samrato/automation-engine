"""
Task: Excel Report Generator
Description: Generates formatted Excel pivot table report summaries from raw sheet data.
"""

from core.logger import logger
from engine import register_task


@register_task(
    name="reports",
    category="excel",
    description="Processes raw transaction/sales data in Excel to output formatted summary sheets.",
)
def generate_excel_reports(source_file: str, dest_file: str):
    """
    Student Task:
    1. Read raw transactional data from source_file using pandas.
    2. Perform aggregation or grouping (e.g., sum of sales per region or category).
    3. Load the summary data into a new worksheet in dest_file.
    4. Apply conditional formatting, styles, and headers using openpyxl.
    5. Save the file.
    """
    logger.info(f"Generating aggregated excel report from {source_file} to {dest_file}")
    raise NotImplementedError("Student Task: Implement generate_excel_reports() in automations/excel/reports.py")
