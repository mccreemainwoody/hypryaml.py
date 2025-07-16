import json
import subprocess

from models import CommandResult

from collections.abc import Collection


def run_hyprctl_command(args: Collection[str,], use_json: bool = False) \
        -> CommandResult:
    """Run a hyprctl command and return its output.

    Return code will be -1 if hyprctl does not recognize the request (the
    original CLI would return 0 instead).

    Args:
        args (Collection[str]): The command to run, accompanied by its
        arguments.
        use_json (bool, optional): If true, the command answer is supposed to
        return a Json object. Failure to do so by the API will result to an
        error.

    Returns:
        CommandResult: The output of the command.
    """
    total_command = ["hyprctl", *args]

    if use_json:
        total_command.insert(0, "-j")

    result = subprocess.run(
        total_command,
        capture_output=True,
        text=True,
        check=False
    )

    stdout = result.stdout.strip()
    stderr = result.stderr.strip()

    if use_json:
        stdout = json.loads(stdout)

    exit_code = -1 if stdout == "unknown request" else result.returncode

    return CommandResult(exit_code=exit_code, stdout=stdout, stderr=stderr)


def run_hyprctl_keyword(keyword: str, value: str) -> CommandResult:
    """Assign a value to a keyword using the hyprctl API.

    Return its results afterward.

    Args:
        keyword (str): The Hyprland configuration keyword to update.
        value (str): The value to assign to the keyword.

    Returns:
        CommandResult: The output of the command.
    """
    args = ("keyword", keyword, value)
    return run_hyprctl_command(args)
