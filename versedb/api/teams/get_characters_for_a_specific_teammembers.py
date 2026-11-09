from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_characters_for_a_specific_teammembers_response_200 import (
    GetCharactersForASpecificTeammembersResponse200,
)
from ...models.get_characters_for_a_specific_teammembers_response_403 import (
    GetCharactersForASpecificTeammembersResponse403,
)
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
    page: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["sort"] = sort

    params["direction"] = direction

    params["limit"] = limit

    params["page"] = page

    params["languages"] = languages

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/teams/{team_id}/characters".format(
            team_id=quote(str(team_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetCharactersForASpecificTeammembersResponse200
    | GetCharactersForASpecificTeammembersResponse403
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    if response.status_code == 200:
        response_200 = GetCharactersForASpecificTeammembersResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetCharactersForASpecificTeammembersResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 429:
        response_429 = TooManyRequestsError.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetCharactersForASpecificTeammembersResponse200
    | GetCharactersForASpecificTeammembersResponse403
    | TooManyRequestsError
    | UnauthorizedError
]:
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
    page: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> Response[
    GetCharactersForASpecificTeammembersResponse200
    | GetCharactersForASpecificTeammembersResponse403
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Get characters for a specific team (members)

     Returns the team's character roster, by name unless sort says otherwise.

    Args:
        team_id (int): The ID of the team.
        q (str | Unset): Optional search within the team's members. Results come back in relevance
            order unless sort is passed.
        sort (str | Unset): Sort field (name, cached_issues_count, joined_date). Defaults to name.
        direction (str | Unset): Sort direction (asc, desc).
        limit (int | Unset): Number of results per page (max 50).
        page (int | Unset): Page number; meta.last_page says where the list ends.
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCharactersForASpecificTeammembersResponse200 | GetCharactersForASpecificTeammembersResponse403 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        q=q,
        sort=sort,
        direction=direction,
        limit=limit,
        page=page,
        languages=languages,
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
    page: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> (
    GetCharactersForASpecificTeammembersResponse200
    | GetCharactersForASpecificTeammembersResponse403
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Get characters for a specific team (members)

     Returns the team's character roster, by name unless sort says otherwise.

    Args:
        team_id (int): The ID of the team.
        q (str | Unset): Optional search within the team's members. Results come back in relevance
            order unless sort is passed.
        sort (str | Unset): Sort field (name, cached_issues_count, joined_date). Defaults to name.
        direction (str | Unset): Sort direction (asc, desc).
        limit (int | Unset): Number of results per page (max 50).
        page (int | Unset): Page number; meta.last_page says where the list ends.
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCharactersForASpecificTeammembersResponse200 | GetCharactersForASpecificTeammembersResponse403 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        team_id=team_id,
        client=client,
        q=q,
        sort=sort,
        direction=direction,
        limit=limit,
        page=page,
        languages=languages,
    ).parsed


async def asyncio_detailed(
    team_id: int,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> Response[
    GetCharactersForASpecificTeammembersResponse200
    | GetCharactersForASpecificTeammembersResponse403
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Get characters for a specific team (members)

     Returns the team's character roster, by name unless sort says otherwise.

    Args:
        team_id (int): The ID of the team.
        q (str | Unset): Optional search within the team's members. Results come back in relevance
            order unless sort is passed.
        sort (str | Unset): Sort field (name, cached_issues_count, joined_date). Defaults to name.
        direction (str | Unset): Sort direction (asc, desc).
        limit (int | Unset): Number of results per page (max 50).
        page (int | Unset): Page number; meta.last_page says where the list ends.
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCharactersForASpecificTeammembersResponse200 | GetCharactersForASpecificTeammembersResponse403 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        q=q,
        sort=sort,
        direction=direction,
        limit=limit,
        page=page,
        languages=languages,
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
    page: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> (
    GetCharactersForASpecificTeammembersResponse200
    | GetCharactersForASpecificTeammembersResponse403
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Get characters for a specific team (members)

     Returns the team's character roster, by name unless sort says otherwise.

    Args:
        team_id (int): The ID of the team.
        q (str | Unset): Optional search within the team's members. Results come back in relevance
            order unless sort is passed.
        sort (str | Unset): Sort field (name, cached_issues_count, joined_date). Defaults to name.
        direction (str | Unset): Sort direction (asc, desc).
        limit (int | Unset): Number of results per page (max 50).
        page (int | Unset): Page number; meta.last_page says where the list ends.
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCharactersForASpecificTeammembersResponse200 | GetCharactersForASpecificTeammembersResponse403 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            q=q,
            sort=sort,
            direction=direction,
            limit=limit,
            page=page,
            languages=languages,
        )
    ).parsed
