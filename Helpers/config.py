import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")


def get_required_env(name: str) -> str:
    value = os.getenv(name)

    if not value:
        raise RuntimeError(
            f"Missing required environment variable: {name}. "
            "Create a .env file based on .env.example."
        )

    return value


def get_bool_env(name: str, default: bool = False) -> bool:
    value = os.getenv(name)

    if value is None:
        return default

    return value.lower() == "true"


def get_int_env(name: str, default: int) -> int:
    value = os.getenv(name)

    if value is None:
        return default

    try:
        return int(value)
    except ValueError as error:
        raise RuntimeError(f"{name} must be an integer.") from error


BASE_URL = get_required_env("BASE_URL")

ADMIN_USERNAME = get_required_env("ADMIN_USERNAME")
ADMIN_PASSWORD = get_required_env("ADMIN_PASSWORD")

USER_USERNAME = get_required_env("USER_USERNAME")
USER_PASSWORD = get_required_env("USER_PASSWORD")

FAIL_PASSWORD = get_required_env("FAIL_PASSWORD")

BROWSER = os.getenv("BROWSER", "chrome").lower()
HEADLESS = get_bool_env("HEADLESS")
WINDOW_WIDTH = get_int_env("WINDOW_WIDTH", 1920)
WINDOW_HEIGHT = get_int_env("WINDOW_HEIGHT", 1080)
CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH")
