from models.CommandResult import CommandResult
from ..hyprctl import run_hyprctl_command


def run_hyprpaper_command(command: str) -> CommandResult:
    """Run a hyprpaper command and return its output.

    Args:
        command (str): The hyprpaper command to run.

    Returns:
        CommandResult: The output of the command.
    """
    return run_hyprctl_command(f"hyprpaper {command}")
