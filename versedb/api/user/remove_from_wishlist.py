from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remove_from_wishlist_body import RemoveFromWishlistBody
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    issue_id: int,
    *,
    body: RemoveFromWishlistBody | Unset = UNSET,
    variant_id: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["variant_id"] = variant_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/issues/{issue_id}/wishlist".format(
            issue_id=quote(str(issue_id), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | TooManyRequestsError | UnauthorizedError]:
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
    body: RemoveFromWishlistBody | Unset = UNSET,
    variant_id: int | Unset = UNSET,
) -> Response[Any | TooManyRequestsError | UnauthorizedError]:
    """Remove from wishlist.

     Removes the issue from the authenticated user's wishlist. Idempotent:
    returns 204 whether or not the issue was on the wishlist.

    Args:
        issue_id (int):
        variant_id (int | Unset): Optional cover variant to remove. Omit to remove the "any cover"
            entry — variant-pinned entries for the same issue are left alone.
        body (RemoveFromWishlistBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        issue_id=issue_id,
        body=body,
        variant_id=variant_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    issue_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: RemoveFromWishlistBody | Unset = UNSET,
    variant_id: int | Unset = UNSET,
) -> Any | TooManyRequestsError | UnauthorizedError | None:
    """Remove from wishlist.

     Removes the issue from the authenticated user's wishlist. Idempotent:
    returns 204 whether or not the issue was on the wishlist.

    Args:
        issue_id (int):
        variant_id (int | Unset): Optional cover variant to remove. Omit to remove the "any cover"
            entry — variant-pinned entries for the same issue are left alone.
        body (RemoveFromWishlistBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        issue_id=issue_id,
        client=client,
        body=body,
        variant_id=variant_id,
    ).parsed


async def asyncio_detailed(
    issue_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: RemoveFromWishlistBody | Unset = UNSET,
    variant_id: int | Unset = UNSET,
) -> Response[Any | TooManyRequestsError | UnauthorizedError]:
    """Remove from wishlist.

     Removes the issue from the authenticated user's wishlist. Idempotent:
    returns 204 whether or not the issue was on the wishlist.

    Args:
        issue_id (int):
        variant_id (int | Unset): Optional cover variant to remove. Omit to remove the "any cover"
            entry — variant-pinned entries for the same issue are left alone.
        body (RemoveFromWishlistBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        issue_id=issue_id,
        body=body,
        variant_id=variant_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    issue_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: RemoveFromWishlistBody | Unset = UNSET,
    variant_id: int | Unset = UNSET,
) -> Any | TooManyRequestsError | UnauthorizedError | None:
    """Remove from wishlist.

     Removes the issue from the authenticated user's wishlist. Idempotent:
    returns 204 whether or not the issue was on the wishlist.

    Args:
        issue_id (int):
        variant_id (int | Unset): Optional cover variant to remove. Omit to remove the "any cover"
            entry — variant-pinned entries for the same issue are left alone.
        body (RemoveFromWishlistBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            issue_id=issue_id,
            client=client,
            body=body,
            variant_id=variant_id,
        )
    ).parsed
