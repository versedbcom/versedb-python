from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_character_series_response_200 import GetCharacterSeriesResponse200
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    character_id: int,
    *,
    limit: int | Unset = UNSET,
    q: str | Unset = UNSET,
    medium: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["q"] = q

    params["medium"] = medium

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/characters/{character_id}/series".format(
            character_id=quote(str(character_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCharacterSeriesResponse200 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = GetCharacterSeriesResponse200.from_dict(response.json())

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
) -> Response[GetCharacterSeriesResponse200 | TooManyRequestsError | UnauthorizedError]:
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
    limit: int | Unset = UNSET,
    q: str | Unset = UNSET,
    medium: str | Unset = UNSET,
) -> Response[GetCharacterSeriesResponse200 | TooManyRequestsError | UnauthorizedError]:
    """Get character series.

     Returns paginated series where the character appears.

    Args:
        character_id (int):
        limit (int | Unset): Results per page (max 50).
        q (str | Unset): Optional case-insensitive search within these results.
        medium (str | Unset): Comma-separated series mediums to filter by (comic, manga, manhwa,
            manhua, bande_dessinee, magazine).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCharacterSeriesResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        character_id=character_id,
        limit=limit,
        q=q,
        medium=medium,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    character_id: int,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    q: str | Unset = UNSET,
    medium: str | Unset = UNSET,
) -> GetCharacterSeriesResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """Get character series.

     Returns paginated series where the character appears.

    Args:
        character_id (int):
        limit (int | Unset): Results per page (max 50).
        q (str | Unset): Optional case-insensitive search within these results.
        medium (str | Unset): Comma-separated series mediums to filter by (comic, manga, manhwa,
            manhua, bande_dessinee, magazine).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCharacterSeriesResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        character_id=character_id,
        client=client,
        limit=limit,
        q=q,
        medium=medium,
    ).parsed


async def asyncio_detailed(
    character_id: int,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    q: str | Unset = UNSET,
    medium: str | Unset = UNSET,
) -> Response[GetCharacterSeriesResponse200 | TooManyRequestsError | UnauthorizedError]:
    """Get character series.

     Returns paginated series where the character appears.

    Args:
        character_id (int):
        limit (int | Unset): Results per page (max 50).
        q (str | Unset): Optional case-insensitive search within these results.
        medium (str | Unset): Comma-separated series mediums to filter by (comic, manga, manhwa,
            manhua, bande_dessinee, magazine).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCharacterSeriesResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        character_id=character_id,
        limit=limit,
        q=q,
        medium=medium,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    character_id: int,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    q: str | Unset = UNSET,
    medium: str | Unset = UNSET,
) -> GetCharacterSeriesResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """Get character series.

     Returns paginated series where the character appears.

    Args:
        character_id (int):
        limit (int | Unset): Results per page (max 50).
        q (str | Unset): Optional case-insensitive search within these results.
        medium (str | Unset): Comma-separated series mediums to filter by (comic, manga, manhwa,
            manhua, bande_dessinee, magazine).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCharacterSeriesResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            character_id=character_id,
            client=client,
            limit=limit,
            q=q,
            medium=medium,
        )
    ).parsed
