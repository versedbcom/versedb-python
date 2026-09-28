from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...models.update_list_body import UpdateListBody
from ...models.update_list_response_200 import UpdateListResponse200
from ...models.update_list_response_403 import UpdateListResponse403
from ...types import UNSET, Response, Unset


def _get_kwargs(
    list_id: int,
    *,
    body: UpdateListBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/lists/{list_id}".format(
            list_id=quote(str(list_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TooManyRequestsError | UnauthorizedError | UpdateListResponse200 | UpdateListResponse403 | None:
    if response.status_code == 200:
        response_200 = UpdateListResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UpdateListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 429:
        response_429 = TooManyRequestsError.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TooManyRequestsError | UnauthorizedError | UpdateListResponse200 | UpdateListResponse403]:
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
    body: UpdateListBody | Unset = UNSET,
) -> Response[TooManyRequestsError | UnauthorizedError | UpdateListResponse200 | UpdateListResponse403]:
    """Update list.

     Updates a list's metadata. Wishlists can only update privacy settings.

    Args:
        list_id (int):
        body (UpdateListBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TooManyRequestsError | UnauthorizedError | UpdateListResponse200 | UpdateListResponse403]
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
    body: UpdateListBody | Unset = UNSET,
) -> TooManyRequestsError | UnauthorizedError | UpdateListResponse200 | UpdateListResponse403 | None:
    """Update list.

     Updates a list's metadata. Wishlists can only update privacy settings.

    Args:
        list_id (int):
        body (UpdateListBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TooManyRequestsError | UnauthorizedError | UpdateListResponse200 | UpdateListResponse403
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
    body: UpdateListBody | Unset = UNSET,
) -> Response[TooManyRequestsError | UnauthorizedError | UpdateListResponse200 | UpdateListResponse403]:
    """Update list.

     Updates a list's metadata. Wishlists can only update privacy settings.

    Args:
        list_id (int):
        body (UpdateListBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TooManyRequestsError | UnauthorizedError | UpdateListResponse200 | UpdateListResponse403]
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
    body: UpdateListBody | Unset = UNSET,
) -> TooManyRequestsError | UnauthorizedError | UpdateListResponse200 | UpdateListResponse403 | None:
    """Update list.

     Updates a list's metadata. Wishlists can only update privacy settings.

    Args:
        list_id (int):
        body (UpdateListBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TooManyRequestsError | UnauthorizedError | UpdateListResponse200 | UpdateListResponse403
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
            body=body,
        )
    ).parsed
