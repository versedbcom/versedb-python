from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_variant_details_response_200 import GetVariantDetailsResponse200
from ...models.get_variant_details_response_404 import GetVariantDetailsResponse404
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import Response


def _get_kwargs(
    issue_id: int,
    variant_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/issues/{issue_id}/variants/{variant_id}".format(
            issue_id=quote(str(issue_id), safe=""),
            variant_id=quote(str(variant_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetVariantDetailsResponse200 | GetVariantDetailsResponse404 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = GetVariantDetailsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetVariantDetailsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = TooManyRequestsError.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetVariantDetailsResponse200 | GetVariantDetailsResponse404 | TooManyRequestsError | UnauthorizedError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    issue_id: int,
    variant_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetVariantDetailsResponse200 | GetVariantDetailsResponse404 | TooManyRequestsError | UnauthorizedError]:
    """Get variant details.

     Returns a specific variant cover with full details.

    Args:
        issue_id (int):
        variant_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVariantDetailsResponse200 | GetVariantDetailsResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        issue_id=issue_id,
        variant_id=variant_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    issue_id: int,
    variant_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetVariantDetailsResponse200 | GetVariantDetailsResponse404 | TooManyRequestsError | UnauthorizedError | None:
    """Get variant details.

     Returns a specific variant cover with full details.

    Args:
        issue_id (int):
        variant_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVariantDetailsResponse200 | GetVariantDetailsResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        issue_id=issue_id,
        variant_id=variant_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    issue_id: int,
    variant_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetVariantDetailsResponse200 | GetVariantDetailsResponse404 | TooManyRequestsError | UnauthorizedError]:
    """Get variant details.

     Returns a specific variant cover with full details.

    Args:
        issue_id (int):
        variant_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVariantDetailsResponse200 | GetVariantDetailsResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        issue_id=issue_id,
        variant_id=variant_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    issue_id: int,
    variant_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetVariantDetailsResponse200 | GetVariantDetailsResponse404 | TooManyRequestsError | UnauthorizedError | None:
    """Get variant details.

     Returns a specific variant cover with full details.

    Args:
        issue_id (int):
        variant_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVariantDetailsResponse200 | GetVariantDetailsResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            issue_id=issue_id,
            variant_id=variant_id,
            client=client,
        )
    ).parsed
