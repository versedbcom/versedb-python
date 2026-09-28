from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_imprints_response_200 import ListImprintsResponse200
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    publisher_id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["publisher_id"] = publisher_id

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/imprints",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListImprintsResponse200 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = ListImprintsResponse200.from_dict(response.json())

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
) -> Response[ListImprintsResponse200 | TooManyRequestsError | UnauthorizedError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    publisher_id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ListImprintsResponse200 | TooManyRequestsError | UnauthorizedError]:
    """List imprints

     Returns: id, name, slug, publisher

    Args:
        q (str | Unset): Search by imprint name.
        publisher_id (int | Unset): Filter by publisher ID.
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListImprintsResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        q=q,
        publisher_id=publisher_id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    publisher_id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ListImprintsResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """List imprints

     Returns: id, name, slug, publisher

    Args:
        q (str | Unset): Search by imprint name.
        publisher_id (int | Unset): Filter by publisher ID.
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListImprintsResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        client=client,
        q=q,
        publisher_id=publisher_id,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    publisher_id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ListImprintsResponse200 | TooManyRequestsError | UnauthorizedError]:
    """List imprints

     Returns: id, name, slug, publisher

    Args:
        q (str | Unset): Search by imprint name.
        publisher_id (int | Unset): Filter by publisher ID.
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListImprintsResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        q=q,
        publisher_id=publisher_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    publisher_id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ListImprintsResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """List imprints

     Returns: id, name, slug, publisher

    Args:
        q (str | Unset): Search by imprint name.
        publisher_id (int | Unset): Filter by publisher ID.
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListImprintsResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            publisher_id=publisher_id,
            limit=limit,
        )
    ).parsed
