from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lookup_by_upc_response_200 import LookupByUpcResponse200
from ...models.lookup_by_upc_response_403 import LookupByUpcResponse403
from ...models.lookup_by_upc_response_404 import LookupByUpcResponse404
from ...models.lookup_by_upc_response_409 import LookupByUpcResponse409
from ...models.lookup_by_upc_response_422 import LookupByUpcResponse422
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    upc: str,
    *,
    languages: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["languages"] = languages

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/lookup/upc/{upc}".format(
            upc=quote(str(upc), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    LookupByUpcResponse200
    | LookupByUpcResponse403
    | LookupByUpcResponse404
    | LookupByUpcResponse409
    | LookupByUpcResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    if response.status_code == 200:
        response_200 = LookupByUpcResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = LookupByUpcResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = LookupByUpcResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = LookupByUpcResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = LookupByUpcResponse422.from_dict(response.json())

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
    LookupByUpcResponse200
    | LookupByUpcResponse403
    | LookupByUpcResponse404
    | LookupByUpcResponse409
    | LookupByUpcResponse422
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
    upc: str,
    *,
    client: AuthenticatedClient | Client,
    languages: str | Unset = UNSET,
) -> Response[
    LookupByUpcResponse200
    | LookupByUpcResponse403
    | LookupByUpcResponse404
    | LookupByUpcResponse409
    | LookupByUpcResponse422
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Lookup by UPC.

     Find an issue by its UPC barcode (10 to 18 digits; anything else in the code is dropped). A
    variant's printed code finds its issue, and a bare 12-digit series code
    widens to every issue built on it. One issue returns 200 with its covers; a code several issues hold
    returns 409 with up to 25 candidates.

    Args:
        upc (str): The UPC barcode.
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LookupByUpcResponse200 | LookupByUpcResponse403 | LookupByUpcResponse404 | LookupByUpcResponse409 | LookupByUpcResponse422 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        upc=upc,
        languages=languages,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    upc: str,
    *,
    client: AuthenticatedClient | Client,
    languages: str | Unset = UNSET,
) -> (
    LookupByUpcResponse200
    | LookupByUpcResponse403
    | LookupByUpcResponse404
    | LookupByUpcResponse409
    | LookupByUpcResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Lookup by UPC.

     Find an issue by its UPC barcode (10 to 18 digits; anything else in the code is dropped). A
    variant's printed code finds its issue, and a bare 12-digit series code
    widens to every issue built on it. One issue returns 200 with its covers; a code several issues hold
    returns 409 with up to 25 candidates.

    Args:
        upc (str): The UPC barcode.
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LookupByUpcResponse200 | LookupByUpcResponse403 | LookupByUpcResponse404 | LookupByUpcResponse409 | LookupByUpcResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        upc=upc,
        client=client,
        languages=languages,
    ).parsed


async def asyncio_detailed(
    upc: str,
    *,
    client: AuthenticatedClient | Client,
    languages: str | Unset = UNSET,
) -> Response[
    LookupByUpcResponse200
    | LookupByUpcResponse403
    | LookupByUpcResponse404
    | LookupByUpcResponse409
    | LookupByUpcResponse422
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Lookup by UPC.

     Find an issue by its UPC barcode (10 to 18 digits; anything else in the code is dropped). A
    variant's printed code finds its issue, and a bare 12-digit series code
    widens to every issue built on it. One issue returns 200 with its covers; a code several issues hold
    returns 409 with up to 25 candidates.

    Args:
        upc (str): The UPC barcode.
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LookupByUpcResponse200 | LookupByUpcResponse403 | LookupByUpcResponse404 | LookupByUpcResponse409 | LookupByUpcResponse422 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        upc=upc,
        languages=languages,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    upc: str,
    *,
    client: AuthenticatedClient | Client,
    languages: str | Unset = UNSET,
) -> (
    LookupByUpcResponse200
    | LookupByUpcResponse403
    | LookupByUpcResponse404
    | LookupByUpcResponse409
    | LookupByUpcResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Lookup by UPC.

     Find an issue by its UPC barcode (10 to 18 digits; anything else in the code is dropped). A
    variant's printed code finds its issue, and a bare 12-digit series code
    widens to every issue built on it. One issue returns 200 with its covers; a code several issues hold
    returns 409 with up to 25 candidates.

    Args:
        upc (str): The UPC barcode.
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LookupByUpcResponse200 | LookupByUpcResponse403 | LookupByUpcResponse404 | LookupByUpcResponse409 | LookupByUpcResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            upc=upc,
            client=client,
            languages=languages,
        )
    ).parsed
