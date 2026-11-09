from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remove_from_pull_list_response_403 import RemoveFromPullListResponse403
from ...models.remove_from_pull_list_response_404 import RemoveFromPullListResponse404
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import Response


def _get_kwargs(
    item_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/pull-list/items/{item_id}".format(
            item_id=quote(str(item_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | RemoveFromPullListResponse403
    | RemoveFromPullListResponse404
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = RemoveFromPullListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RemoveFromPullListResponse404.from_dict(response.json())

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
    Any | RemoveFromPullListResponse403 | RemoveFromPullListResponse404 | TooManyRequestsError | UnauthorizedError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | RemoveFromPullListResponse403 | RemoveFromPullListResponse404 | TooManyRequestsError | UnauthorizedError
]:
    """Remove from pull list.

     Removes a series from the authenticated user's pull list. Idempotent: returns 204 whether or not the
    series was on it.

    Args:
        item_id (int): The series ID of the pull list entry.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RemoveFromPullListResponse403 | RemoveFromPullListResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | RemoveFromPullListResponse403
    | RemoveFromPullListResponse404
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Remove from pull list.

     Removes a series from the authenticated user's pull list. Idempotent: returns 204 whether or not the
    series was on it.

    Args:
        item_id (int): The series ID of the pull list entry.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RemoveFromPullListResponse403 | RemoveFromPullListResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    item_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | RemoveFromPullListResponse403 | RemoveFromPullListResponse404 | TooManyRequestsError | UnauthorizedError
]:
    """Remove from pull list.

     Removes a series from the authenticated user's pull list. Idempotent: returns 204 whether or not the
    series was on it.

    Args:
        item_id (int): The series ID of the pull list entry.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RemoveFromPullListResponse403 | RemoveFromPullListResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | RemoveFromPullListResponse403
    | RemoveFromPullListResponse404
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Remove from pull list.

     Removes a series from the authenticated user's pull list. Idempotent: returns 204 whether or not the
    series was on it.

    Args:
        item_id (int): The series ID of the pull list entry.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RemoveFromPullListResponse403 | RemoveFromPullListResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
        )
    ).parsed
