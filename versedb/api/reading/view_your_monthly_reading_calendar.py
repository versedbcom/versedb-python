from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.view_your_monthly_reading_calendar_response_200 import ViewYourMonthlyReadingCalendarResponse200
from ...models.view_your_monthly_reading_calendar_response_401 import ViewYourMonthlyReadingCalendarResponse401
from ...models.view_your_monthly_reading_calendar_response_403 import ViewYourMonthlyReadingCalendarResponse403
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    year: int | Unset = UNSET,
    month: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["year"] = year

    params["month"] = month

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/user/reading-stats/calendar",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TooManyRequestsError
    | ViewYourMonthlyReadingCalendarResponse200
    | ViewYourMonthlyReadingCalendarResponse401
    | ViewYourMonthlyReadingCalendarResponse403
    | None
):
    if response.status_code == 200:
        response_200 = ViewYourMonthlyReadingCalendarResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ViewYourMonthlyReadingCalendarResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ViewYourMonthlyReadingCalendarResponse403.from_dict(response.json())

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
    | ViewYourMonthlyReadingCalendarResponse200
    | ViewYourMonthlyReadingCalendarResponse401
    | ViewYourMonthlyReadingCalendarResponse403
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
    month: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Response[
    TooManyRequestsError
    | ViewYourMonthlyReadingCalendarResponse200
    | ViewYourMonthlyReadingCalendarResponse401
    | ViewYourMonthlyReadingCalendarResponse403
]:
    """View your monthly reading calendar.

     Pro feature. Returns up to 60 reads per page, newest first.

    Args:
        year (int | Unset): UTC year; defaults to the current year.
        month (int | Unset): Month from 1 to 12; defaults to the current UTC month.
        page (int | Unset): Page number, starting at 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TooManyRequestsError | ViewYourMonthlyReadingCalendarResponse200 | ViewYourMonthlyReadingCalendarResponse401 | ViewYourMonthlyReadingCalendarResponse403]
    """

    kwargs = _get_kwargs(
        year=year,
        month=month,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    year: int | Unset = UNSET,
    month: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> (
    TooManyRequestsError
    | ViewYourMonthlyReadingCalendarResponse200
    | ViewYourMonthlyReadingCalendarResponse401
    | ViewYourMonthlyReadingCalendarResponse403
    | None
):
    """View your monthly reading calendar.

     Pro feature. Returns up to 60 reads per page, newest first.

    Args:
        year (int | Unset): UTC year; defaults to the current year.
        month (int | Unset): Month from 1 to 12; defaults to the current UTC month.
        page (int | Unset): Page number, starting at 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TooManyRequestsError | ViewYourMonthlyReadingCalendarResponse200 | ViewYourMonthlyReadingCalendarResponse401 | ViewYourMonthlyReadingCalendarResponse403
    """

    return sync_detailed(
        client=client,
        year=year,
        month=month,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    year: int | Unset = UNSET,
    month: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Response[
    TooManyRequestsError
    | ViewYourMonthlyReadingCalendarResponse200
    | ViewYourMonthlyReadingCalendarResponse401
    | ViewYourMonthlyReadingCalendarResponse403
]:
    """View your monthly reading calendar.

     Pro feature. Returns up to 60 reads per page, newest first.

    Args:
        year (int | Unset): UTC year; defaults to the current year.
        month (int | Unset): Month from 1 to 12; defaults to the current UTC month.
        page (int | Unset): Page number, starting at 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TooManyRequestsError | ViewYourMonthlyReadingCalendarResponse200 | ViewYourMonthlyReadingCalendarResponse401 | ViewYourMonthlyReadingCalendarResponse403]
    """

    kwargs = _get_kwargs(
        year=year,
        month=month,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    year: int | Unset = UNSET,
    month: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> (
    TooManyRequestsError
    | ViewYourMonthlyReadingCalendarResponse200
    | ViewYourMonthlyReadingCalendarResponse401
    | ViewYourMonthlyReadingCalendarResponse403
    | None
):
    """View your monthly reading calendar.

     Pro feature. Returns up to 60 reads per page, newest first.

    Args:
        year (int | Unset): UTC year; defaults to the current year.
        month (int | Unset): Month from 1 to 12; defaults to the current UTC month.
        page (int | Unset): Page number, starting at 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TooManyRequestsError | ViewYourMonthlyReadingCalendarResponse200 | ViewYourMonthlyReadingCalendarResponse401 | ViewYourMonthlyReadingCalendarResponse403
    """

    return (
        await asyncio_detailed(
            client=client,
            year=year,
            month=month,
            page=page,
        )
    ).parsed
