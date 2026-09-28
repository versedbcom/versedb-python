from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_all_publishers_with_optional_search_response_200 import (
    ListAllPublishersWithOptionalSearchResponse200,
)
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    medium: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["medium"] = medium

    params["sort"] = sort

    params["direction"] = direction

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/publishers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListAllPublishersWithOptionalSearchResponse200 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = ListAllPublishersWithOptionalSearchResponse200.from_dict(response.json())

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
) -> Response[ListAllPublishersWithOptionalSearchResponse200 | TooManyRequestsError | UnauthorizedError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    medium: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ListAllPublishersWithOptionalSearchResponse200 | TooManyRequestsError | UnauthorizedError]:
    """List all publishers with optional search

     Returns: id, name, founded_year, headquarters, status, logo_url

    Args:
        q (str | Unset): Search by publisher name.
        medium (str | Unset): Filter by primary medium (comic, manga, manhwa, manhua,
            bande_dessinee, magazine).
        sort (str | Unset): Sort field (name, founded_year, cached_titles_count,
            cached_series_count, cached_issues_count). Passing sort replaces the relevance ordering
            applied to q results.
        direction (str | Unset): Sort direction (asc, desc).
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAllPublishersWithOptionalSearchResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        q=q,
        medium=medium,
        sort=sort,
        direction=direction,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    medium: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ListAllPublishersWithOptionalSearchResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """List all publishers with optional search

     Returns: id, name, founded_year, headquarters, status, logo_url

    Args:
        q (str | Unset): Search by publisher name.
        medium (str | Unset): Filter by primary medium (comic, manga, manhwa, manhua,
            bande_dessinee, magazine).
        sort (str | Unset): Sort field (name, founded_year, cached_titles_count,
            cached_series_count, cached_issues_count). Passing sort replaces the relevance ordering
            applied to q results.
        direction (str | Unset): Sort direction (asc, desc).
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAllPublishersWithOptionalSearchResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        client=client,
        q=q,
        medium=medium,
        sort=sort,
        direction=direction,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    medium: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ListAllPublishersWithOptionalSearchResponse200 | TooManyRequestsError | UnauthorizedError]:
    """List all publishers with optional search

     Returns: id, name, founded_year, headquarters, status, logo_url

    Args:
        q (str | Unset): Search by publisher name.
        medium (str | Unset): Filter by primary medium (comic, manga, manhwa, manhua,
            bande_dessinee, magazine).
        sort (str | Unset): Sort field (name, founded_year, cached_titles_count,
            cached_series_count, cached_issues_count). Passing sort replaces the relevance ordering
            applied to q results.
        direction (str | Unset): Sort direction (asc, desc).
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAllPublishersWithOptionalSearchResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        q=q,
        medium=medium,
        sort=sort,
        direction=direction,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    medium: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ListAllPublishersWithOptionalSearchResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """List all publishers with optional search

     Returns: id, name, founded_year, headquarters, status, logo_url

    Args:
        q (str | Unset): Search by publisher name.
        medium (str | Unset): Filter by primary medium (comic, manga, manhwa, manhua,
            bande_dessinee, magazine).
        sort (str | Unset): Sort field (name, founded_year, cached_titles_count,
            cached_series_count, cached_issues_count). Passing sort replaces the relevance ordering
            applied to q results.
        direction (str | Unset): Sort direction (asc, desc).
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAllPublishersWithOptionalSearchResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            medium=medium,
            sort=sort,
            direction=direction,
            limit=limit,
        )
    ).parsed
