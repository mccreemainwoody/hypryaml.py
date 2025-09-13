import typer

from pathlib import Path
from typing import Annotated

from hypryaml.workflow import apply_configuration
from . import __name__, __description__, __version__


app = typer.Typer()


def version_callback(value: bool):
    """Print the version of the CLI tool, then exit."""
    if not value:
        return

    typer.echo(f"{__name__} - {__description__}\n{__version__}")
    raise typer.Exit(0)


@app.command()
def main(  # noqa: D103
    config: Annotated[
        Path,
        typer.Argument(
            help="Path of the configuration file to apply. Must be a "
            "valid YAML file",
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
            resolve_path=True,
        ),
    ],
    version: Annotated[
        bool | None,
        typer.Option(
            "--version",
            "-v",
            help="Show the version of the CLI tool and exit",
            callback=version_callback,
            is_flag=True,
            is_eager=True,
        ),
    ] = None,
):
    success = apply_configuration(config)

    if success:
        typer.echo("Configuration applied successfully.")
    else:
        typer.echo("Failed to apply configuration.", err=True)
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
