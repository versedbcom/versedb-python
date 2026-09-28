from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_a_comic_shop_response_200 import GetAComicShopResponse200
from ...models.get_a_comic_shop_response_404 import GetAComicShopResponse404
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import Response


def _get_kwargs(
    shop_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/shops/{shop_id}".format(
            shop_id=quote(str(shop_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetAComicShopResponse200 | GetAComicShopResponse404 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = GetAComicShopResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetAComicShopResponse404.from_dict(response.json())

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
) -> Response[GetAComicShopResponse200 | GetAComicShopResponse404 | TooManyRequestsError | UnauthorizedError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    shop_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetAComicShopResponse200 | GetAComicShopResponse404 | TooManyRequestsError | UnauthorizedError]:
    """Get a comic shop.

     Returns full shop details including services offered.

    `operating_hours` is keyed Monday-first by lowercase day name. Each value is
    either `closed` or one or more 24-hour `HH:MM-HH:MM` ranges joined by commas
    (a split shift reads `09:00-13:00,15:00-19:00`). A day missing from the map
    has unknown hours — that is not the same as the shop being closed that day.

    Args:
        shop_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAComicShopResponse200 | GetAComicShopResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        shop_id=shop_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    shop_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetAComicShopResponse200 | GetAComicShopResponse404 | TooManyRequestsError | UnauthorizedError | None:
    """Get a comic shop.

     Returns full shop details including services offered.

    `operating_hours` is keyed Monday-first by lowercase day name. Each value is
    either `closed` or one or more 24-hour `HH:MM-HH:MM` ranges joined by commas
    (a split shift reads `09:00-13:00,15:00-19:00`). A day missing from the map
    has unknown hours — that is not the same as the shop being closed that day.

    Args:
        shop_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAComicShopResponse200 | GetAComicShopResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        shop_id=shop_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    shop_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetAComicShopResponse200 | GetAComicShopResponse404 | TooManyRequestsError | UnauthorizedError]:
    """Get a comic shop.

     Returns full shop details including services offered.

    `operating_hours` is keyed Monday-first by lowercase day name. Each value is
    either `closed` or one or more 24-hour `HH:MM-HH:MM` ranges joined by commas
    (a split shift reads `09:00-13:00,15:00-19:00`). A day missing from the map
    has unknown hours — that is not the same as the shop being closed that day.

    Args:
        shop_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAComicShopResponse200 | GetAComicShopResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        shop_id=shop_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    shop_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetAComicShopResponse200 | GetAComicShopResponse404 | TooManyRequestsError | UnauthorizedError | None:
    """Get a comic shop.

     Returns full shop details including services offered.

    `operating_hours` is keyed Monday-first by lowercase day name. Each value is
    either `closed` or one or more 24-hour `HH:MM-HH:MM` ranges joined by commas
    (a split shift reads `09:00-13:00,15:00-19:00`). A day missing from the map
    has unknown hours — that is not the same as the shop being closed that day.

    Args:
        shop_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAComicShopResponse200 | GetAComicShopResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            shop_id=shop_id,
            client=client,
        )
    ).parsed
