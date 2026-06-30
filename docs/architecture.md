# System Architecture

This document describes the structure and design choices of the **Automation Engine** platform.

## Overview

The Automation Engine is designed as a modular, extensible command-line platform. It aims to let students and developers write small, self-contained automation tasks in Python without worrying about CLI routing, environment settings loading, formatting, logging, or error wrapping.

```mermaid
graph TD
    CLI[cli.py - Typer] -->|discovers & runs| Engine[engine.py - Registry]
    Main[main.py] --> CLI
    Engine -->|imports| Automs[automations/ submodules]
    Automs -->|register via| Dec[@register_task]
    Engine -->|uses| Core[core/ utilities, logger, exceptions]
    Core --> Config[config.py - Env load]
```

## Core Components

### 1. The Entrypoint (`main.py` & `cli.py`)
- `main.py` is the application entrypoint.
- `cli.py` uses [Typer](https://typer.tiangolo.com/) and [Rich](https://rich.readthedocs.io/) to structure CLI commands.
- It exposes a `list` command (rendering registered tasks as a Rich table) and a `run` command.

### 2. Task Discovery and Execution (`engine.py`)
- Contains a global `_TASK_REGISTRY` dict.
- Exposes a decorator `@register_task(name, category, description)` which registers functions into the registry.
- `AutomationEngine.discover_tasks()` dynamically walks and imports all Python packages inside the `automations/` folder, prompting the `@register_task` decorators to register their functions.
- `AutomationEngine.execute_task(category, name, *args, **kwargs)` fetches the target function, wraps it inside execution metrics (timing and logger output), and runs it.

### 3. Settings Management (`config.py`)
- Utilizes `python-dotenv` to look up configurations inside a `.env` file.
- Provides standard defaults for local running and auto-creates input/output/logs folders on startup.

### 4. Logging & Utilities (`core/`)
- `logger.py`: Combines rich stdout console stream with a daily rotating file logger inside `logs/app.log`.
- `utils.py`: Provides helper wrappers such as `@measure_time` to auto-log performance data.
- `exceptions.py`: Standardizes errors (`TaskNotFoundError`, `TaskExecutionError`, etc.) to prevent engine crashes.

## Extending the Platform
To add a new automation capability:
1. Identify the domain (e.g. `automations/files/` or create a new directory sub-package like `automations/mlops/`).
2. If creating a new subdirectory, make sure it has an `__init__.py`.
3. Create a python file, import `register_task` from `engine`, and apply it to your handler function.
4. The CLI will automatically display and run the new command.
