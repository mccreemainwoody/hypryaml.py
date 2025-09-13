from collections.abc import Generator
from typing import Any


def generate_keywords(config: dict) -> Generator[tuple[str, Any]]:
    """Generate keywords from the configuration dictionary.

    Args:
        config (dict): The configuration dictionary.

    Returns:
        list[str]: A list of keywords with their corresponding values.
    """
    for key, value in config.items():
        if isinstance(value, dict):
            for child_key, child_value in generate_keywords(value):
                yield f"{key}:{child_key}", child_value
        elif isinstance(value, list):
            for child_id, child in enumerate(value):
                for child_key, child_value in generate_keywords(child):
                    yield f"{key}:{child_id}:{child_key}", child_value
        else:
            yield key, value
