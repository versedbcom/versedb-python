from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_item_to_list_body import AddItemToListBody
from ...models.add_item_to_list_response_201 import AddItemToListResponse201
from ...models.add_item_to_list_response_403 import AddItemToListResponse403
from ...models.add_item_to_list_response_409 import AddItemToListResponse409
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import Response


def _get_kwargs(
    list_id: int,
    *,
    body: AddItemToListBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/lists/{list_id}/items".format(
            list_id=quote(str(list_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AddItemToListResponse201
    | AddItemToListResponse403
    | AddItemToListResponse409
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    if response.status_code == 201:
        response_201 = AddItemToListResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AddItemToListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = AddItemToListResponse409.from_dict(response.json())

        return response_409

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
    AddItemToListResponse201
    | AddItemToListResponse403
    | AddItemToListResponse409
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
    list_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: AddItemToListBody,
) -> Response[
    AddItemToListResponse201
    | AddItemToListResponse403
    | AddItemToListResponse409
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Add item to list.

     Adds an entity to a list. Free users: 100 items/list, PRO users: 500 items/list.

    Args:
        list_id (int):
        body (AddItemToListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddItemToListResponse201 | AddItemToListResponse403 | AddItemToListResponse409 | TooManyRequestsError | UnauthorizedError]
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
    body: AddItemToListBody,
) -> (
    AddItemToListResponse201
    | AddItemToListResponse403
    | AddItemToListResponse409
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Add item to list.

     Adds an entity to a list. Free users: 100 items/list, PRO users: 500 items/list.

    Args:
        list_id (int):
        body (AddItemToListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddItemToListResponse201 | AddItemToListResponse403 | AddItemToListResponse409 | TooManyRequestsError | UnauthorizedError
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
    body: AddItemToListBody,
) -> Response[
    AddItemToListResponse201
    | AddItemToListResponse403
    | AddItemToListResponse409
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Add item to list.

     Adds an entity to a list. Free users: 100 items/list, PRO users: 500 items/list.

    Args:
        list_id (int):
        body (AddItemToListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddItemToListResponse201 | AddItemToListResponse403 | AddItemToListResponse409 | TooManyRequestsError | UnauthorizedError]
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
    body: AddItemToListBody,
) -> (
    AddItemToListResponse201
    | AddItemToListResponse403
    | AddItemToListResponse409
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Add item to list.

     Adds an entity to a list. Free users: 100 items/list, PRO users: 500 items/list.

    Args:
        list_id (int):
        body (AddItemToListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddItemToListResponse201 | AddItemToListResponse403 | AddItemToListResponse409 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
            body=body,
        )
    ).parsed
