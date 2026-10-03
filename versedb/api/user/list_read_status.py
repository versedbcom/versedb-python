from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_read_status_response_200 import ListReadStatusResponse200
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per_page: int | Unset = UNSET,
    unreviewed: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["unreviewed"] = unreviewed

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/user/read-status",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListReadStatusResponse200 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = ListReadStatusResponse200.from_dict(response.json())

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
) -> Response[ListReadStatusResponse200 | TooManyRequestsError | UnauthorizedError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    unreviewed: bool | Unset = UNSET,
) -> Response[ListReadStatusResponse200 | TooManyRequestsError | UnauthorizedError]:
    """List read status.

     Returns all issues the user has marked as read with timestamps.

    Needs `read:user` or `read:showcase`; both get the same response.

    Args:
        per_page (int | Unset): Items per page (max 100).
        unreviewed (bool | Unset): When true, only returns reads for issues the user has not yet
            reviewed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListReadStatusResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        unreviewed=unreviewed,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    unreviewed: bool | Unset = UNSET,
) -> ListReadStatusResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """List read status.

     Returns all issues the user has marked as read with timestamps.

    Needs `read:user` or `read:showcase`; both get the same response.

    Args:
        per_page (int | Unset): Items per page (max 100).
        unreviewed (bool | Unset): When true, only returns reads for issues the user has not yet
            reviewed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListReadStatusResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        client=client,
        per_page=per_page,
        unreviewed=unreviewed,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    unreviewed: bool | Unset = UNSET,
) -> Response[ListReadStatusResponse200 | TooManyRequestsError | UnauthorizedError]:
    """List read status.

     Returns all issues the user has marked as read with timestamps.

    Needs `read:user` or `read:showcase`; both get the same response.

    Args:
        per_page (int | Unset): Items per page (max 100).
        unreviewed (bool | Unset): When true, only returns reads for issues the user has not yet
            reviewed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListReadStatusResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        unreviewed=unreviewed,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    unreviewed: bool | Unset = UNSET,
) -> ListReadStatusResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """List read status.

     Returns all issues the user has marked as read with timestamps.

    Needs `read:user` or `read:showcase`; both get the same response.

    Args:
        per_page (int | Unset): Items per page (max 100).
        unreviewed (bool | Unset): When true, only returns reads for issues the user has not yet
            reviewed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListReadStatusResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            client=client,
            per_page=per_page,
            unreviewed=unreviewed,
        )
    ).parsed
