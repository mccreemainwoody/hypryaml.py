from dataclasses import dataclass


@dataclass(frozen=True)
class CommandResult:
    """Represents the result of a command execution."""

    exit_code: int
    """The exit code of the command."""
    stdout: str
    """The content of the command standard output."""
    stderr: str
    """The content of the command standard error output."""

    @property
    def success(self):
        """Whether the command execution was successful."""
        return self.exit_code == 0
