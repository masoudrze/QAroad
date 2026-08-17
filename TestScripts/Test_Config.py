import pytest

from Helpers import config


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("true", True),
        ("TRUE", True),
        ("false", False),
        ("anything-else", False),
    ],
)
def test_get_bool_env_parses_headless_flag(monkeypatch, value, expected):
    monkeypatch.setenv("HEADLESS", value)

    assert config.get_bool_env("HEADLESS") is expected


def test_get_int_env_uses_default_when_value_is_missing(monkeypatch):
    monkeypatch.delenv("WINDOW_WIDTH", raising=False)

    assert config.get_int_env("WINDOW_WIDTH", 1920) == 1920


def test_get_int_env_rejects_non_numeric_values(monkeypatch):
    monkeypatch.setenv("WINDOW_HEIGHT", "wide")

    with pytest.raises(RuntimeError, match="WINDOW_HEIGHT must be an integer"):
        config.get_int_env("WINDOW_HEIGHT", 1080)
