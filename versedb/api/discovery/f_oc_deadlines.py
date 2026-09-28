from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.f_oc_deadlines_response_200 import FOcDeadlinesResponse200
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    days: int | Unset = UNSET,
    start_date: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["page"] = page

    params["days"] = days

    params["start_date"] = start_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/discovery/foc",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FOcDeadlinesResponse200 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = FOcDeadlinesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 429:
        response_429 = TooManyRequestsError.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FOcDeadlinesResponse200 | TooManyRequestsError | UnauthorizedError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    days: int | Unset = UNSET,
    start_date: str | Unset = UNSET,
) -> Response[FOcDeadlinesResponse200 | TooManyRequestsError | UnauthorizedError]:
    """FOC deadlines.

     Returns issues with Final Order Cutoff (FOC) deadline within the next N days.
    FOC is when retailers must place final orders with distributors (typically 2 weeks before release).

    Args:
        limit (int | Unset): Results per page (1-50).
        page (int | Unset): Page number; meta.last_page says where the list ends.
        days (int | Unset): FOC window in days (1-30).
        start_date (str | Unset): Start of FOC window (YYYY-MM-DD). Defaults to today.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FOcDeadlinesResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        limit=limit,
        page=page,
        days=days,
        start_date=start_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    days: int | Unset = UNSET,
    start_date: str | Unset = UNSET,
) -> FOcDeadlinesResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """FOC deadlines.

     Returns issues with Final Order Cutoff (FOC) deadline within the next N days.
    FOC is when retailers must place final orders with distributors (typically 2 weeks before release).

    Args:
        limit (int | Unset): Results per page (1-50).
        page (int | Unset): Page number; meta.last_page says where the list ends.
        days (int | Unset): FOC window in days (1-30).
        start_date (str | Unset): Start of FOC window (YYYY-MM-DD). Defaults to today.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FOcDeadlinesResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        client=client,
        limit=limit,
        page=page,
        days=days,
        start_date=start_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    days: int | Unset = UNSET,
    start_date: str | Unset = UNSET,
) -> Response[FOcDeadlinesResponse200 | TooManyRequestsError | UnauthorizedError]:
    """FOC deadlines.

     Returns issues with Final Order Cutoff (FOC) deadline within the next N days.
    FOC is when retailers must place final orders with distributors (typically 2 weeks before release).

    Args:
        limit (int | Unset): Results per page (1-50).
        page (int | Unset): Page number; meta.last_page says where the list ends.
        days (int | Unset): FOC window in days (1-30).
        start_date (str | Unset): Start of FOC window (YYYY-MM-DD). Defaults to today.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FOcDeadlinesResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        limit=limit,
        page=page,
        days=days,
        start_date=start_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    days: int | Unset = UNSET,
    start_date: str | Unset = UNSET,
) -> FOcDeadlinesResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """FOC deadlines.

     Returns issues with Final Order Cutoff (FOC) deadline within the next N days.
    FOC is when retailers must place final orders with distributors (typically 2 weeks before release).

    Args:
        limit (int | Unset): Results per page (1-50).
        page (int | Unset): Page number; meta.last_page says where the list ends.
        days (int | Unset): FOC window in days (1-30).
        start_date (str | Unset): Start of FOC window (YYYY-MM-DD). Defaults to today.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FOcDeadlinesResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            page=page,
            days=days,
            start_date=start_date,
        )
    ).parsed
