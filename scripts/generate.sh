#!/usr/bin/env bash
# Regenerate the versedb package from the live User API spec.
set -euo pipefail

cd "$(dirname "$0")/.."

GENERATOR_VERSION="0.29.1"

uv run scripts/prepare_spec.py "${1:-https://versedb.com/api/docs.openapi}" openapi.json

uvx "openapi-python-client==${GENERATOR_VERSION}" generate \
  --path openapi.json \
  --config generator.yaml \
  --custom-template-path templates \
  --meta none \
  --output-path versedb \
  --overwrite

# The package is fully typed; --overwrite removes the marker, so restore it.
touch versedb/py.typed
