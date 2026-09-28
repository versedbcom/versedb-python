"""Smoke tests: the generated package imports cleanly and exposes the client."""

import importlib
import pkgutil

import versedb
import versedb.api
from versedb import AuthenticatedClient


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
