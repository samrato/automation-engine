import pytest

from core.exceptions import TaskNotFoundError
from engine import _TASK_REGISTRY, AutomationEngine, register_task


def test_task_registration():
    """Test that the @register_task decorator updates the registry."""

    # Define a temporary dummy task
    @register_task(name="dummy_test", category="test", description="A test dummy task")
    def dummy_func():
        return "hello test"

    engine = AutomationEngine()
    task_info = engine.get_task("test", "dummy_test")

    assert task_info["name"] == "dummy_test"
    assert task_info["category"] == "test"
    assert task_info["description"] == "A test dummy task"
    assert task_info["func"]() == "hello test"

    # Clean up registry
    del _TASK_REGISTRY["test:dummy_test"]


def test_task_not_found():
    """Test that looking up a non-existent task raises TaskNotFoundError."""
    engine = AutomationEngine()
    with pytest.raises(TaskNotFoundError):
        engine.get_task("nonexistent", "task")
