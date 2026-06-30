import importlib
import pkgutil
from typing import Any, Callable, Dict, List

from core.exceptions import TaskExecutionError, TaskNotFoundError
from core.logger import logger
from core.utils import measure_time

# Registry for tasks. Key format: "category:task_name"
_TASK_REGISTRY: Dict[str, Dict[str, Any]] = {}


def register_task(name: str, category: str, description: str = ""):
    """
    Decorator to register a function as an automation task.

    Usage:
        @register_task(name="cleanup_downloads", category="files", description="Cleans temporary files.")
        def my_task(days: int = 7):
            ...
    """

    def decorator(func: Callable[..., Any]):
        registry_key = f"{category}:{name}"
        _TASK_REGISTRY[registry_key] = {
            "name": name,
            "category": category,
            "description": description or func.__doc__ or "No description provided.",
            "func": func,
        }
        return func

    return decorator


class AutomationEngine:
    """
    Task loader and execution engine.
    Dynamically loads task modules and manages execution.
    """

    def __init__(self, automations_package_name: str = "automations"):
        self.package_name = automations_package_name

    def discover_tasks(self) -> None:
        """
        Dynamically imports all modules within the automations package
        to trigger task registration decorators.
        """
        logger.debug(f"Starting task discovery in '{self.package_name}' package...")
        try:
            package = importlib.import_module(self.package_name)
        except ImportError as e:
            logger.error(f"Failed to import base package '{self.package_name}': {e}")
            return

        # Recursively find and import all sub-modules
        def walk_and_import(pkg):
            for _, name, is_pkg in pkgutil.iter_modules(pkg.__path__, pkg.__name__ + "."):
                try:
                    logger.debug(f"Importing module: {name}")
                    module = importlib.import_module(name)
                    if is_pkg:
                        walk_and_import(module)
                except Exception as e:
                    logger.warning(f"Failed to load module '{name}' during discovery: {e}")

        walk_and_import(package)
        logger.info(f"Task discovery complete. Loaded {len(_TASK_REGISTRY)} tasks.")

    def list_tasks(self) -> List[Dict[str, Any]]:
        """Returns a list of all registered tasks metadata."""
        return [
            {
                "key": key,
                "name": val["name"],
                "category": val["category"],
                "description": val["description"],
            }
            for key, val in _TASK_REGISTRY.items()
        ]

    def get_task(self, category: str, name: str) -> Dict[str, Any]:
        """Retrieve a task from the registry."""
        key = f"{category}:{name}"
        if key not in _TASK_REGISTRY:
            raise TaskNotFoundError(f"Task '{name}' in category '{category}' not found.")
        return _TASK_REGISTRY[key]

    def execute_task(self, category: str, name: str, *args: Any, **kwargs: Any) -> Any:
        """
        Execute a registered task with args and kwargs.
        Applies timing and error handling wrapper automatically.
        """
        task_info = self.get_task(category, name)
        task_func = task_info["func"]

        # Apply execution timer decorator
        timed_func = measure_time(task_func)

        try:
            logger.info(f"Executing task '{category}:{name}'...")
            return timed_func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Failed to execute task '{category}:{name}': {e}")
            raise TaskExecutionError(f"Task execution failed: {e}") from e
