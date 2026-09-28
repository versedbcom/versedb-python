Overrides for openapi-python-client's built-in templates, copied from the
version pinned in `scripts/generate.sh`. Re-copy them when bumping it.

- `client.py.jinja`: every request sends `Accept: application/json` unless the
  caller overrides it. Without it, versedb.com answers a bad or missing token
  with a 302 to the login page instead of a JSON 401.
