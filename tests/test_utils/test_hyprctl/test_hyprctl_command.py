import pytest

from hyprthemes.models import CommandResult
from hyprthemes.utils.hyprctl import run_hyprctl_command


def assert_hyprctl_command(args: list[str,]) -> CommandResult:
    result = run_hyprctl_command(args)

    if not result.success:
        pytest.fail(f"Hyprctl command failed:\n{result}")

    return result


def test_hyprctl_help():
    result = run_hyprctl_command(["--help"])

    assert result.exit_code == 1


def test_hyprctl_version():
    assert_hyprctl_command(["version"])


def test_hyprctl_splash():
    assert_hyprctl_command(["splash"])
