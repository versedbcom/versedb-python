from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_a_specific_team_response_200 import GetASpecificTeamResponse200
from ...models.get_a_specific_team_response_404 import GetASpecificTeamResponse404
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import Response


def _get_kwargs(
    team_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/teams/{team_id}".format(
            team_id=quote(str(team_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetASpecificTeamResponse200 | GetASpecificTeamResponse404 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = GetASpecificTeamResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetASpecificTeamResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = TooManyRequestsError.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetASpecificTeamResponse200 | GetASpecificTeamResponse404 | TooManyRequestsError | UnauthorizedError]:
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
) -> Response[GetASpecificTeamResponse200 | GetASpecificTeamResponse404 | TooManyRequestsError | UnauthorizedError]:
    """Get a specific team

     Returns team details without relationship data.
    Use the relationship endpoints for related data:
    - /teams/{id}/characters - Get team members
    - /teams/{id}/series - Get team's series appearances
    - /teams/{id}/issues - Get team's issue appearances

    Args:
        team_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetASpecificTeamResponse200 | GetASpecificTeamResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    team_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetASpecificTeamResponse200 | GetASpecificTeamResponse404 | TooManyRequestsError | UnauthorizedError | None:
    """Get a specific team

     Returns team details without relationship data.
    Use the relationship endpoints for related data:
    - /teams/{id}/characters - Get team members
    - /teams/{id}/series - Get team's series appearances
    - /teams/{id}/issues - Get team's issue appearances

    Args:
        team_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetASpecificTeamResponse200 | GetASpecificTeamResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        team_id=team_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    team_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetASpecificTeamResponse200 | GetASpecificTeamResponse404 | TooManyRequestsError | UnauthorizedError]:
    """Get a specific team

     Returns team details without relationship data.
    Use the relationship endpoints for related data:
    - /teams/{id}/characters - Get team members
    - /teams/{id}/series - Get team's series appearances
    - /teams/{id}/issues - Get team's issue appearances

    Args:
        team_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetASpecificTeamResponse200 | GetASpecificTeamResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetASpecificTeamResponse200 | GetASpecificTeamResponse404 | TooManyRequestsError | UnauthorizedError | None:
    """Get a specific team

     Returns team details without relationship data.
    Use the relationship endpoints for related data:
    - /teams/{id}/characters - Get team members
    - /teams/{id}/series - Get team's series appearances
    - /teams/{id}/issues - Get team's issue appearances

    Args:
        team_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetASpecificTeamResponse200 | GetASpecificTeamResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
        )
    ).parsed
