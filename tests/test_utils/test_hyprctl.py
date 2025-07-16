import pytest

from src.utils.hyprctl import HyprCtlResponse, run_hyprctl_command


def assert_hyprctl_command(args: list[str,]) -> HyprCtlResponse:
    """Global function to test hyprctl commands."""
    result = run_hyprctl_command(args)

    if result["exit_code"] != 0:
        pytest.fail(f"Hyprctl command failed: {result}")

    return result


def test_hyprctl_help():
    result = run_hyprctl_command(["--help"])

    assert result["exit_code"] == 1


def test_hyprctl_version():
    assert_hyprctl_command(["version"])


def test_hyprctl_splash():
    assert_hyprctl_command(["splash"])
