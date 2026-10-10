from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_issues_for_a_specific_team_response_200 import GetIssuesForASpecificTeamResponse200
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    team_id: int,
    *,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    medium: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["sort"] = sort

    params["direction"] = direction

    params["limit"] = limit

    params["medium"] = medium

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/teams/{team_id}/issues".format(
            team_id=quote(str(team_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetIssuesForASpecificTeamResponse200 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = GetIssuesForASpecificTeamResponse200.from_dict(response.json())

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
) -> Response[GetIssuesForASpecificTeamResponse200 | TooManyRequestsError | UnauthorizedError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_id: int,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    medium: str | Unset = UNSET,
) -> Response[GetIssuesForASpecificTeamResponse200 | TooManyRequestsError | UnauthorizedError]:
    """Get issues for a specific team

     Returns the issues the team appears in, newest release first unless sort says otherwise.

    Args:
        team_id (int):
        q (str | Unset): Optional search within the team's issues. Results come back in relevance
            order unless sort is passed.
        sort (str | Unset): Sort field (release_date, cover_date, average_rating). Defaults to
            release_date.
        direction (str | Unset): Sort direction (asc, desc). Defaults to desc.
        limit (int | Unset): Number of results per page (max 50).
        medium (str | Unset): Comma-separated series mediums to filter by (comic, manga, manhwa,
            manhua, bande_dessinee, magazine).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetIssuesForASpecificTeamResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        q=q,
        sort=sort,
        direction=direction,
        limit=limit,
        medium=medium,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    team_id: int,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    medium: str | Unset = UNSET,
) -> GetIssuesForASpecificTeamResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """Get issues for a specific team

     Returns the issues the team appears in, newest release first unless sort says otherwise.

    Args:
        team_id (int):
        q (str | Unset): Optional search within the team's issues. Results come back in relevance
            order unless sort is passed.
        sort (str | Unset): Sort field (release_date, cover_date, average_rating). Defaults to
            release_date.
        direction (str | Unset): Sort direction (asc, desc). Defaults to desc.
        limit (int | Unset): Number of results per page (max 50).
        medium (str | Unset): Comma-separated series mediums to filter by (comic, manga, manhwa,
            manhua, bande_dessinee, magazine).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetIssuesForASpecificTeamResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        team_id=team_id,
        client=client,
        q=q,
        sort=sort,
        direction=direction,
        limit=limit,
        medium=medium,
    ).parsed


async def asyncio_detailed(
    team_id: int,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    medium: str | Unset = UNSET,
) -> Response[GetIssuesForASpecificTeamResponse200 | TooManyRequestsError | UnauthorizedError]:
    """Get issues for a specific team

     Returns the issues the team appears in, newest release first unless sort says otherwise.

    Args:
        team_id (int):
        q (str | Unset): Optional search within the team's issues. Results come back in relevance
            order unless sort is passed.
        sort (str | Unset): Sort field (release_date, cover_date, average_rating). Defaults to
            release_date.
        direction (str | Unset): Sort direction (asc, desc). Defaults to desc.
        limit (int | Unset): Number of results per page (max 50).
        medium (str | Unset): Comma-separated series mediums to filter by (comic, manga, manhwa,
            manhua, bande_dessinee, magazine).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetIssuesForASpecificTeamResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        q=q,
        sort=sort,
        direction=direction,
        limit=limit,
        medium=medium,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_id: int,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    medium: str | Unset = UNSET,
) -> GetIssuesForASpecificTeamResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """Get issues for a specific team

     Returns the issues the team appears in, newest release first unless sort says otherwise.

    Args:
        team_id (int):
        q (str | Unset): Optional search within the team's issues. Results come back in relevance
            order unless sort is passed.
        sort (str | Unset): Sort field (release_date, cover_date, average_rating). Defaults to
            release_date.
        direction (str | Unset): Sort direction (asc, desc). Defaults to desc.
        limit (int | Unset): Number of results per page (max 50).
        medium (str | Unset): Comma-separated series mediums to filter by (comic, manga, manhwa,
            manhua, bande_dessinee, magazine).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetIssuesForASpecificTeamResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            q=q,
            sort=sort,
            direction=direction,
            limit=limit,
            medium=medium,
        )
    ).parsed
