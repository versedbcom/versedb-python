from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_story_arcs_for_a_specific_character_response_200 import GetStoryArcsForASpecificCharacterResponse200
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    character_id: int,
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
        "url": "/api/v1/characters/{character_id}/story-arcs".format(
            character_id=quote(str(character_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetStoryArcsForASpecificCharacterResponse200 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = GetStoryArcsForASpecificCharacterResponse200.from_dict(response.json())

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
) -> Response[GetStoryArcsForASpecificCharacterResponse200 | TooManyRequestsError | UnauthorizedError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    character_id: int,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[GetStoryArcsForASpecificCharacterResponse200 | TooManyRequestsError | UnauthorizedError]:
    """Get story arcs for a specific character

     Returns every story arc the given character appears in.

    Args:
        character_id (int):
        q (str | Unset): Optional case-insensitive search within these results.
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetStoryArcsForASpecificCharacterResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        character_id=character_id,
        q=q,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    character_id: int,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> GetStoryArcsForASpecificCharacterResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """Get story arcs for a specific character

     Returns every story arc the given character appears in.

    Args:
        character_id (int):
        q (str | Unset): Optional case-insensitive search within these results.
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetStoryArcsForASpecificCharacterResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        character_id=character_id,
        client=client,
        q=q,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    character_id: int,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[GetStoryArcsForASpecificCharacterResponse200 | TooManyRequestsError | UnauthorizedError]:
    """Get story arcs for a specific character

     Returns every story arc the given character appears in.

    Args:
        character_id (int):
        q (str | Unset): Optional case-insensitive search within these results.
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetStoryArcsForASpecificCharacterResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        character_id=character_id,
        q=q,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    character_id: int,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> GetStoryArcsForASpecificCharacterResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """Get story arcs for a specific character

     Returns every story arc the given character appears in.

    Args:
        character_id (int):
        q (str | Unset): Optional case-insensitive search within these results.
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetStoryArcsForASpecificCharacterResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            character_id=character_id,
            client=client,
            q=q,
            limit=limit,
        )
    ).parsed
