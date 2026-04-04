"""Utilities for fetching and parsing PD2 data files."""
import csv
from io import StringIO
from urllib.request import Request, urlopen


BASE_URL = "https://raw.githubusercontent.com/Lukaszpg/PD2-Single-Player-Plus-mod/main/data/global/excel"


def fetch_tsv(filename: str) -> str:
    """Fetch TSV file from GitHub."""
    url = f"{BASE_URL}/{filename}"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(req) as response:
        return response.read().decode('utf-8')


def parse_tsv(content: str) -> list[dict[str, str]]:
    """Parse TSV content into list of dicts."""
    reader = csv.DictReader(StringIO(content), delimiter='\t')
    return list(reader)


def fetch_and_parse(filename: str) -> list[dict[str, str]]:
    """Fetch and parse TSV file in one call."""
    content = fetch_tsv(filename)
    return parse_tsv(content)
