from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_story_arcs_for_a_specific_universe_response_200 import GetStoryArcsForASpecificUniverseResponse200
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    *,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/universes/{universe_id}/story-arcs".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetStoryArcsForASpecificUniverseResponse200 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = GetStoryArcsForASpecificUniverseResponse200.from_dict(response.json())

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
) -> Response[GetStoryArcsForASpecificUniverseResponse200 | TooManyRequestsError | UnauthorizedError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[GetStoryArcsForASpecificUniverseResponse200 | TooManyRequestsError | UnauthorizedError]:
    """Get story arcs for a specific universe

     Returns every story arc that takes place in the given universe.

    Args:
        universe_id (int):
        q (str | Unset): Optional case-insensitive search within these results.
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetStoryArcsForASpecificUniverseResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        q=q,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> GetStoryArcsForASpecificUniverseResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """Get story arcs for a specific universe

     Returns every story arc that takes place in the given universe.

    Args:
        universe_id (int):
        q (str | Unset): Optional case-insensitive search within these results.
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetStoryArcsForASpecificUniverseResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        q=q,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[GetStoryArcsForASpecificUniverseResponse200 | TooManyRequestsError | UnauthorizedError]:
    """Get story arcs for a specific universe

     Returns every story arc that takes place in the given universe.

    Args:
        universe_id (int):
        q (str | Unset): Optional case-insensitive search within these results.
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetStoryArcsForASpecificUniverseResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        q=q,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> GetStoryArcsForASpecificUniverseResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """Get story arcs for a specific universe

     Returns every story arc that takes place in the given universe.

    Args:
        universe_id (int):
        q (str | Unset): Optional case-insensitive search within these results.
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetStoryArcsForASpecificUniverseResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            q=q,
            limit=limit,
        )
    ).parsed
