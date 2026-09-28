from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remove_item_from_list_response_403 import RemoveItemFromListResponse403
from ...models.remove_item_from_list_response_404 import RemoveItemFromListResponse404
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import Response


def _get_kwargs(
    list_id: int,
    item_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/lists/{list_id}/items/{item_id}".format(
            list_id=quote(str(list_id), safe=""),
            item_id=quote(str(item_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | RemoveItemFromListResponse403
    | RemoveItemFromListResponse404
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
        response_403 = RemoveItemFromListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RemoveItemFromListResponse404.from_dict(response.json())

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
    Any | RemoveItemFromListResponse403 | RemoveItemFromListResponse404 | TooManyRequestsError | UnauthorizedError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    list_id: int,
    item_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | RemoveItemFromListResponse403 | RemoveItemFromListResponse404 | TooManyRequestsError | UnauthorizedError
]:
    """Remove item from list.

     Removes an item from a list. Other items' positions are automatically adjusted.

    Args:
        list_id (int):
        item_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RemoveItemFromListResponse403 | RemoveItemFromListResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        item_id=item_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    list_id: int,
    item_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | RemoveItemFromListResponse403
    | RemoveItemFromListResponse404
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Remove item from list.

     Removes an item from a list. Other items' positions are automatically adjusted.

    Args:
        list_id (int):
        item_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RemoveItemFromListResponse403 | RemoveItemFromListResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        list_id=list_id,
        item_id=item_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    list_id: int,
    item_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | RemoveItemFromListResponse403 | RemoveItemFromListResponse404 | TooManyRequestsError | UnauthorizedError
]:
    """Remove item from list.

     Removes an item from a list. Other items' positions are automatically adjusted.

    Args:
        list_id (int):
        item_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RemoveItemFromListResponse403 | RemoveItemFromListResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        item_id=item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    list_id: int,
    item_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | RemoveItemFromListResponse403
    | RemoveItemFromListResponse404
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Remove item from list.

     Removes an item from a list. Other items' positions are automatically adjusted.

    Args:
        list_id (int):
        item_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RemoveItemFromListResponse403 | RemoveItemFromListResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            item_id=item_id,
            client=client,
        )
    ).parsed
