from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_titles_response_200 import ListTitlesResponse200
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    publisher_id: int | Unset = UNSET,
    publisher: int | Unset = UNSET,
    publisher_ids: str | Unset = UNSET,
    hide_unreleased: bool | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["publisher_id"] = publisher_id

    params["publisher"] = publisher

    params["publisher_ids"] = publisher_ids

    params["hide_unreleased"] = hide_unreleased

    params["sort"] = sort

    params["direction"] = direction

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/titles",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListTitlesResponse200 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = ListTitlesResponse200.from_dict(response.json())

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
) -> Response[ListTitlesResponse200 | TooManyRequestsError | UnauthorizedError]:
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
    publisher_id: int | Unset = UNSET,
    publisher: int | Unset = UNSET,
    publisher_ids: str | Unset = UNSET,
    hide_unreleased: bool | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ListTitlesResponse200 | TooManyRequestsError | UnauthorizedError]:
    """List titles

     Returns: id, name, slug, start_year, end_year, status, type, image_url,
    content_rating_label, min_age, is_nsfw, series_count, issues_count,
    average_rating, total_reviews

    Args:
        q (str | Unset): Search by title name.
        publisher_id (int | Unset): Filter by publisher ID.
        publisher (int | Unset): Deprecated alias for publisher_id, kept for existing callers.
        publisher_ids (str | Unset): Comma-separated publisher IDs. Returns a title published by
            any one of them.
        hide_unreleased (bool | Unset): Return only titles whose start year has already arrived.
        sort (str | Unset): Sort field. One of name, start_year, average_rating,
            cached_series_count, cached_issues_count; anything else falls back to name. Passing sort
            replaces the relevance ordering applied to q results.
        direction (str | Unset): Sort direction, asc or desc. Anything else falls back to asc.
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListTitlesResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        q=q,
        publisher_id=publisher_id,
        publisher=publisher,
        publisher_ids=publisher_ids,
        hide_unreleased=hide_unreleased,
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
    publisher_id: int | Unset = UNSET,
    publisher: int | Unset = UNSET,
    publisher_ids: str | Unset = UNSET,
    hide_unreleased: bool | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ListTitlesResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """List titles

     Returns: id, name, slug, start_year, end_year, status, type, image_url,
    content_rating_label, min_age, is_nsfw, series_count, issues_count,
    average_rating, total_reviews

    Args:
        q (str | Unset): Search by title name.
        publisher_id (int | Unset): Filter by publisher ID.
        publisher (int | Unset): Deprecated alias for publisher_id, kept for existing callers.
        publisher_ids (str | Unset): Comma-separated publisher IDs. Returns a title published by
            any one of them.
        hide_unreleased (bool | Unset): Return only titles whose start year has already arrived.
        sort (str | Unset): Sort field. One of name, start_year, average_rating,
            cached_series_count, cached_issues_count; anything else falls back to name. Passing sort
            replaces the relevance ordering applied to q results.
        direction (str | Unset): Sort direction, asc or desc. Anything else falls back to asc.
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListTitlesResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        client=client,
        q=q,
        publisher_id=publisher_id,
        publisher=publisher,
        publisher_ids=publisher_ids,
        hide_unreleased=hide_unreleased,
        sort=sort,
        direction=direction,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    publisher_id: int | Unset = UNSET,
    publisher: int | Unset = UNSET,
    publisher_ids: str | Unset = UNSET,
    hide_unreleased: bool | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ListTitlesResponse200 | TooManyRequestsError | UnauthorizedError]:
    """List titles

     Returns: id, name, slug, start_year, end_year, status, type, image_url,
    content_rating_label, min_age, is_nsfw, series_count, issues_count,
    average_rating, total_reviews

    Args:
        q (str | Unset): Search by title name.
        publisher_id (int | Unset): Filter by publisher ID.
        publisher (int | Unset): Deprecated alias for publisher_id, kept for existing callers.
        publisher_ids (str | Unset): Comma-separated publisher IDs. Returns a title published by
            any one of them.
        hide_unreleased (bool | Unset): Return only titles whose start year has already arrived.
        sort (str | Unset): Sort field. One of name, start_year, average_rating,
            cached_series_count, cached_issues_count; anything else falls back to name. Passing sort
            replaces the relevance ordering applied to q results.
        direction (str | Unset): Sort direction, asc or desc. Anything else falls back to asc.
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListTitlesResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        q=q,
        publisher_id=publisher_id,
        publisher=publisher,
        publisher_ids=publisher_ids,
        hide_unreleased=hide_unreleased,
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
    publisher_id: int | Unset = UNSET,
    publisher: int | Unset = UNSET,
    publisher_ids: str | Unset = UNSET,
    hide_unreleased: bool | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ListTitlesResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """List titles

     Returns: id, name, slug, start_year, end_year, status, type, image_url,
    content_rating_label, min_age, is_nsfw, series_count, issues_count,
    average_rating, total_reviews

    Args:
        q (str | Unset): Search by title name.
        publisher_id (int | Unset): Filter by publisher ID.
        publisher (int | Unset): Deprecated alias for publisher_id, kept for existing callers.
        publisher_ids (str | Unset): Comma-separated publisher IDs. Returns a title published by
            any one of them.
        hide_unreleased (bool | Unset): Return only titles whose start year has already arrived.
        sort (str | Unset): Sort field. One of name, start_year, average_rating,
            cached_series_count, cached_issues_count; anything else falls back to name. Passing sort
            replaces the relevance ordering applied to q results.
        direction (str | Unset): Sort direction, asc or desc. Anything else falls back to asc.
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListTitlesResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            publisher_id=publisher_id,
            publisher=publisher,
            publisher_ids=publisher_ids,
            hide_unreleased=hide_unreleased,
            sort=sort,
            direction=direction,
            limit=limit,
        )
    ).parsed
