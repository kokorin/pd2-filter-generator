"""Utilities for code generation."""
import re


def sanitize_name(name: str) -> str | None:
    """Convert item type name to valid Python enum name."""
    if not name or name == "None":
        return None

    # Remove special chars, uppercase, replace spaces with underscore
    name = name.replace(" ", "_").replace("-", "_").upper()
    # Remove invalid chars
    name = "".join(c for c in name if c.isalnum() or c == "_")

    # Ensure doesn't start with number
    if name and name[0].isdigit():
        name = f"TYPE_{name}"

    return name


def camel_to_snake(name: str) -> str:
    """Convert CamelCase to snake_case.

    Examples:
        ItemType -> item_type
        HTTPResponse -> http_response
        XMLParser -> xml_parser
    """
    # Insert underscore before uppercase letters that follow lowercase
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    # Insert underscore before uppercase letters that follow lowercase or uppercase letters
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
    return s2.lower()
