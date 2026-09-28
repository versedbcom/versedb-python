from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_series_issues_response_200 import GetSeriesIssuesResponse200
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["sort"] = sort

    params["direction"] = direction

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/series/{id}/issues".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetSeriesIssuesResponse200 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = GetSeriesIssuesResponse200.from_dict(response.json())

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
) -> Response[GetSeriesIssuesResponse200 | TooManyRequestsError | UnauthorizedError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[GetSeriesIssuesResponse200 | TooManyRequestsError | UnauthorizedError]:
    """Get series issues.

     Returns paginated issues for a specific series.

    Args:
        id (int):
        q (str | Unset): Search within this series' issues (number, name).
        sort (str | Unset): Sort field (issue_number, release_date, name).
        direction (str | Unset): Sort direction (asc, desc).
        limit (int | Unset): Results per page (max 100).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSeriesIssuesResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        id=id,
        q=q,
        sort=sort,
        direction=direction,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> GetSeriesIssuesResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """Get series issues.

     Returns paginated issues for a specific series.

    Args:
        id (int):
        q (str | Unset): Search within this series' issues (number, name).
        sort (str | Unset): Sort field (issue_number, release_date, name).
        direction (str | Unset): Sort direction (asc, desc).
        limit (int | Unset): Results per page (max 100).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSeriesIssuesResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        id=id,
        client=client,
        q=q,
        sort=sort,
        direction=direction,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[GetSeriesIssuesResponse200 | TooManyRequestsError | UnauthorizedError]:
    """Get series issues.

     Returns paginated issues for a specific series.

    Args:
        id (int):
        q (str | Unset): Search within this series' issues (number, name).
        sort (str | Unset): Sort field (issue_number, release_date, name).
        direction (str | Unset): Sort direction (asc, desc).
        limit (int | Unset): Results per page (max 100).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSeriesIssuesResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        id=id,
        q=q,
        sort=sort,
        direction=direction,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> GetSeriesIssuesResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """Get series issues.

     Returns paginated issues for a specific series.

    Args:
        id (int):
        q (str | Unset): Search within this series' issues (number, name).
        sort (str | Unset): Sort field (issue_number, release_date, name).
        direction (str | Unset): Sort direction (asc, desc).
        limit (int | Unset): Results per page (max 100).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSeriesIssuesResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            q=q,
            sort=sort,
            direction=direction,
            limit=limit,
        )
    ).parsed
