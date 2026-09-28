from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.follow_updates_response_200 import FollowUpdatesResponse200
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    days: int | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["days"] = days

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/discovery/follow-updates",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FollowUpdatesResponse200 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = FollowUpdatesResponse200.from_dict(response.json())

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
) -> Response[FollowUpdatesResponse200 | TooManyRequestsError | UnauthorizedError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[FollowUpdatesResponse200 | TooManyRequestsError | UnauthorizedError]:
    """Follow updates.

     Returns recent releases from the titles, characters, creators, and teams the user
    follows. A Series is not followable — it reaches this feed through its Title, and
    every volume of that title counts.

    `follow_contexts` and `follow_types` are top-level maps keyed by issue id: the
    context explains why the issue is shown ("New in X-Men"), the type is one of
    `title`, `character`, `creator`, `team`.

    Args:
        days (int | Unset): Lookback window in days (1-90).
        page (int | Unset): Page number for pagination.
        per_page (int | Unset): Items per page (1-50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FollowUpdatesResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        days=days,
        page=page,
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> FollowUpdatesResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """Follow updates.

     Returns recent releases from the titles, characters, creators, and teams the user
    follows. A Series is not followable — it reaches this feed through its Title, and
    every volume of that title counts.

    `follow_contexts` and `follow_types` are top-level maps keyed by issue id: the
    context explains why the issue is shown ("New in X-Men"), the type is one of
    `title`, `character`, `creator`, `team`.

    Args:
        days (int | Unset): Lookback window in days (1-90).
        page (int | Unset): Page number for pagination.
        per_page (int | Unset): Items per page (1-50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FollowUpdatesResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        client=client,
        days=days,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[FollowUpdatesResponse200 | TooManyRequestsError | UnauthorizedError]:
    """Follow updates.

     Returns recent releases from the titles, characters, creators, and teams the user
    follows. A Series is not followable — it reaches this feed through its Title, and
    every volume of that title counts.

    `follow_contexts` and `follow_types` are top-level maps keyed by issue id: the
    context explains why the issue is shown ("New in X-Men"), the type is one of
    `title`, `character`, `creator`, `team`.

    Args:
        days (int | Unset): Lookback window in days (1-90).
        page (int | Unset): Page number for pagination.
        per_page (int | Unset): Items per page (1-50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FollowUpdatesResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        days=days,
        page=page,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> FollowUpdatesResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """Follow updates.

     Returns recent releases from the titles, characters, creators, and teams the user
    follows. A Series is not followable — it reaches this feed through its Title, and
    every volume of that title counts.

    `follow_contexts` and `follow_types` are top-level maps keyed by issue id: the
    context explains why the issue is shown ("New in X-Men"), the type is one of
    `title`, `character`, `creator`, `team`.

    Args:
        days (int | Unset): Lookback window in days (1-90).
        page (int | Unset): Page number for pagination.
        per_page (int | Unset): Items per page (1-50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FollowUpdatesResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            client=client,
            days=days,
            page=page,
            per_page=per_page,
        )
    ).parsed
