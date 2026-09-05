# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "click",
#   "pystache",
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
import re
from pathlib import Path
from typing import Any

import click
import pystache

CACHE_DIR = Path(__file__).parent.parent / ".cache"


def find_in_mpq(d2_path: Path, mpq_path: Path) -> Path:
    """Finds a file in a directory where all MPQs are extracted to.
    TODO refactor to read original MPQ without a need for manual extraction.

    Args:
        d2_path: directory with extracted MPQ data
        mpq_path: Path inside MPQ (e.g., Path("data/global/excel/Armor.txt"))

    Returns:
        Full Path to a file, or None if not found
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


# TODO: refactor caching
def read_tbl(tbl_path: Path) -> dict[str, str]:
    """Parses a Diablo 2 TBL file into a key-value dictionary."""

    result = TBL_CACHE.setdefault(tbl_path, {})
    if result:
        return result

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


# TODO: refactor
def to_snake_case(value: str) -> str:
    value = value.replace(" ", "_")

    value = re.sub(r"[^A-Za-z0-9_]+", "", value)
    # 1. Insert an underscore before any capital letter followed by lowercase (e.g., camelCase -> camel_Case)
    value = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", value)

    # 2. Insert an underscore between lowercase/numbers and uppercase letters (e.g., HTTPResponse -> HTTP_Response)
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)

    # 3. Replace spaces, hyphens, or multiple underscores with a single underscore
    value = re.sub(r"[\s\-_]+", "_", value)

    # 4. Clean up any trailing/leading underscores and convert to lowercase
    return value.strip("_").lower()


def render_template(template_name: str, context: dict[str, Any]) -> None:
    template_path = Path(__file__).parent / "templates" / f"{template_name}.py.mst"
    python_path = Path(__file__).parent.parent / "src" / "pd2_filter_generator" / f"{template_name}.py"

    template = template_path.read_text("utf-8")
    rendered = pystache.render(template, context)
    python_path.write_text(rendered, "utf-8", newline="\n")


def resolve_name(d2_path: Path, code: str) -> str:
    for tbl_name in ["patchstring.tbl", "expansionstring.tbl", "string.tbl"]:
        tbl_path = find_in_mpq(d2_path, Path("data/local/lng/eng") / tbl_name)
        tbl = read_tbl(tbl_path)
        if code in tbl:
            return tbl[code]
    raise ValueError(f"No such code: {code}")  # noqa: TRY003 EM102


def read_weapons(d2_path: Path) -> list[dict[str, str]]:
    path = find_in_mpq(d2_path, Path("data/global/excel/Weapons.txt"))
    raw = read_tsv(path)
    # PD2 spawns new potions with new codes, legacy potions are disabled from dropping
    # https://wiki.projectdiablo2.com/wiki/Item_Filtering#Potions
    legacy_potions = {"opl", "gpl", "opm", "gpm", "ops", "gps", "7cr2"}

    return [
        {
            # For some reason in tbl files Strangling Potion and Choking Potion are called
            # Strangling Gas Potion and Choking Gas Potion
            "name": to_snake_case(resolve_name(d2_path, row["namestr"])).replace("_gas_", "_").upper(),
            "code": row["code"],
            "type": row["type"],
            "type2": row["type2"],
            "props": json.dumps(row),
        }
        for row in raw
        if (
            row["name"] not in {"None", "Not Used", "Unused", "unused", "Expansion"}
            and row["code"] not in legacy_potions
            and row["spawnable"] == "1"
        )
    ]


def read_armor(d2_path: Path) -> list[dict[str, str]]:
    path = find_in_mpq(d2_path, Path("data/global/excel/Armor.txt"))
    raw = read_tsv(path)
    # Special weapon types are added in PD2, only for unique version
    # https://wiki.projectdiablo2.com/wiki/Item_Filtering#PD2_Items
    special_equipment = {
        "rar": "Cage of the Unsullied",
        "rbe": "Band of Skulls",
        "ram": "The Third Eye",
    }
    return [
        {
            "name": to_snake_case(special_equipment.get(row["code"]) or resolve_name(d2_path, row["namestr"])).upper(),
            "code": row["code"],
            "reqstr": row["reqstr"],
            "levelreq": row["levelreq"],
            "props": json.dumps(row),
        }
        for row in raw
        if row["name"] not in {"None", "Not Used", "Unused", "unused", "Expansion"}
    ]


def read_sets(d2_path: Path) -> list[dict[str, str]]:
    path = find_in_mpq(d2_path, Path("data/global/excel/Sets.txt"))
    raw = read_tsv(path)
    return [
        {
            "name": to_snake_case(resolve_name(d2_path, row["name"])).upper(),
            "level": row["level"],
            "props": json.dumps(row),
        }
        for row in raw
        if row["index"] not in {"None", "Not Used", "Unused", "unused", "Expansion"}
    ]


def read_set_items(d2_path: Path) -> list[dict[str, str]]:
    path = find_in_mpq(d2_path, Path("data/global/excel/SetItems.txt"))
    raw = read_tsv(path)
    return [
        {
            "name": to_snake_case(resolve_name(d2_path, row["index"])).upper(),
            "set": to_snake_case(resolve_name(d2_path, row["set"])).upper(),
            "lvl": row["lvl"],
            "lvl_req": row["lvl req"],
            "props": json.dumps(row),
        }
        for row in raw
        if row["index"] not in {"None", "Not Used", "Unused", "unused", "Expansion"}
    ]


def read_unique_items(d2_path: Path) -> list[dict[str, str]]:
    path = find_in_mpq(d2_path, Path("data/global/excel/UniqueItems.txt"))
    raw = read_tsv(path)
    uniques = [
        {
            "name": to_snake_case(resolve_name(d2_path, row["index"])).upper(),
            "code": row["code"],
            "ladder": str(row["ladder"] == "1"),
            "lvl": row["lvl"],
            "lvl_req": row["lvl req"],
            # "props": json.dumps(row), props will affect deduplication, be careful
        }
        for row in raw
        if (
            row["index"]
            not in {
                "None",
                "Not Used",
                "Unused",
                "unused",
                "Expansion",
                "Armor",
                "Ring",
                "Elite Uniques",
                "Class Specific",
            }
            and row["enabled"] not in {"0", "", None}
        )
    ]

    # Some uniques (like Rainbow Facet) have different variations, we deduplicate variations if they are same
    # If variations are different - generated code will raise an error
    result = []
    for unique in uniques:
        if unique in result:
            continue
        result.append(unique)

    return result


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
    context = {
        "weapon": read_weapons(d2_path),
        "armor": read_armor(d2_path),
        "set": read_sets(d2_path),
        "set_item": read_set_items(d2_path),
        "unique_item": read_unique_items(d2_path),
    }
    click.echo(f"Loaded {', '.join(context.keys())}")

    for template_name in context:
        click.echo(f"Processing {template_name}")
        render_template(template_name, context)


if __name__ == "__main__":
    cli()
