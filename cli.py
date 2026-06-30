from typing import List, Optional

import typer
from rich.console import Console
from rich.table import Table

from core.exceptions import AutomationEngineError
from engine import AutomationEngine

app = typer.Typer(
    name="automation-engine",
    help="CLI for managing and running automation tasks.",
    no_args_is_help=True,
)

console = Console()


def parse_kwargs(args: List[str]) -> dict:
    """Helper to parse extra key=value arguments from CLI."""
    kwargs = {}
    for arg in args:
        if "=" not in arg:
            raise typer.BadParameter(f"Argument '{arg}' must be in key=value format.")
        key, val = arg.split("=", 1)
        # Try casting to basic types
        if val.lower() == "true":
            kwargs[key] = True
        elif val.lower() == "false":
            kwargs[key] = False
        elif val.isdigit():
            kwargs[key] = int(val)
        else:
            try:
                kwargs[key] = float(val)
            except ValueError:
                kwargs[key] = val
    return kwargs


@app.command("list")
def list_tasks():
    """List all registered automation tasks."""
    engine = AutomationEngine()
    engine.discover_tasks()
    tasks = engine.list_tasks()

    if not tasks:
        console.print("[yellow]No tasks registered. Build tasks inside the 'automations' subdirectories![/yellow]")
        return

    table = Table(
        title="Available Automation Tasks",
        show_header=True,
        header_style="bold magenta",
    )
    table.add_column("Category", style="cyan")
    table.add_column("Task Name", style="green")
    table.add_column("Description", style="white")

    for task in tasks:
        table.add_row(task["category"], task["name"], task["description"])

    console.print(table)


@app.command("run")
def run_task(
    category: str = typer.Argument(..., help="Category of the task (e.g. 'files', 'api')"),
    task_name: str = typer.Argument(..., help="Name of the task to run"),
    params: Optional[List[str]] = typer.Argument(
        None, help="Parameters in key=value format (e.g., path=/tmp days=5 verify=true)"
    ),
):
    """
    Run a specific automation task.
    """
    engine = AutomationEngine()
    engine.discover_tasks()

    kwargs = {}
    if params:
        try:
            kwargs = parse_kwargs(params)
        except Exception as e:
            console.print(f"[red]Error parsing parameters:[/red] {e}")
            raise typer.Exit(code=1)

    console.print(f"[bold blue]Initializing task execution: {category}:{task_name}...[/bold blue]")
    try:
        result = engine.execute_task(category, task_name, **kwargs)
        console.print("[bold green]✓ Execution completed successfully.[/bold green]")
        if result is not None:
            console.print("[bold cyan]Result:[/bold cyan]")
            console.print(result)
    except AutomationEngineError as e:
        console.print(f"[bold red]Execution failed:[/bold red] {e}")
        raise typer.Exit(code=1)
    except Exception as e:
        console.print(f"[bold red]Unexpected Error:[/bold red] {e}")
        raise typer.Exit(code=1)


def get_mock_args(func) -> dict:
    import inspect

    sig = inspect.signature(func)
    mock_kwargs = {}
    for name, param in sig.parameters.items():
        if param.default is inspect.Parameter.empty and param.kind in (
            inspect.Parameter.POSITIONAL_OR_KEYWORD,
            inspect.Parameter.KEYWORD_ONLY,
            inspect.Parameter.POSITIONAL_ONLY,
        ):
            anno = param.annotation
            if anno is int:
                mock_kwargs[name] = 0
            elif anno is float:
                mock_kwargs[name] = 0.0
            elif anno is bool:
                mock_kwargs[name] = False
            elif anno in (list, List, list[str], List[str], "list[str]", "List[str]"):
                mock_kwargs[name] = []
            elif anno in (dict, dict[str, str], "dict", "dict[str, str]"):
                mock_kwargs[name] = {}
            else:
                mock_kwargs[name] = "dummy"
    return mock_kwargs


@app.command("run-all")
def run_all_tasks():
    """
    Execute all registered tasks to verify implementation status.
    Useful for instructors to inspect which team files have been completed.
    """
    engine = AutomationEngine()
    engine.discover_tasks()
    tasks = engine.list_tasks()

    if not tasks:
        console.print("[yellow]No tasks registered.[/yellow]")
        return

    table = Table(
        title="Automation Tasks Implementation Status",
        show_header=True,
        header_style="bold magenta",
    )
    table.add_column("Task Key", style="cyan")
    table.add_column("Status", style="bold")
    table.add_column("Details", style="white")

    for task in tasks:
        key = f"{task['category']}:{task['name']}"
        task_info = engine.get_task(task["category"], task["name"])
        func = task_info["func"]
        mock_kwargs = get_mock_args(func)

        try:
            engine.execute_task(task["category"], task["name"], **mock_kwargs)
            status = "[green]✅ Implemented (Success)[/green]"
            details = "Completed successfully with placeholder arguments."
        except AutomationEngineError as e:
            cause = e.__cause__
            if isinstance(cause, NotImplementedError):
                status = "[red]❌ Not Implemented[/red]"
                details = "Raises NotImplementedError."
            elif isinstance(cause, TypeError) and ("missing" in str(cause) or "required" in str(cause)):
                status = "[red]❌ Not Implemented[/red]"
                details = f"Argument error: {cause}"
            else:
                status = "[green]✅ Implemented[/green]"
                details = f"Task logic reached but raised: {type(cause).__name__}: {cause}"
        except Exception as e:
            status = "[green]✅ Implemented[/green]"
            details = f"Task logic reached but raised: {type(e).__name__}: {e}"

        table.add_row(key, status, details)

    console.print(table)


if __name__ == "__main__":
    app()
