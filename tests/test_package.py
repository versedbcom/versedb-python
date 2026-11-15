"""Smoke tests: the generated package imports cleanly and exposes the client."""

import importlib
import pkgutil
from uuid import UUID

import versedb
import versedb.api
from versedb import AuthenticatedClient
from versedb.api.user import add_issue_to_collection


def test_every_endpoint_module_imports():
    modules = [info.name for info in pkgutil.walk_packages(versedb.api.__path__, "versedb.api.")]
    assert modules
    for name in modules:
        importlib.import_module(name)


def test_authenticated_client_sends_bearer_token():
    client = AuthenticatedClient(base_url="https://versedb.com", token="secret")
    headers = client.get_httpx_client().headers
    assert headers["Authorization"] == "Bearer secret"


def test_client_asks_for_json_by_default():
    client = AuthenticatedClient(base_url="https://versedb.com", token="secret")
    assert client.get_httpx_client().headers["Accept"] == "application/json"


def test_caller_can_override_accept():
    client = AuthenticatedClient(base_url="https://versedb.com", token="secret", headers={"Accept": "text/plain"})
    assert client.get_httpx_client().headers["Accept"] == "text/plain"


def test_idempotency_key_is_sent_as_a_string():
    key = UUID("7c0e4c7e-3a55-4f0c-9a58-2f6f4a0d1b21")
    kwargs = add_issue_to_collection._get_kwargs(5432, idempotency_key=key)
    client = AuthenticatedClient(base_url="https://versedb.com", token="secret")
    request = client.get_httpx_client().build_request(**kwargs)
    assert request.headers["Idempotency-Key"] == str(key)


def test_idempotency_key_is_left_out_by_default():
    assert "Idempotency-Key" not in add_issue_to_collection._get_kwargs(5432)["headers"]
