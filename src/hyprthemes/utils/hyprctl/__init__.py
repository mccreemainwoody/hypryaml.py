"""Utilities to interact with Hyprland's hyprctl command line tool."""

from .run_commands import (
    run_hyprctl_command,
    run_hyprctl_keyword,
)

__all__ = [
    "run_hyprctl_command",
    "run_hyprctl_keyword",
]
