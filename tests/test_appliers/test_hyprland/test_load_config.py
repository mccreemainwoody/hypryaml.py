import pytest
import yaml

from appliers.hyprland.load_config import generate_keywords

from pathlib import Path
from typing import Any

from tests.config import TEST_CONFIGS_ROOT


@pytest.mark.parametrize(
    "test_config_path, expected_result",
    [
        (
            TEST_CONFIGS_ROOT / "false_config_hyprland.yaml",
            [
                ("wow:super:awesome", True),
                ("wow:super:features:0:name", "Feature 1"),
                ("wow:super:features:0:enabled", True),
                ("wow:super:features:1:name", "Feature 2"),
                ("wow:super:features:1:enabled", False),
            ],
        ),
        (
            TEST_CONFIGS_ROOT / "tiny_config_hyprland.yaml",
            [
                ("general:border_size", True),
                ("general:col.inactive_border",
                 "rgb(ff0000) rgb(ffff00) 45rad"),
                ("general:col.active_border", "rgb(33ccff) rgb(00ff99) 45rad"),
                ("blur:enabled", True),
                ("blur:noise", 0.15),
            ],
        )
    ],
)
def test_generate_keywords(
    test_config_path: Path,
    expected_result: list[tuple[str, Any]]
):
    test_config_dict = yaml.safe_load(test_config_path.read_text())

    assert "hyprland" in test_config_dict

    actual_result = list(generate_keywords(test_config_dict["hyprland"]))

    assert actual_result == expected_result
