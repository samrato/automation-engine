import time
from functools import wraps
from typing import Any, Callable

from core.logger import logger


def measure_time(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator that measures and logs the execution time of an automation task.
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        logger.info(f"Starting task [bold cyan]{func.__name__}[/bold cyan]...")
        try:
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start_time
            logger.info(f"Task [bold green]{func.__name__}[/bold green] completed successfully in {elapsed:.4f}s.")
            return result
        except Exception as e:
            elapsed = time.perf_counter() - start_time
            logger.error(
                f"Task [bold red]{func.__name__}[/bold red] failed after {elapsed:.4f}s with error: {e}",
                exc_info=True,
            )
            raise e

    return wrapper


def format_size(bytes_count: int) -> str:
    """Format size in bytes to a human-readable string (e.g. KB, MB)."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if bytes_count < 1024.0:
            return f"{bytes_count:.2f} {unit}"
        bytes_count /= 1024.0
    return f"{bytes_count:.2f} PB"
