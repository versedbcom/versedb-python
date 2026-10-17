from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_issues_response_200 import ListIssuesResponse200
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    series_id: int | Unset = UNSET,
    publisher_id: int | Unset = UNSET,
    release_date_from: str | Unset = UNSET,
    release_date_to: str | Unset = UNSET,
    publisher_ids: str | Unset = UNSET,
    series_ids: str | Unset = UNSET,
    title_ids: str | Unset = UNSET,
    character_ids: str | Unset = UNSET,
    creator_ids: str | Unset = UNSET,
    creator_role_ids: str | Unset = UNSET,
    team_ids: str | Unset = UNSET,
    genre_ids: str | Unset = UNSET,
    languages: str | Unset = UNSET,
    medium: str | Unset = UNSET,
    key_issues_only: bool | Unset = UNSET,
    hide_unreleased: bool | Unset = UNSET,
    include: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["series_id"] = series_id

    params["publisher_id"] = publisher_id

    params["release_date_from"] = release_date_from

    params["release_date_to"] = release_date_to

    params["publisher_ids"] = publisher_ids

    params["series_ids"] = series_ids

    params["title_ids"] = title_ids

    params["character_ids"] = character_ids

    params["creator_ids"] = creator_ids

    params["creator_role_ids"] = creator_role_ids

    params["team_ids"] = team_ids

    params["genre_ids"] = genre_ids

    params["languages"] = languages

    params["medium"] = medium

    params["key_issues_only"] = key_issues_only

    params["hide_unreleased"] = hide_unreleased

    params["include"] = include

    params["sort"] = sort

    params["direction"] = direction

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/issues",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListIssuesResponse200 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = ListIssuesResponse200.from_dict(response.json())

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
) -> Response[ListIssuesResponse200 | TooManyRequestsError | UnauthorizedError]:
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
    series_id: int | Unset = UNSET,
    publisher_id: int | Unset = UNSET,
    release_date_from: str | Unset = UNSET,
    release_date_to: str | Unset = UNSET,
    publisher_ids: str | Unset = UNSET,
    series_ids: str | Unset = UNSET,
    title_ids: str | Unset = UNSET,
    character_ids: str | Unset = UNSET,
    creator_ids: str | Unset = UNSET,
    creator_role_ids: str | Unset = UNSET,
    team_ids: str | Unset = UNSET,
    genre_ids: str | Unset = UNSET,
    languages: str | Unset = UNSET,
    medium: str | Unset = UNSET,
    key_issues_only: bool | Unset = UNSET,
    hide_unreleased: bool | Unset = UNSET,
    include: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ListIssuesResponse200 | TooManyRequestsError | UnauthorizedError]:
    """List issues.

     Returns paginated issues with optional search, filtering, and sorting.

    Args:
        q (str | Unset): Search by issue name.
        series_id (int | Unset): Filter by series ID.
        publisher_id (int | Unset): Filter by publisher ID (via series relationship).
        release_date_from (str | Unset): Filter by release date (from).
        release_date_to (str | Unset): Filter by release date (to).
        publisher_ids (str | Unset): Comma-separated publisher IDs; matches issues from any of
            them.
        series_ids (str | Unset): Comma-separated series IDs; matches issues in any of them.
        title_ids (str | Unset): Comma-separated title (franchise) IDs; matches issues whose
            series belongs to any of them.
        character_ids (str | Unset): Comma-separated character IDs, up to 10; an issue must
            feature every one.
        creator_ids (str | Unset): Comma-separated creator IDs, up to 10; an issue must credit
            every one.
        creator_role_ids (str | Unset): Comma-separated creator role IDs; with creator_ids, each
            creator must be credited in one of these roles.
        team_ids (str | Unset): Comma-separated team IDs, up to 10; an issue must feature every
            one.
        genre_ids (str | Unset): Comma-separated genre IDs; matches issues whose series carries
            any of them.
        languages (str | Unset): Comma-separated series language codes (en, ja, fr, ...).
        medium (str | Unset): Series medium (comic, manga, manhwa, manhua, bande_dessinee,
            magazine).
        key_issues_only (bool | Unset): Only return issues with at least one key issue reason.
        hide_unreleased (bool | Unset): Leave out issues whose release date is in the future.
        include (str | Unset): Comma-separated relationships to include (series).
        sort (str | Unset): Sort field (issue_number, release_date, name).
        direction (str | Unset): Sort direction (asc, desc).
        limit (int | Unset): Results per page (max 100).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListIssuesResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        q=q,
        series_id=series_id,
        publisher_id=publisher_id,
        release_date_from=release_date_from,
        release_date_to=release_date_to,
        publisher_ids=publisher_ids,
        series_ids=series_ids,
        title_ids=title_ids,
        character_ids=character_ids,
        creator_ids=creator_ids,
        creator_role_ids=creator_role_ids,
        team_ids=team_ids,
        genre_ids=genre_ids,
        languages=languages,
        medium=medium,
        key_issues_only=key_issues_only,
        hide_unreleased=hide_unreleased,
        include=include,
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
    series_id: int | Unset = UNSET,
    publisher_id: int | Unset = UNSET,
    release_date_from: str | Unset = UNSET,
    release_date_to: str | Unset = UNSET,
    publisher_ids: str | Unset = UNSET,
    series_ids: str | Unset = UNSET,
    title_ids: str | Unset = UNSET,
    character_ids: str | Unset = UNSET,
    creator_ids: str | Unset = UNSET,
    creator_role_ids: str | Unset = UNSET,
    team_ids: str | Unset = UNSET,
    genre_ids: str | Unset = UNSET,
    languages: str | Unset = UNSET,
    medium: str | Unset = UNSET,
    key_issues_only: bool | Unset = UNSET,
    hide_unreleased: bool | Unset = UNSET,
    include: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ListIssuesResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """List issues.

     Returns paginated issues with optional search, filtering, and sorting.

    Args:
        q (str | Unset): Search by issue name.
        series_id (int | Unset): Filter by series ID.
        publisher_id (int | Unset): Filter by publisher ID (via series relationship).
        release_date_from (str | Unset): Filter by release date (from).
        release_date_to (str | Unset): Filter by release date (to).
        publisher_ids (str | Unset): Comma-separated publisher IDs; matches issues from any of
            them.
        series_ids (str | Unset): Comma-separated series IDs; matches issues in any of them.
        title_ids (str | Unset): Comma-separated title (franchise) IDs; matches issues whose
            series belongs to any of them.
        character_ids (str | Unset): Comma-separated character IDs, up to 10; an issue must
            feature every one.
        creator_ids (str | Unset): Comma-separated creator IDs, up to 10; an issue must credit
            every one.
        creator_role_ids (str | Unset): Comma-separated creator role IDs; with creator_ids, each
            creator must be credited in one of these roles.
        team_ids (str | Unset): Comma-separated team IDs, up to 10; an issue must feature every
            one.
        genre_ids (str | Unset): Comma-separated genre IDs; matches issues whose series carries
            any of them.
        languages (str | Unset): Comma-separated series language codes (en, ja, fr, ...).
        medium (str | Unset): Series medium (comic, manga, manhwa, manhua, bande_dessinee,
            magazine).
        key_issues_only (bool | Unset): Only return issues with at least one key issue reason.
        hide_unreleased (bool | Unset): Leave out issues whose release date is in the future.
        include (str | Unset): Comma-separated relationships to include (series).
        sort (str | Unset): Sort field (issue_number, release_date, name).
        direction (str | Unset): Sort direction (asc, desc).
        limit (int | Unset): Results per page (max 100).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListIssuesResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        client=client,
        q=q,
        series_id=series_id,
        publisher_id=publisher_id,
        release_date_from=release_date_from,
        release_date_to=release_date_to,
        publisher_ids=publisher_ids,
        series_ids=series_ids,
        title_ids=title_ids,
        character_ids=character_ids,
        creator_ids=creator_ids,
        creator_role_ids=creator_role_ids,
        team_ids=team_ids,
        genre_ids=genre_ids,
        languages=languages,
        medium=medium,
        key_issues_only=key_issues_only,
        hide_unreleased=hide_unreleased,
        include=include,
        sort=sort,
        direction=direction,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    series_id: int | Unset = UNSET,
    publisher_id: int | Unset = UNSET,
    release_date_from: str | Unset = UNSET,
    release_date_to: str | Unset = UNSET,
    publisher_ids: str | Unset = UNSET,
    series_ids: str | Unset = UNSET,
    title_ids: str | Unset = UNSET,
    character_ids: str | Unset = UNSET,
    creator_ids: str | Unset = UNSET,
    creator_role_ids: str | Unset = UNSET,
    team_ids: str | Unset = UNSET,
    genre_ids: str | Unset = UNSET,
    languages: str | Unset = UNSET,
    medium: str | Unset = UNSET,
    key_issues_only: bool | Unset = UNSET,
    hide_unreleased: bool | Unset = UNSET,
    include: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ListIssuesResponse200 | TooManyRequestsError | UnauthorizedError]:
    """List issues.

     Returns paginated issues with optional search, filtering, and sorting.

    Args:
        q (str | Unset): Search by issue name.
        series_id (int | Unset): Filter by series ID.
        publisher_id (int | Unset): Filter by publisher ID (via series relationship).
        release_date_from (str | Unset): Filter by release date (from).
        release_date_to (str | Unset): Filter by release date (to).
        publisher_ids (str | Unset): Comma-separated publisher IDs; matches issues from any of
            them.
        series_ids (str | Unset): Comma-separated series IDs; matches issues in any of them.
        title_ids (str | Unset): Comma-separated title (franchise) IDs; matches issues whose
            series belongs to any of them.
        character_ids (str | Unset): Comma-separated character IDs, up to 10; an issue must
            feature every one.
        creator_ids (str | Unset): Comma-separated creator IDs, up to 10; an issue must credit
            every one.
        creator_role_ids (str | Unset): Comma-separated creator role IDs; with creator_ids, each
            creator must be credited in one of these roles.
        team_ids (str | Unset): Comma-separated team IDs, up to 10; an issue must feature every
            one.
        genre_ids (str | Unset): Comma-separated genre IDs; matches issues whose series carries
            any of them.
        languages (str | Unset): Comma-separated series language codes (en, ja, fr, ...).
        medium (str | Unset): Series medium (comic, manga, manhwa, manhua, bande_dessinee,
            magazine).
        key_issues_only (bool | Unset): Only return issues with at least one key issue reason.
        hide_unreleased (bool | Unset): Leave out issues whose release date is in the future.
        include (str | Unset): Comma-separated relationships to include (series).
        sort (str | Unset): Sort field (issue_number, release_date, name).
        direction (str | Unset): Sort direction (asc, desc).
        limit (int | Unset): Results per page (max 100).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListIssuesResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        q=q,
        series_id=series_id,
        publisher_id=publisher_id,
        release_date_from=release_date_from,
        release_date_to=release_date_to,
        publisher_ids=publisher_ids,
        series_ids=series_ids,
        title_ids=title_ids,
        character_ids=character_ids,
        creator_ids=creator_ids,
        creator_role_ids=creator_role_ids,
        team_ids=team_ids,
        genre_ids=genre_ids,
        languages=languages,
        medium=medium,
        key_issues_only=key_issues_only,
        hide_unreleased=hide_unreleased,
        include=include,
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
    series_id: int | Unset = UNSET,
    publisher_id: int | Unset = UNSET,
    release_date_from: str | Unset = UNSET,
    release_date_to: str | Unset = UNSET,
    publisher_ids: str | Unset = UNSET,
    series_ids: str | Unset = UNSET,
    title_ids: str | Unset = UNSET,
    character_ids: str | Unset = UNSET,
    creator_ids: str | Unset = UNSET,
    creator_role_ids: str | Unset = UNSET,
    team_ids: str | Unset = UNSET,
    genre_ids: str | Unset = UNSET,
    languages: str | Unset = UNSET,
    medium: str | Unset = UNSET,
    key_issues_only: bool | Unset = UNSET,
    hide_unreleased: bool | Unset = UNSET,
    include: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ListIssuesResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """List issues.

     Returns paginated issues with optional search, filtering, and sorting.

    Args:
        q (str | Unset): Search by issue name.
        series_id (int | Unset): Filter by series ID.
        publisher_id (int | Unset): Filter by publisher ID (via series relationship).
        release_date_from (str | Unset): Filter by release date (from).
        release_date_to (str | Unset): Filter by release date (to).
        publisher_ids (str | Unset): Comma-separated publisher IDs; matches issues from any of
            them.
        series_ids (str | Unset): Comma-separated series IDs; matches issues in any of them.
        title_ids (str | Unset): Comma-separated title (franchise) IDs; matches issues whose
            series belongs to any of them.
        character_ids (str | Unset): Comma-separated character IDs, up to 10; an issue must
            feature every one.
        creator_ids (str | Unset): Comma-separated creator IDs, up to 10; an issue must credit
            every one.
        creator_role_ids (str | Unset): Comma-separated creator role IDs; with creator_ids, each
            creator must be credited in one of these roles.
        team_ids (str | Unset): Comma-separated team IDs, up to 10; an issue must feature every
            one.
        genre_ids (str | Unset): Comma-separated genre IDs; matches issues whose series carries
            any of them.
        languages (str | Unset): Comma-separated series language codes (en, ja, fr, ...).
        medium (str | Unset): Series medium (comic, manga, manhwa, manhua, bande_dessinee,
            magazine).
        key_issues_only (bool | Unset): Only return issues with at least one key issue reason.
        hide_unreleased (bool | Unset): Leave out issues whose release date is in the future.
        include (str | Unset): Comma-separated relationships to include (series).
        sort (str | Unset): Sort field (issue_number, release_date, name).
        direction (str | Unset): Sort direction (asc, desc).
        limit (int | Unset): Results per page (max 100).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListIssuesResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            series_id=series_id,
            publisher_id=publisher_id,
            release_date_from=release_date_from,
            release_date_to=release_date_to,
            publisher_ids=publisher_ids,
            series_ids=series_ids,
            title_ids=title_ids,
            character_ids=character_ids,
            creator_ids=creator_ids,
            creator_role_ids=creator_role_ids,
            team_ids=team_ids,
            genre_ids=genre_ids,
            languages=languages,
            medium=medium,
            key_issues_only=key_issues_only,
            hide_unreleased=hide_unreleased,
            include=include,
            sort=sort,
            direction=direction,
            limit=limit,
        )
    ).parsed
