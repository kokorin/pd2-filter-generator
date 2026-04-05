# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "click",
#   "jinja2",
# ]
# ///

from __future__ import annotations

import csv
import keyword
import re
from io import StringIO
from pathlib import Path
from urllib.request import Request, urlopen

import click
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


NUMBER_TO_WORDS = {
    0: "ZERO",
    1: "ONE",
    2: "TWO",
    3: "THREE",
    4: "FOUR",
    5: "FIVE",
    6: "SIX",
    7: "SEVEN",
    8: "EIGHT",
    9: "NINE",
}


def to_field_name(name: str) -> str | None:
    """Convert any string to valid Python field identifier (snake_case).

    Handles: CamelCase, special chars, keywords, leading digits.

    Examples:
        BodyLoc1 -> body_loc1
        ItemType -> item_type
        *eol -> eol
        class -> class_
        2handed -> field_2handed
    """
    if not name:
        return None

    # CamelCase to snake_case
    # Insert underscore before uppercase letters that follow lowercase
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    # Insert underscore before uppercase letters that follow lowercase/digits
    s2 = re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1)
    name = s2.lower()

    # Replace invalid chars with underscore
    name = re.sub(r"[^a-z0-9_]", "_", name)

    # Collapse multiple underscores
    name = re.sub(r"_+", "_", name)

    # Strip leading/trailing underscores
    name = name.strip("_")

    if not name:
        return None

    # Replace all leading digits with words
    # 2h -> two_h, 2handed -> two_handed
    match = re.match(r"^(\d+)", name)
    if match:
        digits = match.group(1)
        words = "_".join(NUMBER_TO_WORDS[int(d)].lower() for d in digits)
        name = words + "_" + name[len(digits) :]

    # Handle keywords
    if keyword.iskeyword(name):
        name += "_"

    return name


def to_member_name(name: str) -> str | None:
    """Convert any string to valid Python enum member identifier (UPPER_CASE).

    Returns None for "None" string or empty input.
    Handles: spaces, special chars, keywords, leading digits.

    Examples:
        Shield -> SHIELD
        2Handed Melee Weapon -> TYPE_2HANDED_MELEE_WEAPON
        cap/hat -> CAP_HAT
        None -> None
        "" -> None
    """
    if not name or name == "None":
        return None

    # Replace invalid chars with underscore
    name = re.sub(r"[^a-zA-Z0-9_]", "_", name)

    # Collapse multiple underscores
    name = re.sub(r"_+", "_", name)

    # Strip leading/trailing underscores
    name = name.strip("_")

    if not name:
        return None

    # Replace all leading digits with words
    # 2H -> TWO_H, 2Handed -> TWO_HANDED
    match = re.match(r"^(\d+)", name)
    if match:
        digits = match.group(1)
        words = "_".join(NUMBER_TO_WORDS[int(d)] for d in digits)
        name = words + "_" + name[len(digits) :]

    # Handle keywords (rare for uppercase, but be safe)
    if keyword.iskeyword(name.lower()):
        name += "_"

    return name.upper()


def is_valid_identifier(name: str) -> bool:
    """Check if name is a valid Python identifier (not a keyword)."""
    return name.isidentifier() and not keyword.iskeyword(name)


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
    env.globals["is_valid_identifier"] = is_valid_identifier
    env.filters["to_field_name"] = to_field_name
    env.filters["to_member_name"] = to_member_name

    # Find all .jinja templates
    templates = sorted(templates_dir.glob("*.jinja"))

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


if __name__ == "__main__":
    cli()
