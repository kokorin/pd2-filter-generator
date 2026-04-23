# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "click",
#   "jinja2",
#   "duckdb",
# ]
# ///
"""
Use Ladik's MPQ Editor to extract data from MPQ files
ListFiles are required to open some MPQ - https://d2mods.info/forum/viewtopic.php?t=65218
Add ListFiles to MPQ Editor's ListFiles directory and select it in dropdown list (if asked on MPQ read).

Extraction overwrites files, so extraction must be ordered. To speed up extraction, extract only 2 dirs:
* data/global/excel
* data/local/lng/eng

Order of extraction:
1. {D2}/d2data.mpq
2. {D2}/d2exp.mpq
3. {D2}/patch_d2.mpq
4. {D2}/ProjectD2/patch_d2.mpq
5. {D2}/ProjectD2/pd2data.mpq
Some MPQ may contain Excel TXT files named with different case: Armor.txt and armor.txt
NOTE: not sure about order of steps 4 and 5
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

import click
from jinja2 import Environment, FileSystemLoader

CACHE_DIR = Path(__file__).parent.parent / ".cache"


def find_in_mpq(mpq_path: Path, d2_path: Path) -> Path:
    """Extract file from MPQ stack. First MPQ in list has highest priority.

    Args:
        path: Path inside MPQ (e.g., Path("data/global/excel/Armor.txt"))
        d2_path: directory with extracted MPQ data

    Returns:
        Raw file bytes from first MPQ that contains it, or None if not found
    """

    mpq_path = d2_path / mpq_path
    for path in [mpq_path, mpq_path.with_name(mpq_path.name.lower())]:
        if path.exists():
            return path

    raise FileNotFoundError(f"{mpq_path} not found in any MPQ file")  # noqa: TRY003,EM102


def read_tsv(tsv_path: Path) -> list[dict[str, str]]:
    lines = tsv_path.read_text().splitlines()
    reader = csv.DictReader(lines, delimiter="\t")
    return list(reader)


TBL_CACHE = {}


def read_tbl(tbl_path: Path) -> dict[str, str]:
    result = TBL_CACHE.setdefault(tbl_path, {})
    if result:
        return result

    """Parse a Diablo 2 TBL file into a key-value dictionary."""
    with open(tbl_path, "rb") as f:
        data = f.read()

    offset = 0

    # Skip CRC (2 bytes)
    offset += 2

    # Number of elements (2 bytes, uint16 little-endian)
    num_elements = int.from_bytes(data[offset : offset + 2], byteorder="little")
    offset += 2

    # Hash table size (4 bytes, uint32 little-endian)
    hash_table_size = int.from_bytes(data[offset : offset + 4], byteorder="little")
    offset += 4

    # Version (1 byte, always 0)
    offset += 1

    # Skip metadata (12 bytes: StringOffset, retry count, FileSize)
    offset += 12

    # Element indices (num_elements * 2 bytes)
    offset += num_elements * 2

    # Read hash entries (17 bytes each)
    hash_entries = []
    for _ in range(hash_table_size):
        is_active = data[offset] != 0
        offset += 1

        index = int.from_bytes(data[offset : offset + 2], byteorder="little")
        offset += 2

        hash_value = int.from_bytes(data[offset : offset + 4], byteorder="little")
        offset += 4

        index_string = int.from_bytes(data[offset : offset + 4], byteorder="little")
        offset += 4

        name_string = int.from_bytes(data[offset : offset + 4], byteorder="little")
        offset += 4

        name_length = int.from_bytes(data[offset : offset + 2], byteorder="little")
        offset += 2

        hash_entries.append(
            {
                "is_active": is_active,
                "index": index,
                "hash_value": hash_value,
                "index_string": index_string,
                "name_string": name_string,
                "name_length": name_length,
            }
        )

    for idx, entry in enumerate(hash_entries):
        if not entry["is_active"]:
            continue

        # Read value at nameString offset
        value_offset = entry["name_string"]
        value_length = entry["name_length"] - 1
        value = data[value_offset : value_offset + value_length].decode("latin-1")

        # Read key at indexString offset (null-terminated)
        key_offset = entry["index_string"]
        key_end = data.index(b"\x00", key_offset)
        key = data[key_offset:key_end].decode("latin-1")

        # Handle special keys
        if key.upper() == "X":
            key = f"#{idx}"

        # Store in lookup table (skip duplicates)
        if key not in result:
            result[key] = value

    cached = CACHE_DIR / tbl_path.with_suffix(".json").name
    if not cached.exists():
        cached.parent.mkdir(parents=True, exist_ok=True)
        cached.write_text(json.dumps(result))

    return result


def raise_exception(msg: str):
    raise Exception(msg)  # noqa: TRY002


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--d2-path",
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    help="Diablo II installation directory (e.g., C:/Games/Diablo II)",
)
def generate(d2_path: Path):
    """Generate constants from PD2 data files."""
    templates_dir = Path(__file__).parent / "templates"
    output_dir = Path(__file__).parent.parent / "src" / "pd2_filter_generator"

    # Setup Jinja environment with custom functions/filters
    env = Environment(loader=FileSystemLoader(templates_dir), autoescape=False)  # noqa: S701
    env.globals["read_tsv"] = lambda mpq_path: read_tsv(find_in_mpq(Path(mpq_path), d2_path))
    env.globals["read_tbl"] = lambda mpq_path: read_tbl(find_in_mpq(Path(mpq_path), d2_path))
    env.globals["raise"] = raise_exception

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
        output_file.write_text(rendered, encoding="utf-8", newline="\n")

        click.echo(f"  -> {output_file.relative_to(Path.cwd())}")


if __name__ == "__main__":
    cli()
