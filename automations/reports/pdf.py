"""
Task: PDF Report Generator
Description: Builds formatted PDF report summaries using ReportLab.
"""

from core.logger import logger
from engine import register_task


@register_task(
    name="pdf",
    category="reports",
    description="Generates styled PDF files with tables, headers, and logs using ReportLab.",
)
def export_pdf_report(title: str, content_lines: list[str], output_file: str):
    """
    Student Task:
    1. Import ReportLab elements (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle).
    2. Define a standard styling stylesheet (e.g. from reportlab.lib.styles).
    3. Construct PDF flowables containing title, date, logs list table, and footer.
    4. Build the document template to output_file.
    5. Return path of the generated PDF.
    """
    logger.info(f"Generating PDF report: '{title}' -> {output_file}")
    raise NotImplementedError("Student Task: Implement export_pdf_report() in automations/reports/pdf.py")
