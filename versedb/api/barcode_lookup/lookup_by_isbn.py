from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lookup_by_isbn_response_200 import LookupByIsbnResponse200
from ...models.lookup_by_isbn_response_403 import LookupByIsbnResponse403
from ...models.lookup_by_isbn_response_404 import LookupByIsbnResponse404
from ...models.lookup_by_isbn_response_422 import LookupByIsbnResponse422
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    isbn: str,
    *,
    languages: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["languages"] = languages

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/lookup/isbn/{isbn}".format(
            isbn=quote(str(isbn), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    LookupByIsbnResponse200
    | LookupByIsbnResponse403
    | LookupByIsbnResponse404
    | LookupByIsbnResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    if response.status_code == 200:
        response_200 = LookupByIsbnResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = LookupByIsbnResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = LookupByIsbnResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = LookupByIsbnResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = TooManyRequestsError.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    LookupByIsbnResponse200
    | LookupByIsbnResponse403
    | LookupByIsbnResponse404
    | LookupByIsbnResponse422
    | TooManyRequestsError
    | UnauthorizedError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    isbn: str,
    *,
    client: AuthenticatedClient | Client,
    languages: str | Unset = UNSET,
) -> Response[
    LookupByIsbnResponse200
    | LookupByIsbnResponse403
    | LookupByIsbnResponse404
    | LookupByIsbnResponse422
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Lookup by ISBN.

     Find an issue by its ISBN (10 or 13 digits, with or without dashes).
    Commonly used for trade paperbacks and hardcovers.
    Returns full issue details including series information.

    Args:
        isbn (str): The ISBN (10 or 13 digits).
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LookupByIsbnResponse200 | LookupByIsbnResponse403 | LookupByIsbnResponse404 | LookupByIsbnResponse422 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        isbn=isbn,
        languages=languages,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    isbn: str,
    *,
    client: AuthenticatedClient | Client,
    languages: str | Unset = UNSET,
) -> (
    LookupByIsbnResponse200
    | LookupByIsbnResponse403
    | LookupByIsbnResponse404
    | LookupByIsbnResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Lookup by ISBN.

     Find an issue by its ISBN (10 or 13 digits, with or without dashes).
    Commonly used for trade paperbacks and hardcovers.
    Returns full issue details including series information.

    Args:
        isbn (str): The ISBN (10 or 13 digits).
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LookupByIsbnResponse200 | LookupByIsbnResponse403 | LookupByIsbnResponse404 | LookupByIsbnResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        isbn=isbn,
        client=client,
        languages=languages,
    ).parsed


async def asyncio_detailed(
    isbn: str,
    *,
    client: AuthenticatedClient | Client,
    languages: str | Unset = UNSET,
) -> Response[
    LookupByIsbnResponse200
    | LookupByIsbnResponse403
    | LookupByIsbnResponse404
    | LookupByIsbnResponse422
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Lookup by ISBN.

     Find an issue by its ISBN (10 or 13 digits, with or without dashes).
    Commonly used for trade paperbacks and hardcovers.
    Returns full issue details including series information.

    Args:
        isbn (str): The ISBN (10 or 13 digits).
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LookupByIsbnResponse200 | LookupByIsbnResponse403 | LookupByIsbnResponse404 | LookupByIsbnResponse422 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        isbn=isbn,
        languages=languages,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    isbn: str,
    *,
    client: AuthenticatedClient | Client,
    languages: str | Unset = UNSET,
) -> (
    LookupByIsbnResponse200
    | LookupByIsbnResponse403
    | LookupByIsbnResponse404
    | LookupByIsbnResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Lookup by ISBN.

     Find an issue by its ISBN (10 or 13 digits, with or without dashes).
    Commonly used for trade paperbacks and hardcovers.
    Returns full issue details including series information.

    Args:
        isbn (str): The ISBN (10 or 13 digits).
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LookupByIsbnResponse200 | LookupByIsbnResponse403 | LookupByIsbnResponse404 | LookupByIsbnResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            isbn=isbn,
            client=client,
            languages=languages,
        )
    ).parsed
