from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.stop_a_list_updating_itself_response_200 import StopAListUpdatingItselfResponse200
from ...models.stop_a_list_updating_itself_response_422 import StopAListUpdatingItselfResponse422
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import Response


def _get_kwargs(
    list_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/lists/{list_id}/stop-rule".format(
            list_id=quote(str(list_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    StopAListUpdatingItselfResponse200
    | StopAListUpdatingItselfResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    if response.status_code == 200:
        response_200 = StopAListUpdatingItselfResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 422:
        response_422 = StopAListUpdatingItselfResponse422.from_dict(response.json())

        return response_422

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
    StopAListUpdatingItselfResponse200 | StopAListUpdatingItselfResponse422 | TooManyRequestsError | UnauthorizedError
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
    StopAListUpdatingItselfResponse200 | StopAListUpdatingItselfResponse422 | TooManyRequestsError | UnauthorizedError
]:
    """Stop a list updating itself.

     One-way: drops a smart list's rule and keeps every item the last refresh left,
    handing the contents back for editing by hand. A rule is only ever attached when
    a list is created, so it cannot be put back.

    Args:
        list_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StopAListUpdatingItselfResponse200 | StopAListUpdatingItselfResponse422 | TooManyRequestsError | UnauthorizedError]
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
) -> (
    StopAListUpdatingItselfResponse200
    | StopAListUpdatingItselfResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Stop a list updating itself.

     One-way: drops a smart list's rule and keeps every item the last refresh left,
    handing the contents back for editing by hand. A rule is only ever attached when
    a list is created, so it cannot be put back.

    Args:
        list_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StopAListUpdatingItselfResponse200 | StopAListUpdatingItselfResponse422 | TooManyRequestsError | UnauthorizedError
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
    StopAListUpdatingItselfResponse200 | StopAListUpdatingItselfResponse422 | TooManyRequestsError | UnauthorizedError
]:
    """Stop a list updating itself.

     One-way: drops a smart list's rule and keeps every item the last refresh left,
    handing the contents back for editing by hand. A rule is only ever attached when
    a list is created, so it cannot be put back.

    Args:
        list_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StopAListUpdatingItselfResponse200 | StopAListUpdatingItselfResponse422 | TooManyRequestsError | UnauthorizedError]
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
) -> (
    StopAListUpdatingItselfResponse200
    | StopAListUpdatingItselfResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Stop a list updating itself.

     One-way: drops a smart list's rule and keeps every item the last refresh left,
    handing the contents back for editing by hand. A rule is only ever attached when
    a list is created, so it cannot be put back.

    Args:
        list_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StopAListUpdatingItselfResponse200 | StopAListUpdatingItselfResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
        )
    ).parsed
