# API Reference & Extending Tasks

This reference manual documents the programmatic API and decoration structures for registering automation tasks.

## The `@register_task` Decorator

All automation tasks must use the `@register_task` decorator defined in `engine.py`. This registration enables dynamic discovery.

### Signature

```python
def register_task(name: str, category: str, description: str = ""):
    ...
```

- **`name`**: The unique string ID of the task within its category (e.g. `organize`, `backup`).
- **`category`**: The directory prefix/namespace category (e.g. `files`, `api`, `docker`). This corresponds to the submodule folder structure.
- **`description`**: A short sentence describing what the task does. If omitted, the decorator falls back to the function's docstring.

### Standard Template

Use this template when writing any new automation:

```python
from engine import register_task
from core.logger import logger
from config import settings

@register_task(
    name="my_action",
    category="my_category",
    description="Does something useful."
)
def run_action(param1: str, param2: int = 10):
    """
    Optional details about the function logic.
    """
    logger.info(f"Running action with {param1} and {param2}")
    
    # Custom business logic goes here
    
    return {"status": "success", "processed": param1}
```

## Global Configuration Object

Use `config.settings` to access environment configurations securely:

```python
from config import settings

# Access SMTP variables
smtp_host = settings.SMTP_HOST

# Access Input/Output directories
input_dir = settings.DATA_INPUT_DIR
```

Do not access environment variables directly via `os.environ` or `os.getenv` within tasks. Define them in `config.py` first, then pull from `settings` to ensure uniform configurations across all student scripts.
