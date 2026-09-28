from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_series_response_200 import ListSeriesResponse200
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    title_id: int | Unset = UNSET,
    publisher_id: int | Unset = UNSET,
    status: str | Unset = UNSET,
    genre_ids: str | Unset = UNSET,
    publisher_ids: str | Unset = UNSET,
    creator_ids: str | Unset = UNSET,
    character_ids: str | Unset = UNSET,
    languages: str | Unset = UNSET,
    medium: str | Unset = UNSET,
    publication_type: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    start_year: int | Unset = UNSET,
    end_year: int | Unset = UNSET,
    decade: str | Unset = UNSET,
    hide_unreleased: bool | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["title_id"] = title_id

    params["publisher_id"] = publisher_id

    params["status"] = status

    params["genre_ids"] = genre_ids

    params["publisher_ids"] = publisher_ids

    params["creator_ids"] = creator_ids

    params["character_ids"] = character_ids

    params["languages"] = languages

    params["medium"] = medium

    params["publication_type"] = publication_type

    params["format"] = format_

    params["start_year"] = start_year

    params["end_year"] = end_year

    params["decade"] = decade

    params["hide_unreleased"] = hide_unreleased

    params["sort"] = sort

    params["direction"] = direction

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/series",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListSeriesResponse200 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = ListSeriesResponse200.from_dict(response.json())

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
) -> Response[ListSeriesResponse200 | TooManyRequestsError | UnauthorizedError]:
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
    title_id: int | Unset = UNSET,
    publisher_id: int | Unset = UNSET,
    status: str | Unset = UNSET,
    genre_ids: str | Unset = UNSET,
    publisher_ids: str | Unset = UNSET,
    creator_ids: str | Unset = UNSET,
    character_ids: str | Unset = UNSET,
    languages: str | Unset = UNSET,
    medium: str | Unset = UNSET,
    publication_type: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    start_year: int | Unset = UNSET,
    end_year: int | Unset = UNSET,
    decade: str | Unset = UNSET,
    hide_unreleased: bool | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ListSeriesResponse200 | TooManyRequestsError | UnauthorizedError]:
    """List series.

     Returns paginated series with optional search and filtering.

    Args:
        q (str | Unset): Search by series name.
        title_id (int | Unset): Filter by title ID.
        publisher_id (int | Unset): Filter by publisher ID.
        status (str | Unset): Filter by series status (Ongoing, Completed, Canceled).
        genre_ids (str | Unset): Comma-separated genre IDs. Returns a series carrying any one of
            them.
        publisher_ids (str | Unset): Comma-separated publisher IDs. Returns a series published by
            any one of them; use this instead of publisher_id to pass more than one.
        creator_ids (str | Unset): Comma-separated creator IDs. Returns a series credited to any
            one of them.
        character_ids (str | Unset): Comma-separated character IDs. Returns a series any one of
            them appears in.
        languages (str | Unset): Comma-separated ISO 639-1 language codes. Returns a series
            published in any one of them.
        medium (str | Unset): Filter by medium (comic, manga, manhwa, manhua, bande_dessinee,
            magazine).
        publication_type (str | Unset): Filter by publication type (regular_series,
            limited_series, one_shot, graphic_novel, graphic_novel_series, collected_edition,
            special).
        format_ (str | Unset): Filter by physical format (Standard, Deluxe, Omnibus, TPB,
            Hardcover, Other).
        start_year (int | Unset): Filter by the year the series began.
        end_year (int | Unset): Filter by the year the series ended.
        decade (str | Unset): Filter by the decade the series began, written as a four-digit year
            ending in s. Accepts 1900s through the current decade.
        hide_unreleased (bool | Unset): Return only series whose start year has already arrived.
        sort (str | Unset): Sort field (name, start_year, average_rating, latest_release_date,
            cached_issues_count).
        direction (str | Unset): Sort direction (asc, desc).
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListSeriesResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        q=q,
        title_id=title_id,
        publisher_id=publisher_id,
        status=status,
        genre_ids=genre_ids,
        publisher_ids=publisher_ids,
        creator_ids=creator_ids,
        character_ids=character_ids,
        languages=languages,
        medium=medium,
        publication_type=publication_type,
        format_=format_,
        start_year=start_year,
        end_year=end_year,
        decade=decade,
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
    title_id: int | Unset = UNSET,
    publisher_id: int | Unset = UNSET,
    status: str | Unset = UNSET,
    genre_ids: str | Unset = UNSET,
    publisher_ids: str | Unset = UNSET,
    creator_ids: str | Unset = UNSET,
    character_ids: str | Unset = UNSET,
    languages: str | Unset = UNSET,
    medium: str | Unset = UNSET,
    publication_type: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    start_year: int | Unset = UNSET,
    end_year: int | Unset = UNSET,
    decade: str | Unset = UNSET,
    hide_unreleased: bool | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ListSeriesResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """List series.

     Returns paginated series with optional search and filtering.

    Args:
        q (str | Unset): Search by series name.
        title_id (int | Unset): Filter by title ID.
        publisher_id (int | Unset): Filter by publisher ID.
        status (str | Unset): Filter by series status (Ongoing, Completed, Canceled).
        genre_ids (str | Unset): Comma-separated genre IDs. Returns a series carrying any one of
            them.
        publisher_ids (str | Unset): Comma-separated publisher IDs. Returns a series published by
            any one of them; use this instead of publisher_id to pass more than one.
        creator_ids (str | Unset): Comma-separated creator IDs. Returns a series credited to any
            one of them.
        character_ids (str | Unset): Comma-separated character IDs. Returns a series any one of
            them appears in.
        languages (str | Unset): Comma-separated ISO 639-1 language codes. Returns a series
            published in any one of them.
        medium (str | Unset): Filter by medium (comic, manga, manhwa, manhua, bande_dessinee,
            magazine).
        publication_type (str | Unset): Filter by publication type (regular_series,
            limited_series, one_shot, graphic_novel, graphic_novel_series, collected_edition,
            special).
        format_ (str | Unset): Filter by physical format (Standard, Deluxe, Omnibus, TPB,
            Hardcover, Other).
        start_year (int | Unset): Filter by the year the series began.
        end_year (int | Unset): Filter by the year the series ended.
        decade (str | Unset): Filter by the decade the series began, written as a four-digit year
            ending in s. Accepts 1900s through the current decade.
        hide_unreleased (bool | Unset): Return only series whose start year has already arrived.
        sort (str | Unset): Sort field (name, start_year, average_rating, latest_release_date,
            cached_issues_count).
        direction (str | Unset): Sort direction (asc, desc).
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListSeriesResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        client=client,
        q=q,
        title_id=title_id,
        publisher_id=publisher_id,
        status=status,
        genre_ids=genre_ids,
        publisher_ids=publisher_ids,
        creator_ids=creator_ids,
        character_ids=character_ids,
        languages=languages,
        medium=medium,
        publication_type=publication_type,
        format_=format_,
        start_year=start_year,
        end_year=end_year,
        decade=decade,
        hide_unreleased=hide_unreleased,
        sort=sort,
        direction=direction,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    title_id: int | Unset = UNSET,
    publisher_id: int | Unset = UNSET,
    status: str | Unset = UNSET,
    genre_ids: str | Unset = UNSET,
    publisher_ids: str | Unset = UNSET,
    creator_ids: str | Unset = UNSET,
    character_ids: str | Unset = UNSET,
    languages: str | Unset = UNSET,
    medium: str | Unset = UNSET,
    publication_type: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    start_year: int | Unset = UNSET,
    end_year: int | Unset = UNSET,
    decade: str | Unset = UNSET,
    hide_unreleased: bool | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ListSeriesResponse200 | TooManyRequestsError | UnauthorizedError]:
    """List series.

     Returns paginated series with optional search and filtering.

    Args:
        q (str | Unset): Search by series name.
        title_id (int | Unset): Filter by title ID.
        publisher_id (int | Unset): Filter by publisher ID.
        status (str | Unset): Filter by series status (Ongoing, Completed, Canceled).
        genre_ids (str | Unset): Comma-separated genre IDs. Returns a series carrying any one of
            them.
        publisher_ids (str | Unset): Comma-separated publisher IDs. Returns a series published by
            any one of them; use this instead of publisher_id to pass more than one.
        creator_ids (str | Unset): Comma-separated creator IDs. Returns a series credited to any
            one of them.
        character_ids (str | Unset): Comma-separated character IDs. Returns a series any one of
            them appears in.
        languages (str | Unset): Comma-separated ISO 639-1 language codes. Returns a series
            published in any one of them.
        medium (str | Unset): Filter by medium (comic, manga, manhwa, manhua, bande_dessinee,
            magazine).
        publication_type (str | Unset): Filter by publication type (regular_series,
            limited_series, one_shot, graphic_novel, graphic_novel_series, collected_edition,
            special).
        format_ (str | Unset): Filter by physical format (Standard, Deluxe, Omnibus, TPB,
            Hardcover, Other).
        start_year (int | Unset): Filter by the year the series began.
        end_year (int | Unset): Filter by the year the series ended.
        decade (str | Unset): Filter by the decade the series began, written as a four-digit year
            ending in s. Accepts 1900s through the current decade.
        hide_unreleased (bool | Unset): Return only series whose start year has already arrived.
        sort (str | Unset): Sort field (name, start_year, average_rating, latest_release_date,
            cached_issues_count).
        direction (str | Unset): Sort direction (asc, desc).
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListSeriesResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        q=q,
        title_id=title_id,
        publisher_id=publisher_id,
        status=status,
        genre_ids=genre_ids,
        publisher_ids=publisher_ids,
        creator_ids=creator_ids,
        character_ids=character_ids,
        languages=languages,
        medium=medium,
        publication_type=publication_type,
        format_=format_,
        start_year=start_year,
        end_year=end_year,
        decade=decade,
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
    title_id: int | Unset = UNSET,
    publisher_id: int | Unset = UNSET,
    status: str | Unset = UNSET,
    genre_ids: str | Unset = UNSET,
    publisher_ids: str | Unset = UNSET,
    creator_ids: str | Unset = UNSET,
    character_ids: str | Unset = UNSET,
    languages: str | Unset = UNSET,
    medium: str | Unset = UNSET,
    publication_type: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    start_year: int | Unset = UNSET,
    end_year: int | Unset = UNSET,
    decade: str | Unset = UNSET,
    hide_unreleased: bool | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ListSeriesResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """List series.

     Returns paginated series with optional search and filtering.

    Args:
        q (str | Unset): Search by series name.
        title_id (int | Unset): Filter by title ID.
        publisher_id (int | Unset): Filter by publisher ID.
        status (str | Unset): Filter by series status (Ongoing, Completed, Canceled).
        genre_ids (str | Unset): Comma-separated genre IDs. Returns a series carrying any one of
            them.
        publisher_ids (str | Unset): Comma-separated publisher IDs. Returns a series published by
            any one of them; use this instead of publisher_id to pass more than one.
        creator_ids (str | Unset): Comma-separated creator IDs. Returns a series credited to any
            one of them.
        character_ids (str | Unset): Comma-separated character IDs. Returns a series any one of
            them appears in.
        languages (str | Unset): Comma-separated ISO 639-1 language codes. Returns a series
            published in any one of them.
        medium (str | Unset): Filter by medium (comic, manga, manhwa, manhua, bande_dessinee,
            magazine).
        publication_type (str | Unset): Filter by publication type (regular_series,
            limited_series, one_shot, graphic_novel, graphic_novel_series, collected_edition,
            special).
        format_ (str | Unset): Filter by physical format (Standard, Deluxe, Omnibus, TPB,
            Hardcover, Other).
        start_year (int | Unset): Filter by the year the series began.
        end_year (int | Unset): Filter by the year the series ended.
        decade (str | Unset): Filter by the decade the series began, written as a four-digit year
            ending in s. Accepts 1900s through the current decade.
        hide_unreleased (bool | Unset): Return only series whose start year has already arrived.
        sort (str | Unset): Sort field (name, start_year, average_rating, latest_release_date,
            cached_issues_count).
        direction (str | Unset): Sort direction (asc, desc).
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListSeriesResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            title_id=title_id,
            publisher_id=publisher_id,
            status=status,
            genre_ids=genre_ids,
            publisher_ids=publisher_ids,
            creator_ids=creator_ids,
            character_ids=character_ids,
            languages=languages,
            medium=medium,
            publication_type=publication_type,
            format_=format_,
            start_year=start_year,
            end_year=end_year,
            decade=decade,
            hide_unreleased=hide_unreleased,
            sort=sort,
            direction=direction,
            limit=limit,
        )
    ).parsed
