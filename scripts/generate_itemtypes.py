"""Generate ItemTypes enum from PD2 data."""
from pathlib import Path

from codegen_utils import sanitize_name
from jinja2 import Environment, FileSystemLoader
from pd2_data import fetch_and_parse


def generate_itemtypes(output_dir: Path) -> Path:
    """Generate ItemTypes enum file."""
    # Fetch data
    data = fetch_and_parse("ItemTypes.txt")

    # Filter and transform
    items = []
    for item in data:
        name = sanitize_name(item.get("ItemType"))
        code = item.get("Code", "")

        if not name or not code:
            continue

        item["ItemType"] = name
        items.append(item)

    # Render template
    templates_dir = Path(__file__).parent / "templates"
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template("item_types.py.jinja")

    rendered = template.render(items=items)

    # Write output
    output_file = output_dir / "item_types.py"
    output_file.write_text(rendered, encoding="utf-8")

    return output_file
