from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_the_authenticated_user_response_200 import GetTheAuthenticatedUserResponse200
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/user",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetTheAuthenticatedUserResponse200 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = GetTheAuthenticatedUserResponse200.from_dict(response.json())

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
) -> Response[GetTheAuthenticatedUserResponse200 | TooManyRequestsError | UnauthorizedError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetTheAuthenticatedUserResponse200 | TooManyRequestsError | UnauthorizedError]:
    """Get the authenticated user.

     Returns the profile of the user the token belongs to.

    Needs `read:user` or `read:showcase`. A `read:showcase` token gets only `id`, `name`,
    `username`, `bio`, the avatar and banner fields, `is_pro`, the level and XP fields,
    `created_at` and `updated_at`: no email, location, birth date, preferences, or
    notification and account settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTheAuthenticatedUserResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> GetTheAuthenticatedUserResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """Get the authenticated user.

     Returns the profile of the user the token belongs to.

    Needs `read:user` or `read:showcase`. A `read:showcase` token gets only `id`, `name`,
    `username`, `bio`, the avatar and banner fields, `is_pro`, the level and XP fields,
    `created_at` and `updated_at`: no email, location, birth date, preferences, or
    notification and account settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTheAuthenticatedUserResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetTheAuthenticatedUserResponse200 | TooManyRequestsError | UnauthorizedError]:
    """Get the authenticated user.

     Returns the profile of the user the token belongs to.

    Needs `read:user` or `read:showcase`. A `read:showcase` token gets only `id`, `name`,
    `username`, `bio`, the avatar and banner fields, `is_pro`, the level and XP fields,
    `created_at` and `updated_at`: no email, location, birth date, preferences, or
    notification and account settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTheAuthenticatedUserResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> GetTheAuthenticatedUserResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """Get the authenticated user.

     Returns the profile of the user the token belongs to.

    Needs `read:user` or `read:showcase`. A `read:showcase` token gets only `id`, `name`,
    `username`, `bio`, the avatar and banner fields, `is_pro`, the level and XP fields,
    `created_at` and `updated_at`: no email, location, birth date, preferences, or
    notification and account settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTheAuthenticatedUserResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
