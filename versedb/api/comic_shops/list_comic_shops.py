from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_comic_shops_response_200 import ListComicShopsResponse200
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    country: str | Unset = UNSET,
    state: str | Unset = UNSET,
    city: str | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["country"] = country

    params["state"] = state

    params["city"] = city

    params["q"] = q

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/shops",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListComicShopsResponse200 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = ListComicShopsResponse200.from_dict(response.json())

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
) -> Response[ListComicShopsResponse200 | TooManyRequestsError | UnauthorizedError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    country: str | Unset = UNSET,
    state: str | Unset = UNSET,
    city: str | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ListComicShopsResponse200 | TooManyRequestsError | UnauthorizedError]:
    """List comic shops.

     Returns paginated shops with optional location-based and text filtering.

    Args:
        country (str | Unset): Filter by country. Accepts an ISO alpha-2 code or canonical country
            name.
        state (str | Unset): Filter by state or province.
        city (str | Unset): Filter by city. Accepts the city name or its URL slug, case-
            insensitive.
        q (str | Unset): Search by shop name, city, street address, postal code or state,
            tolerating small typos. Results are ordered by relevance when set.
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListComicShopsResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        country=country,
        state=state,
        city=city,
        q=q,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    country: str | Unset = UNSET,
    state: str | Unset = UNSET,
    city: str | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ListComicShopsResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """List comic shops.

     Returns paginated shops with optional location-based and text filtering.

    Args:
        country (str | Unset): Filter by country. Accepts an ISO alpha-2 code or canonical country
            name.
        state (str | Unset): Filter by state or province.
        city (str | Unset): Filter by city. Accepts the city name or its URL slug, case-
            insensitive.
        q (str | Unset): Search by shop name, city, street address, postal code or state,
            tolerating small typos. Results are ordered by relevance when set.
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListComicShopsResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        client=client,
        country=country,
        state=state,
        city=city,
        q=q,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    country: str | Unset = UNSET,
    state: str | Unset = UNSET,
    city: str | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ListComicShopsResponse200 | TooManyRequestsError | UnauthorizedError]:
    """List comic shops.

     Returns paginated shops with optional location-based and text filtering.

    Args:
        country (str | Unset): Filter by country. Accepts an ISO alpha-2 code or canonical country
            name.
        state (str | Unset): Filter by state or province.
        city (str | Unset): Filter by city. Accepts the city name or its URL slug, case-
            insensitive.
        q (str | Unset): Search by shop name, city, street address, postal code or state,
            tolerating small typos. Results are ordered by relevance when set.
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListComicShopsResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        country=country,
        state=state,
        city=city,
        q=q,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    country: str | Unset = UNSET,
    state: str | Unset = UNSET,
    city: str | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ListComicShopsResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """List comic shops.

     Returns paginated shops with optional location-based and text filtering.

    Args:
        country (str | Unset): Filter by country. Accepts an ISO alpha-2 code or canonical country
            name.
        state (str | Unset): Filter by state or province.
        city (str | Unset): Filter by city. Accepts the city name or its URL slug, case-
            insensitive.
        q (str | Unset): Search by shop name, city, street address, postal code or state,
            tolerating small typos. Results are ordered by relevance when set.
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListComicShopsResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            client=client,
            country=country,
            state=state,
            city=city,
            q=q,
            limit=limit,
        )
    ).parsed
