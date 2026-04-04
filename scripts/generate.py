# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "click",
#   "jinja2",
# ]
# ///

from pathlib import Path

import click
from generate_itemtypes import generate_itemtypes
from pd2_data import fetch_and_parse


@click.group()
def cli():
    """PD2 constants generator."""
    pass


@cli.command()
@click.argument('filename', default='ItemTypes.txt')
@click.option('--limit', '-n', default=10, help='Number of rows to show')
def inspect(filename, limit):
    """Inspect a PD2 data file."""
    click.echo(f"Fetching {filename}...")
    data = fetch_and_parse(filename)

    click.echo(f"Total rows: {len(data)}")
    if data:
        click.echo(f"Columns {len(data[0].keys())}:")
        for i, column in enumerate(data[0].keys()):
            click.echo(f"  {i}: {column}")
        click.echo(f"\nFirst {limit} rows:")
        for item in data[:limit]:
            # Show first few columns
            cols = list(item.items())[:3]
            row = ' | '.join(f"{k}={v}" for k, v in cols if v)
            click.echo(f"  {row}")


@cli.command()
def generate():
    """Generate constants from PD2 data files."""
    output_dir = Path(__file__).parent.parent / "src" / "pd2_filter_generator"

    click.echo("Generating ItemTypes...")
    output_file = generate_itemtypes(output_dir)
    click.echo(f"Generated: {output_file.relative_to(Path.cwd())}")


if __name__ == "__main__":
    cli()
