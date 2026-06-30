import os
from pathlib import Path

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings:
    """
    Global configuration settings for the Automation Engine.
    Loads values from environment variables with sensible defaults.
    """

    # Base Directory
    BASE_DIR: Path = Path(__file__).resolve().parent

    # Environment
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    # Email (SMTP)
    SMTP_HOST: str = os.getenv("SMTP_HOST", "smtp.gmail.com")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USERNAME: str | None = os.getenv("SMTP_USERNAME")
    SMTP_PASSWORD: str | None = os.getenv("SMTP_PASSWORD")
    SENDER_EMAIL: str | None = os.getenv("SENDER_EMAIL")

    # Notifications
    SLACK_WEBHOOK_URL: str | None = os.getenv("SLACK_WEBHOOK_URL")
    SLACK_API_TOKEN: str | None = os.getenv("SLACK_API_TOKEN")
    DISCORD_WEBHOOK_URL: str | None = os.getenv("DISCORD_WEBHOOK_URL")

    # APIs
    EXTERNAL_API_URL: str = os.getenv("EXTERNAL_API_URL", "https://api.placeholder-service.com/v1")
    EXTERNAL_API_KEY: str | None = os.getenv("EXTERNAL_API_KEY")

    # Folders
    DATA_INPUT_DIR: Path = BASE_DIR / os.getenv("DATA_INPUT_DIR", "data/input")
    DATA_OUTPUT_DIR: Path = BASE_DIR / os.getenv("DATA_OUTPUT_DIR", "data/output")
    LOGS_DIR: Path = BASE_DIR / os.getenv("LOGS_DIR", "logs")

    def create_required_dirs(self) -> None:
        """Create standard directories if they don't exist."""
        self.DATA_INPUT_DIR.mkdir(parents=True, exist_ok=True)
        self.DATA_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        self.LOGS_DIR.mkdir(parents=True, exist_ok=True)


# Global settings instance
settings = Settings()
settings.create_required_dirs()
