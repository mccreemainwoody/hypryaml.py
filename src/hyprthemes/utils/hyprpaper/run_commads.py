from hyprthemes.models import CommandResult
from hyprthemes.utils.hyprctl import run_hyprctl_command

from collections.abc import Collection
from os import PathLike


def run_hyprpaper_command(args: Collection[str,]) -> CommandResult:
    """Run a hyprpaper command and return its output.

    Args:
        args (Collection[str]): The hyprpaper command to run.

    Returns:
        CommandResult: The output of the command.
    """
    command_args = ["hyprpaper", *args]
    return run_hyprctl_command(command_args)


def run_hyprpaper_preload(path: PathLike) -> CommandResult:
    """Preload a wallpaper of the hyprpaper API.

    Args:
        path (PathLike): The path to the wallpaper image.

    Returns:
        CommandResult: The output of the command.
    """
    commands_args = ["preload", str(path)]
    return run_hyprpaper_command(commands_args)


def run_hyprpaper_unload(path: PathLike) -> CommandResult:
    """Unload a wallpaper of the hyprpaper API.

    Args:
        path (PathLike): The path to the wallpaper image.

    Returns:
        CommandResult: The output of the command.
    """
    commands_args = ["unload", str(path)]
    return run_hyprpaper_command(commands_args)


def run_hyprpaper_unload_all() -> CommandResult:
    """Unload all the wallpapers of the hyprpaper API.

    Returns:
        CommandResult: The output of the command.
    """
    commands_args = ["unload", "all"]
    return run_hyprpaper_command(commands_args)


def run_hyprpaper_wallpaper(monitor: str, path: PathLike) -> CommandResult:
    """Set a wallpaper for a specific monitor using the hyprpaper API.

    Args:
        monitor (str): The monitor identifier to set the wallpaper of.
        path (PathLike): The path to the wallpaper image.

    Returns:
        CommandResult: The output of the command.
    """
    commands_args = ["wallpaper", f"{monitor},{path}"]
    return run_hyprpaper_command(commands_args)
