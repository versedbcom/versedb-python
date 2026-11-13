from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.check_follow_status_response_200 import CheckFollowStatusResponse200
from ...models.check_follow_status_response_400 import CheckFollowStatusResponse400
from ...models.check_follow_status_response_403 import CheckFollowStatusResponse403
from ...models.check_follow_status_response_404 import CheckFollowStatusResponse404
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import Response


def _get_kwargs(
    type_: str,
    id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/follow/{type_}/{id}/check".format(
            type_=quote(str(type_), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CheckFollowStatusResponse200
    | CheckFollowStatusResponse400
    | CheckFollowStatusResponse403
    | CheckFollowStatusResponse404
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    if response.status_code == 200:
        response_200 = CheckFollowStatusResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CheckFollowStatusResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = CheckFollowStatusResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CheckFollowStatusResponse404.from_dict(response.json())

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
) -> Response[
    CheckFollowStatusResponse200
    | CheckFollowStatusResponse400
    | CheckFollowStatusResponse403
    | CheckFollowStatusResponse404
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
    type_: str,
    id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    CheckFollowStatusResponse200
    | CheckFollowStatusResponse400
    | CheckFollowStatusResponse403
    | CheckFollowStatusResponse404
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Check follow status.

     Reports whether the authenticated user currently follows the given entity. An event in a franchise
    counts as followed when the franchise is.

    Args:
        type_ (str): The content type (title, character, podcast, creator, publisher, team,
            story_arc, comic_shop, event, event_franchise, user).
        id (int): The ID of the content.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckFollowStatusResponse200 | CheckFollowStatusResponse400 | CheckFollowStatusResponse403 | CheckFollowStatusResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        type_=type_,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    type_: str,
    id: int,
    *,
    client: AuthenticatedClient | Client,
) -> (
    CheckFollowStatusResponse200
    | CheckFollowStatusResponse400
    | CheckFollowStatusResponse403
    | CheckFollowStatusResponse404
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Check follow status.

     Reports whether the authenticated user currently follows the given entity. An event in a franchise
    counts as followed when the franchise is.

    Args:
        type_ (str): The content type (title, character, podcast, creator, publisher, team,
            story_arc, comic_shop, event, event_franchise, user).
        id (int): The ID of the content.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckFollowStatusResponse200 | CheckFollowStatusResponse400 | CheckFollowStatusResponse403 | CheckFollowStatusResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        type_=type_,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    type_: str,
    id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    CheckFollowStatusResponse200
    | CheckFollowStatusResponse400
    | CheckFollowStatusResponse403
    | CheckFollowStatusResponse404
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Check follow status.

     Reports whether the authenticated user currently follows the given entity. An event in a franchise
    counts as followed when the franchise is.

    Args:
        type_ (str): The content type (title, character, podcast, creator, publisher, team,
            story_arc, comic_shop, event, event_franchise, user).
        id (int): The ID of the content.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckFollowStatusResponse200 | CheckFollowStatusResponse400 | CheckFollowStatusResponse403 | CheckFollowStatusResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        type_=type_,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type_: str,
    id: int,
    *,
    client: AuthenticatedClient | Client,
) -> (
    CheckFollowStatusResponse200
    | CheckFollowStatusResponse400
    | CheckFollowStatusResponse403
    | CheckFollowStatusResponse404
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Check follow status.

     Reports whether the authenticated user currently follows the given entity. An event in a franchise
    counts as followed when the franchise is.

    Args:
        type_ (str): The content type (title, character, podcast, creator, publisher, team,
            story_arc, comic_shop, event, event_franchise, user).
        id (int): The ID of the content.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckFollowStatusResponse200 | CheckFollowStatusResponse400 | CheckFollowStatusResponse403 | CheckFollowStatusResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            type_=type_,
            id=id,
            client=client,
        )
    ).parsed
