from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.view_yearly_reading_statistics_response_200 import ViewYearlyReadingStatisticsResponse200
from ...models.view_yearly_reading_statistics_response_401 import ViewYearlyReadingStatisticsResponse401
from ...models.view_yearly_reading_statistics_response_403 import ViewYearlyReadingStatisticsResponse403
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    year: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["year"] = year

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/user/reading-stats/year",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TooManyRequestsError
    | ViewYearlyReadingStatisticsResponse200
    | ViewYearlyReadingStatisticsResponse401
    | ViewYearlyReadingStatisticsResponse403
    | None
):
    if response.status_code == 200:
        response_200 = ViewYearlyReadingStatisticsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ViewYearlyReadingStatisticsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ViewYearlyReadingStatisticsResponse403.from_dict(response.json())

        return response_403

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
    TooManyRequestsError
    | ViewYearlyReadingStatisticsResponse200
    | ViewYearlyReadingStatisticsResponse401
    | ViewYearlyReadingStatisticsResponse403
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    year: int | Unset = UNSET,
) -> Response[
    TooManyRequestsError
    | ViewYearlyReadingStatisticsResponse200
    | ViewYearlyReadingStatisticsResponse401
    | ViewYearlyReadingStatisticsResponse403
]:
    """View yearly reading statistics.

     Pro feature. Includes goal progress, daily and monthly counts, pace,
    streaks, rankings and completed series for the authenticated member.

    Args:
        year (int | Unset): UTC year; defaults to the current year.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TooManyRequestsError | ViewYearlyReadingStatisticsResponse200 | ViewYearlyReadingStatisticsResponse401 | ViewYearlyReadingStatisticsResponse403]
    """

    kwargs = _get_kwargs(
        year=year,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    year: int | Unset = UNSET,
) -> (
    TooManyRequestsError
    | ViewYearlyReadingStatisticsResponse200
    | ViewYearlyReadingStatisticsResponse401
    | ViewYearlyReadingStatisticsResponse403
    | None
):
    """View yearly reading statistics.

     Pro feature. Includes goal progress, daily and monthly counts, pace,
    streaks, rankings and completed series for the authenticated member.

    Args:
        year (int | Unset): UTC year; defaults to the current year.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TooManyRequestsError | ViewYearlyReadingStatisticsResponse200 | ViewYearlyReadingStatisticsResponse401 | ViewYearlyReadingStatisticsResponse403
    """

    return sync_detailed(
        client=client,
        year=year,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    year: int | Unset = UNSET,
) -> Response[
    TooManyRequestsError
    | ViewYearlyReadingStatisticsResponse200
    | ViewYearlyReadingStatisticsResponse401
    | ViewYearlyReadingStatisticsResponse403
]:
    """View yearly reading statistics.

     Pro feature. Includes goal progress, daily and monthly counts, pace,
    streaks, rankings and completed series for the authenticated member.

    Args:
        year (int | Unset): UTC year; defaults to the current year.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TooManyRequestsError | ViewYearlyReadingStatisticsResponse200 | ViewYearlyReadingStatisticsResponse401 | ViewYearlyReadingStatisticsResponse403]
    """

    kwargs = _get_kwargs(
        year=year,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    year: int | Unset = UNSET,
) -> (
    TooManyRequestsError
    | ViewYearlyReadingStatisticsResponse200
    | ViewYearlyReadingStatisticsResponse401
    | ViewYearlyReadingStatisticsResponse403
    | None
):
    """View yearly reading statistics.

     Pro feature. Includes goal progress, daily and monthly counts, pace,
    streaks, rankings and completed series for the authenticated member.

    Args:
        year (int | Unset): UTC year; defaults to the current year.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TooManyRequestsError | ViewYearlyReadingStatisticsResponse200 | ViewYearlyReadingStatisticsResponse401 | ViewYearlyReadingStatisticsResponse403
    """

    return (
        await asyncio_detailed(
            client=client,
            year=year,
        )
    ).parsed
