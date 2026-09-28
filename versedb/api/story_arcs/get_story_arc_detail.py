from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_story_arc_detail_response_200 import GetStoryArcDetailResponse200
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import Response


def _get_kwargs(
    story_arc_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/story-arcs/{story_arc_id}".format(
            story_arc_id=quote(str(story_arc_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetStoryArcDetailResponse200 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = GetStoryArcDetailResponse200.from_dict(response.json())

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
) -> Response[GetStoryArcDetailResponse200 | TooManyRequestsError | UnauthorizedError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    story_arc_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetStoryArcDetailResponse200 | TooManyRequestsError | UnauthorizedError]:
    """Get story arc detail.

     Returns full story arc detail with the primary and secondary universes,
    a denormalized characters count, the start/end issue summaries (each
    with its parent series), and the last user who edited the arc.

    Paginated relationship data lives on dedicated nested endpoints:
    - GET /story-arcs/{id}/issues - Issues in the arc, in reading order
    - GET /story-arcs/{id}/series - Series spanned by the arc
    - GET /story-arcs/{id}/characters - Characters appearing in the arc

    Args:
        story_arc_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetStoryArcDetailResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        story_arc_id=story_arc_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    story_arc_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetStoryArcDetailResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """Get story arc detail.

     Returns full story arc detail with the primary and secondary universes,
    a denormalized characters count, the start/end issue summaries (each
    with its parent series), and the last user who edited the arc.

    Paginated relationship data lives on dedicated nested endpoints:
    - GET /story-arcs/{id}/issues - Issues in the arc, in reading order
    - GET /story-arcs/{id}/series - Series spanned by the arc
    - GET /story-arcs/{id}/characters - Characters appearing in the arc

    Args:
        story_arc_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetStoryArcDetailResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        story_arc_id=story_arc_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    story_arc_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetStoryArcDetailResponse200 | TooManyRequestsError | UnauthorizedError]:
    """Get story arc detail.

     Returns full story arc detail with the primary and secondary universes,
    a denormalized characters count, the start/end issue summaries (each
    with its parent series), and the last user who edited the arc.

    Paginated relationship data lives on dedicated nested endpoints:
    - GET /story-arcs/{id}/issues - Issues in the arc, in reading order
    - GET /story-arcs/{id}/series - Series spanned by the arc
    - GET /story-arcs/{id}/characters - Characters appearing in the arc

    Args:
        story_arc_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetStoryArcDetailResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        story_arc_id=story_arc_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    story_arc_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetStoryArcDetailResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """Get story arc detail.

     Returns full story arc detail with the primary and secondary universes,
    a denormalized characters count, the start/end issue summaries (each
    with its parent series), and the last user who edited the arc.

    Paginated relationship data lives on dedicated nested endpoints:
    - GET /story-arcs/{id}/issues - Issues in the arc, in reading order
    - GET /story-arcs/{id}/series - Series spanned by the arc
    - GET /story-arcs/{id}/characters - Characters appearing in the arc

    Args:
        story_arc_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetStoryArcDetailResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            story_arc_id=story_arc_id,
            client=client,
        )
    ).parsed
