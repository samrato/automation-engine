"""
Task: Git Commit
Description: Automates staging changes and committing them.
"""

from core.logger import logger
from engine import register_task


@register_task(
    name="commit",
    category="git",
    description="Stages changes and commits them with a standard message.",
)
def git_commit(repo_path: str, message: str):
    """
    Student Task:
    1. Import the GitPython package: `import git`.
    2. Open the repository: `repo = git.Repo(repo_path)`.
    3. Stage files: `repo.index.add('*')` or list of files.
    4. Commit: `repo.index.commit(message)`.
    5. Log status and hash of the new commit.
    6. Return commit hash.
    """
    logger.info(f"Staging and committing files in '{repo_path}' with message: {message}")
    raise NotImplementedError("Student Task: Implement git_commit() in automations/git/commit.py")
