"""
Task: Git Status
Description: Checks the local git workspace status (untracked, modified, staged files).
"""

from core.logger import logger
from engine import register_task


@register_task(
    name="status",
    category="git",
    description="Gets the repository status, listing modified, untracked, or staged files.",
)
def git_status(repo_path: str):
    """
    Student Task:
    1. Open the repository at repo_path.
    2. Check if the repo is dirty (has changes): repo.is_dirty().
    3. Retrieve lists of untracked files, modified files, and staged files.
    4. Log the state summary.
    5. Return a dictionary containing counts and file paths for each state.
    """
    logger.info(f"Checking Git status for repository at: {repo_path}")
    raise NotImplementedError("Student Task: Implement git_status() in automations/git/status.py")
