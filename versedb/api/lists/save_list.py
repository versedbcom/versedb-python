from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.save_list_response_200 import SaveListResponse200
from ...models.save_list_response_201 import SaveListResponse201
from ...models.save_list_response_403 import SaveListResponse403
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import Response


def _get_kwargs(
    list_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/lists/{list_id}/save".format(
            list_id=quote(str(list_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SaveListResponse200 | SaveListResponse201 | SaveListResponse403 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = SaveListResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = SaveListResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = SaveListResponse403.from_dict(response.json())

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
) -> Response[
    SaveListResponse200 | SaveListResponse201 | SaveListResponse403 | TooManyRequestsError | UnauthorizedError
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
) -> Response[
    SaveListResponse200 | SaveListResponse201 | SaveListResponse403 | TooManyRequestsError | UnauthorizedError
]:
    """Save list.

     Saves a list to the user's saved lists for quick access. Cannot save your own lists.

    Args:
        list_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SaveListResponse200 | SaveListResponse201 | SaveListResponse403 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    list_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> SaveListResponse200 | SaveListResponse201 | SaveListResponse403 | TooManyRequestsError | UnauthorizedError | None:
    """Save list.

     Saves a list to the user's saved lists for quick access. Cannot save your own lists.

    Args:
        list_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SaveListResponse200 | SaveListResponse201 | SaveListResponse403 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        list_id=list_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    list_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    SaveListResponse200 | SaveListResponse201 | SaveListResponse403 | TooManyRequestsError | UnauthorizedError
]:
    """Save list.

     Saves a list to the user's saved lists for quick access. Cannot save your own lists.

    Args:
        list_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SaveListResponse200 | SaveListResponse201 | SaveListResponse403 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    list_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> SaveListResponse200 | SaveListResponse201 | SaveListResponse403 | TooManyRequestsError | UnauthorizedError | None:
    """Save list.

     Saves a list to the user's saved lists for quick access. Cannot save your own lists.

    Args:
        list_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SaveListResponse200 | SaveListResponse201 | SaveListResponse403 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
        )
    ).parsed
