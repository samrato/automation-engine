"""
Task: File Organizer
Description: Organizes files in a target directory by sorting them into subfolders based on extension.
"""

from core.logger import logger
from engine import register_task


@register_task(
    name="organize",
    category="files",
    description="Organizes files in a directory into folders by type (e.g. Documents, Images, Archives).",
)
def organize_directory(directory_path: str):
    """
    Student Task:
    1. Validate if directory_path exists.
    2. Iterate through all files in the target directory (non-recursive or recursive).
    3. Determine the file type based on extension (e.g., '.pdf' -> 'Documents', '.zip' -> 'Archives').
    4. Create the corresponding subfolders if they don't exist.
    5. Move the files into their respective subfolders.
    6. Log and return the number of files moved.
    """
    logger.info(f"Target directory for organization: {directory_path}")
    raise NotImplementedError("Student Task: Implement organize_directory() in automations/files/organizer.py")
