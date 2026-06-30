"""
Task: Excel Report Automation
Description: Generates high-level summaries and charts in an Excel sheet.
"""

from core.logger import logger
from engine import register_task


@register_task(
    name="excel",
    category="reports",
    description="Generates complex formatted reports inside Excel files with styles.",
)
def export_excel_report(data_source: str, output_file: str):
    """
    Student Task:
    1. Read inputs from data_source (JSON/CSV).
    2. Format tables and headers inside a new Excel sheet.
    3. Generate custom charts (bar/pie) using openpyxl.chart modules.
    4. Save output to output_file.
    """
    logger.info(f"Exporting Excel report from {data_source} to {output_file}")
    raise NotImplementedError("Student Task: Implement export_excel_report() in automations/reports/excel.py")
