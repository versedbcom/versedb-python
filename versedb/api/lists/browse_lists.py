from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.browse_lists_response_200 import BrowseListsResponse200
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    entity_type: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["entity_type"] = entity_type

    params["type"] = type_

    params["sort"] = sort

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/lists",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BrowseListsResponse200 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = BrowseListsResponse200.from_dict(response.json())

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
) -> Response[BrowseListsResponse200 | TooManyRequestsError | UnauthorizedError]:
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
    entity_type: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[BrowseListsResponse200 | TooManyRequestsError | UnauthorizedError]:
    """Browse lists.

     Returns paginated public lists with filtering and sorting options.
    Only shows lists with at least one item.

    Args:
        q (str | Unset): Search by list title or description, tolerating small typos in the title.
        entity_type (str | Unset): Filter by entity type (issues, series, characters, creators,
            story_arcs, teams). Matches lists declared as that type plus unrestricted lists holding at
            least one item of it.
        type_ (str | Unset): Filter by who made it — `curated` for staff lists, `community` for
            everyone else. Omit for both.
        sort (str | Unset): Sort order (featured, newest, popular, most_saved). Default: featured.
        limit (int | Unset): Items per page (max 100).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BrowseListsResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        q=q,
        entity_type=entity_type,
        type_=type_,
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
    q: str | Unset = UNSET,
    entity_type: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> BrowseListsResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """Browse lists.

     Returns paginated public lists with filtering and sorting options.
    Only shows lists with at least one item.

    Args:
        q (str | Unset): Search by list title or description, tolerating small typos in the title.
        entity_type (str | Unset): Filter by entity type (issues, series, characters, creators,
            story_arcs, teams). Matches lists declared as that type plus unrestricted lists holding at
            least one item of it.
        type_ (str | Unset): Filter by who made it — `curated` for staff lists, `community` for
            everyone else. Omit for both.
        sort (str | Unset): Sort order (featured, newest, popular, most_saved). Default: featured.
        limit (int | Unset): Items per page (max 100).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BrowseListsResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        client=client,
        q=q,
        entity_type=entity_type,
        type_=type_,
        sort=sort,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    entity_type: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[BrowseListsResponse200 | TooManyRequestsError | UnauthorizedError]:
    """Browse lists.

     Returns paginated public lists with filtering and sorting options.
    Only shows lists with at least one item.

    Args:
        q (str | Unset): Search by list title or description, tolerating small typos in the title.
        entity_type (str | Unset): Filter by entity type (issues, series, characters, creators,
            story_arcs, teams). Matches lists declared as that type plus unrestricted lists holding at
            least one item of it.
        type_ (str | Unset): Filter by who made it — `curated` for staff lists, `community` for
            everyone else. Omit for both.
        sort (str | Unset): Sort order (featured, newest, popular, most_saved). Default: featured.
        limit (int | Unset): Items per page (max 100).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BrowseListsResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        q=q,
        entity_type=entity_type,
        type_=type_,
        sort=sort,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    entity_type: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> BrowseListsResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """Browse lists.

     Returns paginated public lists with filtering and sorting options.
    Only shows lists with at least one item.

    Args:
        q (str | Unset): Search by list title or description, tolerating small typos in the title.
        entity_type (str | Unset): Filter by entity type (issues, series, characters, creators,
            story_arcs, teams). Matches lists declared as that type plus unrestricted lists holding at
            least one item of it.
        type_ (str | Unset): Filter by who made it — `curated` for staff lists, `community` for
            everyone else. Omit for both.
        sort (str | Unset): Sort order (featured, newest, popular, most_saved). Default: featured.
        limit (int | Unset): Items per page (max 100).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BrowseListsResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            entity_type=entity_type,
            type_=type_,
            sort=sort,
            limit=limit,
        )
    ).parsed
