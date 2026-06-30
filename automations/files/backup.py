"""
Task: Folder Backup
Description: Creates a compressed zip backup of a directory and saves it to a backup location.
"""

from core.logger import logger
from engine import register_task


@register_task(
    name="backup",
    category="files",
    description="Compresses a folder into a ZIP archive and saves it to a destination folder.",
)
def backup_folder(source_dir: str, dest_dir: str):
    """
    Student Task:
    1. Validate source and destination directories.
    2. Generate a backup filename with a timestamp (e.g., backup_20260630_110000.zip).
    3. Use the zipfile module to compress all contents of source_dir into the archive.
    4. Save the archive to dest_dir.
    5. Log the size of the generated zip file.
    6. Return a dictionary containing the path to the backup file and its size.
    """
    logger.info(f"Backing up directory: {source_dir} to {dest_dir}")
    raise NotImplementedError("Student Task: Implement backup_folder() in automations/files/backup.py")
