class AutomationEngineError(Exception):
    """Base exception for all automation engine errors."""

    pass


class ConfigurationError(AutomationEngineError):
    """Raised when configuration values are missing, invalid, or misconfigured."""

    pass


class TaskExecutionError(AutomationEngineError):
    """Raised when a specific automation task fails during execution."""

    pass


class TaskNotFoundError(AutomationEngineError):
    """Raised when a requested automation task cannot be resolved or loaded."""

    pass


class ResourceConnectionError(AutomationEngineError):
    """Raised when the engine fails to connect to external systems (APIs, K8s, Docker, DBs)."""

    pass
