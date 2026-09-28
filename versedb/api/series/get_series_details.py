from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_series_details_response_200 import GetSeriesDetailsResponse200
from ...models.get_series_details_response_404 import GetSeriesDetailsResponse404
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import Response


def _get_kwargs(
    series_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/series/{series_id}".format(
            series_id=quote(str(series_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetSeriesDetailsResponse200 | GetSeriesDetailsResponse404 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = GetSeriesDetailsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetSeriesDetailsResponse404.from_dict(response.json())

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
) -> Response[GetSeriesDetailsResponse200 | GetSeriesDetailsResponse404 | TooManyRequestsError | UnauthorizedError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    series_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetSeriesDetailsResponse200 | GetSeriesDetailsResponse404 | TooManyRequestsError | UnauthorizedError]:
    """Get series details.

     Returns a single series with full details including related title, publishers, and genres.
    For relationship data (issues, creators, characters), use the relationship endpoints.

    Args:
        series_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSeriesDetailsResponse200 | GetSeriesDetailsResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        series_id=series_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    series_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetSeriesDetailsResponse200 | GetSeriesDetailsResponse404 | TooManyRequestsError | UnauthorizedError | None:
    """Get series details.

     Returns a single series with full details including related title, publishers, and genres.
    For relationship data (issues, creators, characters), use the relationship endpoints.

    Args:
        series_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSeriesDetailsResponse200 | GetSeriesDetailsResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        series_id=series_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    series_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetSeriesDetailsResponse200 | GetSeriesDetailsResponse404 | TooManyRequestsError | UnauthorizedError]:
    """Get series details.

     Returns a single series with full details including related title, publishers, and genres.
    For relationship data (issues, creators, characters), use the relationship endpoints.

    Args:
        series_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSeriesDetailsResponse200 | GetSeriesDetailsResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        series_id=series_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    series_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetSeriesDetailsResponse200 | GetSeriesDetailsResponse404 | TooManyRequestsError | UnauthorizedError | None:
    """Get series details.

     Returns a single series with full details including related title, publishers, and genres.
    For relationship data (issues, creators, characters), use the relationship endpoints.

    Args:
        series_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSeriesDetailsResponse200 | GetSeriesDetailsResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            series_id=series_id,
            client=client,
        )
    ).parsed
