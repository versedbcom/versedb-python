from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lookup_by_distributor_code_response_200 import LookupByDistributorCodeResponse200
from ...models.lookup_by_distributor_code_response_403 import LookupByDistributorCodeResponse403
from ...models.lookup_by_distributor_code_response_404 import LookupByDistributorCodeResponse404
from ...models.lookup_by_distributor_code_response_409 import LookupByDistributorCodeResponse409
from ...models.lookup_by_distributor_code_response_422 import LookupByDistributorCodeResponse422
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import Response


def _get_kwargs(
    code: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/lookup/code/{code}".format(
            code=quote(str(code), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    LookupByDistributorCodeResponse200
    | LookupByDistributorCodeResponse403
    | LookupByDistributorCodeResponse404
    | LookupByDistributorCodeResponse409
    | LookupByDistributorCodeResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    if response.status_code == 200:
        response_200 = LookupByDistributorCodeResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = LookupByDistributorCodeResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = LookupByDistributorCodeResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = LookupByDistributorCodeResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = LookupByDistributorCodeResponse422.from_dict(response.json())

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
    LookupByDistributorCodeResponse200
    | LookupByDistributorCodeResponse403
    | LookupByDistributorCodeResponse404
    | LookupByDistributorCodeResponse409
    | LookupByDistributorCodeResponse422
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
    code: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    LookupByDistributorCodeResponse200
    | LookupByDistributorCodeResponse403
    | LookupByDistributorCodeResponse404
    | LookupByDistributorCodeResponse409
    | LookupByDistributorCodeResponse422
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Lookup by distributor code.

     Find an issue by its distributor order code: a Lunar code (like `0126IM0451`) or a
    Universal code (like `DC10251016`), in any case. A variant's own code finds its issue,
    and `suggested_variant_id` then names that variant. The payload matches the UPC lookup:
    one issue returns 200, a code held by several issues returns 409 with the candidates.

    Args:
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LookupByDistributorCodeResponse200 | LookupByDistributorCodeResponse403 | LookupByDistributorCodeResponse404 | LookupByDistributorCodeResponse409 | LookupByDistributorCodeResponse422 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        code=code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    code: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    LookupByDistributorCodeResponse200
    | LookupByDistributorCodeResponse403
    | LookupByDistributorCodeResponse404
    | LookupByDistributorCodeResponse409
    | LookupByDistributorCodeResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Lookup by distributor code.

     Find an issue by its distributor order code: a Lunar code (like `0126IM0451`) or a
    Universal code (like `DC10251016`), in any case. A variant's own code finds its issue,
    and `suggested_variant_id` then names that variant. The payload matches the UPC lookup:
    one issue returns 200, a code held by several issues returns 409 with the candidates.

    Args:
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LookupByDistributorCodeResponse200 | LookupByDistributorCodeResponse403 | LookupByDistributorCodeResponse404 | LookupByDistributorCodeResponse409 | LookupByDistributorCodeResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        code=code,
        client=client,
    ).parsed


async def asyncio_detailed(
    code: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    LookupByDistributorCodeResponse200
    | LookupByDistributorCodeResponse403
    | LookupByDistributorCodeResponse404
    | LookupByDistributorCodeResponse409
    | LookupByDistributorCodeResponse422
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Lookup by distributor code.

     Find an issue by its distributor order code: a Lunar code (like `0126IM0451`) or a
    Universal code (like `DC10251016`), in any case. A variant's own code finds its issue,
    and `suggested_variant_id` then names that variant. The payload matches the UPC lookup:
    one issue returns 200, a code held by several issues returns 409 with the candidates.

    Args:
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LookupByDistributorCodeResponse200 | LookupByDistributorCodeResponse403 | LookupByDistributorCodeResponse404 | LookupByDistributorCodeResponse409 | LookupByDistributorCodeResponse422 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        code=code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    code: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    LookupByDistributorCodeResponse200
    | LookupByDistributorCodeResponse403
    | LookupByDistributorCodeResponse404
    | LookupByDistributorCodeResponse409
    | LookupByDistributorCodeResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Lookup by distributor code.

     Find an issue by its distributor order code: a Lunar code (like `0126IM0451`) or a
    Universal code (like `DC10251016`), in any case. A variant's own code finds its issue,
    and `suggested_variant_id` then names that variant. The payload matches the UPC lookup:
    one issue returns 200, a code held by several issues returns 409 with the candidates.

    Args:
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LookupByDistributorCodeResponse200 | LookupByDistributorCodeResponse403 | LookupByDistributorCodeResponse404 | LookupByDistributorCodeResponse409 | LookupByDistributorCodeResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            code=code,
            client=client,
        )
    ).parsed
