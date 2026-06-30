# ------------------------------------------------------------------------------
# Automation Engine Constants
# ------------------------------------------------------------------------------

# Application Metadata
APP_NAME = "Automation Engine"
APP_VERSION = "0.1.0"

# Task Categories / Namespaces
CATEGORY_FILES = "files"
CATEGORY_API = "api"
CATEGORY_EXCEL = "excel"
CATEGORY_EMAIL = "email"
CATEGORY_DOCKER = "docker"
CATEGORY_GIT = "git"
CATEGORY_KUBERNETES = "kubernetes"
CATEGORY_SCHEDULER = "scheduler"
CATEGORY_REPORTS = "reports"
CATEGORY_NOTIFICATIONS = "notifications"

ALL_CATEGORIES = [
    CATEGORY_FILES,
    CATEGORY_API,
    CATEGORY_EXCEL,
    CATEGORY_EMAIL,
    CATEGORY_DOCKER,
    CATEGORY_GIT,
    CATEGORY_KUBERNETES,
    CATEGORY_SCHEDULER,
    CATEGORY_REPORTS,
    CATEGORY_NOTIFICATIONS,
]

# Date Formats
DEFAULT_DATE_FORMAT = "%Y-%m-%d"
DEFAULT_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# Task Statuses
STATUS_PENDING = "pending"
STATUS_RUNNING = "running"
STATUS_SUCCESS = "success"
STATUS_FAILED = "failed"
