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


BASE_URL = get_required_env("BASE_URL")

ADMIN_USERNAME = get_required_env("ADMIN_USERNAME")
ADMIN_PASSWORD=get_required_env("ADMIN_PASSWORD")

USER_USERNAME = get_required_env("USER_USERNAME")
USER_PASSWORD=get_required_env("USER_PASSWORD")

FAIL_PASSWORD=get_required_env("FAIL_PASSWORD")