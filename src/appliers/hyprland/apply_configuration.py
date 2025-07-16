from utils.hyprctl import run_hyprctl_keyword
from .load_config import generate_keywords

from typing import Any


def apply_hyprland_configuration(config: dict[str, Any]) -> bool:
    """Apply the configuration to Hyprland.

    Args:
        config (dict[str, Any]): The configuration to apply.

    Returns:
        bool: True if the configuration was applied successfully, False
        otherwise.
    """
    hyprland_config = config.get("hyprland", {})
    keywords = generate_keywords(hyprland_config)
    success = True

    for keyword, value in keywords:
        command_result = run_hyprctl_keyword(keyword, str(value))

        if not command_result.success:
            print(
                f"Failed to apply configuration {keyword} {value}. "
                f"Return code: {command_result.exit_code} ; message : "
                f"{command_result.stdout}"
            )
            success = False

    return success
