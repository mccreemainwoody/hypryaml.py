import yaml

from hyprthemes.appliers.hyprland import apply_hyprland_configuration

from pathlib import Path
from typing import Any


def parse_configuration(file_path: Path) -> dict[str, Any]:
    """Parse the configuration file and return a configuration dictionary.

    Args:
        file_path (Path): The path to the configuration file.

    Returns:
        dict: The parsed configuration.
    """
    return yaml.safe_load(file_path.read_text())


def apply_configuration(configuration_path: Path) -> bool:
    """Apply the configuration to Hyprland.

    Args:
        configuration_path (dict): The configuration to apply.

    Returns:
        bool: True if the configuration was applied successfully, False
        otherwise.
    """
    assert configuration_path.is_file()

    configuration = parse_configuration(configuration_path)
    success = True

    success = apply_hyprland_configuration(configuration)

    return success
