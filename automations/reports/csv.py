"""
Task: CSV Report Generator
Description: Aggregates and dumps clean datasets to CSV format.
"""

from core.logger import logger
from engine import register_task


@register_task(
    name="csv",
    category="reports",
    description="Aggregates unstructured JSON logs/records and outputs a structured CSV file.",
)
def export_csv_report(input_file: str, output_file: str):
    """
    Student Task:
    1. Read input data from input_file (JSON or raw records).
    2. Normalize nested objects or clean missing values.
    3. Write the clean headers and rows to output_file using python's csv module or pandas.
    4. Log file size and row counts.
    """
    logger.info(f"Generating CSV report: {input_file} -> {output_file}")
    raise NotImplementedError("Student Task: Implement export_csv_report() in automations/reports/csv.py")
