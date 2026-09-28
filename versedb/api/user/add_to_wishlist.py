from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_to_wishlist_body import AddToWishlistBody
from ...models.add_to_wishlist_response_200 import AddToWishlistResponse200
from ...models.add_to_wishlist_response_201 import AddToWishlistResponse201
from ...models.add_to_wishlist_response_422 import AddToWishlistResponse422
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    issue_id: int,
    *,
    body: AddToWishlistBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/issues/{issue_id}/wishlist".format(
            issue_id=quote(str(issue_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AddToWishlistResponse200
    | AddToWishlistResponse201
    | AddToWishlistResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    if response.status_code == 200:
        response_200 = AddToWishlistResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = AddToWishlistResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 422:
        response_422 = AddToWishlistResponse422.from_dict(response.json())

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
    AddToWishlistResponse200
    | AddToWishlistResponse201
    | AddToWishlistResponse422
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
    issue_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: AddToWishlistBody | Unset = UNSET,
) -> Response[
    AddToWishlistResponse200
    | AddToWishlistResponse201
    | AddToWishlistResponse422
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Add to wishlist.

     Adds the issue to the authenticated user's wishlist. Idempotent: calling
    with an issue already on the wishlist returns 200 without creating a duplicate.

    Args:
        issue_id (int):
        body (AddToWishlistBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddToWishlistResponse200 | AddToWishlistResponse201 | AddToWishlistResponse422 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        issue_id=issue_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    issue_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: AddToWishlistBody | Unset = UNSET,
) -> (
    AddToWishlistResponse200
    | AddToWishlistResponse201
    | AddToWishlistResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Add to wishlist.

     Adds the issue to the authenticated user's wishlist. Idempotent: calling
    with an issue already on the wishlist returns 200 without creating a duplicate.

    Args:
        issue_id (int):
        body (AddToWishlistBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddToWishlistResponse200 | AddToWishlistResponse201 | AddToWishlistResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        issue_id=issue_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    issue_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: AddToWishlistBody | Unset = UNSET,
) -> Response[
    AddToWishlistResponse200
    | AddToWishlistResponse201
    | AddToWishlistResponse422
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Add to wishlist.

     Adds the issue to the authenticated user's wishlist. Idempotent: calling
    with an issue already on the wishlist returns 200 without creating a duplicate.

    Args:
        issue_id (int):
        body (AddToWishlistBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddToWishlistResponse200 | AddToWishlistResponse201 | AddToWishlistResponse422 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        issue_id=issue_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    issue_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: AddToWishlistBody | Unset = UNSET,
) -> (
    AddToWishlistResponse200
    | AddToWishlistResponse201
    | AddToWishlistResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Add to wishlist.

     Adds the issue to the authenticated user's wishlist. Idempotent: calling
    with an issue already on the wishlist returns 200 without creating a duplicate.

    Args:
        issue_id (int):
        body (AddToWishlistBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddToWishlistResponse200 | AddToWishlistResponse201 | AddToWishlistResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            issue_id=issue_id,
            client=client,
            body=body,
        )
    ).parsed
