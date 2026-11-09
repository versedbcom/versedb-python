# /// script
# requires-python = ">=3.11"
# ///
"""Fetch the VerseDB User API spec and patch what openapi-python-client can't express.

The API server publishes the spec as JSON at ``/api/v1/openapi.json``. One shape
needs a fix before generation: objects keyed by ID or month number (``{"5432": ...}``,
``{"1": ..., "12": ...}``) come out as fixed ``properties`` with numeric names,
which would become ``field_1`` ... ``field_12`` attributes. They are maps, so they
become ``additionalProperties`` and the model is a plain dict.

Usage: uv run scripts/prepare_spec.py [SOURCE] [OUTPUT]
"""

from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path

DEFAULT_SOURCE = "https://versedb.com/api/v1/openapi.json"
DEFAULT_OUTPUT = Path(__file__).resolve().parent.parent / "openapi.json"


def load(source: str) -> dict:
    if source.startswith(("http://", "https://")):
        request = urllib.request.Request(source, headers={"Accept": "application/json"})
        with urllib.request.urlopen(request, timeout=60) as response:
            text = response.read().decode()
    else:
        text = Path(source).read_text()
    return json.loads(text)


def is_numeric_key(key: object) -> bool:
    return isinstance(key, str) and key.isdigit()


def patch(node: object) -> None:
    if isinstance(node, list):
        for item in node:
            patch(item)
        return
    if not isinstance(node, dict):
        return

    properties = node.get("properties")
    if isinstance(properties, dict) and properties and all(map(is_numeric_key, properties)):
        node["additionalProperties"] = next(iter(properties.values()))
        del node["properties"]
        node.pop("required", None)

    for value in node.values():
        patch(value)


def main() -> None:
    source = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SOURCE
    output = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUTPUT
    spec = load(source)
    patch(spec)
    output.write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
