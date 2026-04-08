# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "click",
#   "jinja2",
#   "duckdb",
# ]
# ///

from __future__ import annotations

import csv
import time
from io import StringIO
from pathlib import Path
from urllib.request import Request, urlopen

import click
import duckdb
from jinja2 import Environment, FileSystemLoader

BASE_URL = "https://raw.githubusercontent.com/Lukaszpg/PD2-Single-Player-Plus-mod/main/data/global/excel"
CACHE_DIR = Path(__file__).parent.parent / ".cache"


def fetch_tsv(filename: str) -> str:
    """Fetch TSV file from GitHub."""
    url = f"{BASE_URL}/{filename}"
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})  # noqa: S310
    with urlopen(req) as response:  # noqa: S310
        return response.read().decode("utf-8")


def parse_tsv(content: str) -> list[dict[str, str]]:
    """Parse TSV content into list of dicts."""
    reader = csv.DictReader(StringIO(content), delimiter="\t")
    return list(reader)


def fetch_and_parse(filename: str) -> list[dict[str, str]]:
    """Fetch and parse TSV file in one call. Results are cached in .cache directory."""
    # Create cache directory
    CACHE_DIR.mkdir(exist_ok=True)

    # Generate cache filename
    cache_file = CACHE_DIR / filename

    # Try to load from cache
    if cache_file.exists():
        content = cache_file.read_text(encoding="utf-8")
    else:
        # Fetch fresh data
        content = fetch_tsv(filename)
        # Save to cache
        cache_file.write_text(content, encoding="utf-8")

    return parse_tsv(content)


@click.group()
def cli():
    """PD2 constants generator."""


@cli.command()
@click.argument("filename", default="ItemTypes.txt")
@click.option("--limit", "-n", default=10, help="Number of rows to show")
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
            row = " | ".join(f"{k}={v}" for k, v in cols if v)
            click.echo(f"  {row}")


@cli.command()
def generate():
    """Generate constants from PD2 data files."""
    templates_dir = Path(__file__).parent / "templates"
    output_dir = Path(__file__).parent.parent / "src" / "pd2_filter_generator"

    # Setup Jinja environment with custom functions/filters
    env = Environment(loader=FileSystemLoader(templates_dir), autoescape=False)  # noqa: S701
    env.globals["fetch_and_parse"] = fetch_and_parse

    # Find all .jinja templates
    templates = sorted(templates_dir.glob("*.py.jinja"))

    if not templates:
        click.echo("No templates found in templates/", err=True)
        return

    click.echo(f"Found {len(templates)} template(s)")

    # Render each template
    for template_path in templates:
        template_name = template_path.name
        output_name = template_name.replace(".jinja", "")

        click.echo(f"Generating {output_name}...")

        template = env.get_template(template_name)
        rendered = template.render()

        output_file = output_dir / output_name
        output_file.write_text(rendered, encoding="utf-8")

        click.echo(f"  -> {output_file.relative_to(Path.cwd())}")


@cli.command()
def analyze():
    """Start DuckDB UI with cached PD2 data files loaded as tables."""
    cache_dir = CACHE_DIR

    if not cache_dir.exists():
        click.echo("No cache directory found. Run 'generate' first.", err=True)
        return

    cache_files = list(cache_dir.glob("*.txt"))
    if not cache_files:
        click.echo("No cached files found. Run 'generate' first.", err=True)
        return

    click.echo(f"Loading {len(cache_files)} cached file(s) into DuckDB...")

    # Create in-memory DuckDB connection
    con = duckdb.connect(":memory:")

    # Load each cache file as a table
    for cache_file in cache_files:
        # Table name: ItemTypes.txt -> itemtypes
        table_name = cache_file.stem.lower()
        click.echo(f"  Loading {cache_file.name} as table '{table_name}'")

        con.execute(
            f"""
            CREATE TABLE {table_name} AS
            SELECT * FROM read_csv_auto('{cache_file.absolute()}', delim='\t', header=true)
        """
        )

    click.echo("\nTables loaded. Starting DuckDB UI...")
    con.sql("CALL start_ui()")
    while True:
        time.sleep(1)


if __name__ == "__main__":
    cli()
