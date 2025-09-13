import pytest

from hypryaml.models import CommandResult
from hypryaml.utils.hyprpaper import run_hyprpaper_command


def assert_hyprctl_command(args: list[str,]) -> CommandResult:
    result = run_hyprpaper_command(args)

    if not result.success:
        pytest.fail(f"Hyprctl command failed:\n{result}")

    return result


def test_hyprpaper_help():
    result = run_hyprpaper_command(["--help"])

    assert result.exit_code == 1


def test_hyprpaper_listloaded():
    assert_hyprctl_command(["listloaded"])


def test_hyprpaper_listactive():
    assert_hyprctl_command(["listactive"])
