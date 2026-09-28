from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.reorder_items_body import ReorderItemsBody
from ...models.reorder_items_response_200 import ReorderItemsResponse200
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import Response


def _get_kwargs(
    list_id: int,
    *,
    body: ReorderItemsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/lists/{list_id}/items/reorder".format(
            list_id=quote(str(list_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ReorderItemsResponse200 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = ReorderItemsResponse200.from_dict(response.json())

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
) -> Response[ReorderItemsResponse200 | TooManyRequestsError | UnauthorizedError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    list_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ReorderItemsBody,
) -> Response[ReorderItemsResponse200 | TooManyRequestsError | UnauthorizedError]:
    """Reorder items.

     Reorders items in a list by providing the new order of item IDs.

    Args:
        list_id (int):
        body (ReorderItemsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReorderItemsResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    list_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ReorderItemsBody,
) -> ReorderItemsResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """Reorder items.

     Reorders items in a list by providing the new order of item IDs.

    Args:
        list_id (int):
        body (ReorderItemsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReorderItemsResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        list_id=list_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    list_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ReorderItemsBody,
) -> Response[ReorderItemsResponse200 | TooManyRequestsError | UnauthorizedError]:
    """Reorder items.

     Reorders items in a list by providing the new order of item IDs.

    Args:
        list_id (int):
        body (ReorderItemsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReorderItemsResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    list_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ReorderItemsBody,
) -> ReorderItemsResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """Reorder items.

     Reorders items in a list by providing the new order of item IDs.

    Args:
        list_id (int):
        body (ReorderItemsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReorderItemsResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
            body=body,
        )
    ).parsed
