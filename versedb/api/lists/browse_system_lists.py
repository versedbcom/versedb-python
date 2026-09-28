from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.browse_system_lists_response_200 import BrowseSystemListsResponse200
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    entity_type: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["entity_type"] = entity_type

    params["sort"] = sort

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/lists/system",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BrowseSystemListsResponse200 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = BrowseSystemListsResponse200.from_dict(response.json())

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
) -> Response[BrowseSystemListsResponse200 | TooManyRequestsError | UnauthorizedError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    entity_type: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[BrowseSystemListsResponse200 | TooManyRequestsError | UnauthorizedError]:
    """Browse system lists.

     Returns platform-curated lists (no user owner). These are editorial picks and featured content.

    Args:
        entity_type (str | Unset): Filter by entity type (issues, series, characters, creators,
            story_arcs, teams).
        sort (str | Unset): Sort order (newest, popular).
        limit (int | Unset): Items per page (max 100).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BrowseSystemListsResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        entity_type=entity_type,
        sort=sort,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    entity_type: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> BrowseSystemListsResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """Browse system lists.

     Returns platform-curated lists (no user owner). These are editorial picks and featured content.

    Args:
        entity_type (str | Unset): Filter by entity type (issues, series, characters, creators,
            story_arcs, teams).
        sort (str | Unset): Sort order (newest, popular).
        limit (int | Unset): Items per page (max 100).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BrowseSystemListsResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        client=client,
        entity_type=entity_type,
        sort=sort,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    entity_type: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[BrowseSystemListsResponse200 | TooManyRequestsError | UnauthorizedError]:
    """Browse system lists.

     Returns platform-curated lists (no user owner). These are editorial picks and featured content.

    Args:
        entity_type (str | Unset): Filter by entity type (issues, series, characters, creators,
            story_arcs, teams).
        sort (str | Unset): Sort order (newest, popular).
        limit (int | Unset): Items per page (max 100).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BrowseSystemListsResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        entity_type=entity_type,
        sort=sort,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    entity_type: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> BrowseSystemListsResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """Browse system lists.

     Returns platform-curated lists (no user owner). These are editorial picks and featured content.

    Args:
        entity_type (str | Unset): Filter by entity type (issues, series, characters, creators,
            story_arcs, teams).
        sort (str | Unset): Sort order (newest, popular).
        limit (int | Unset): Items per page (max 100).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BrowseSystemListsResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            client=client,
            entity_type=entity_type,
            sort=sort,
            limit=limit,
        )
    ).parsed
