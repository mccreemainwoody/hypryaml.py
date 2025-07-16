import typer

from workflow import apply_configuration

from pathlib import Path
from typing import Annotated


def main(
        config: Annotated[
            Path,
            typer.Argument(
                help="Path of the configuration file to apply. Must be a "
                     "valid YAML file",
                exists=True,
                file_okay=True,
                dir_okay=False,
                readable=True,
                resolve_path=True
            )
        ]
):  # noqa: D103
    success = apply_configuration(config)

    if success:
        typer.echo("Configuration applied successfully.")
    else:
        typer.echo("Failed to apply configuration.", err=True)
        raise typer.Exit(code=1)


if __name__ == "__main__":
    typer.run(main)
