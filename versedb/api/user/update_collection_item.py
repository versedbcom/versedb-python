from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...models.update_collection_item_body import UpdateCollectionItemBody
from ...models.update_collection_item_response_200 import UpdateCollectionItemResponse200
from ...models.update_collection_item_response_404 import UpdateCollectionItemResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    issue_id: int,
    *,
    body: UpdateCollectionItemBody | Unset = UNSET,
    variant_id: int | Unset = UNSET,
    collection_item_id: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["variant_id"] = variant_id

    params["collection_item_id"] = collection_item_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/issues/{issue_id}/collection".format(
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
) -> (
    TooManyRequestsError | UnauthorizedError | UpdateCollectionItemResponse200 | UpdateCollectionItemResponse404 | None
):
    if response.status_code == 200:
        response_200 = UpdateCollectionItemResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = UpdateCollectionItemResponse404.from_dict(response.json())

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
) -> Response[
    TooManyRequestsError | UnauthorizedError | UpdateCollectionItemResponse200 | UpdateCollectionItemResponse404
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
    body: UpdateCollectionItemBody | Unset = UNSET,
    variant_id: int | Unset = UNSET,
    collection_item_id: int | Unset = UNSET,
) -> Response[
    TooManyRequestsError | UnauthorizedError | UpdateCollectionItemResponse200 | UpdateCollectionItemResponse404
]:
    """Update collection item.

     Updates metadata on an existing collection entry for an issue.
    Supports partial updates: only send the fields you want to change.

    Args:
        issue_id (int):
        variant_id (int | Unset): Specific variant ID to update (when user has multiple entries).
        collection_item_id (int | Unset): Specific collection item ID to update.
        body (UpdateCollectionItemBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TooManyRequestsError | UnauthorizedError | UpdateCollectionItemResponse200 | UpdateCollectionItemResponse404]
    """

    kwargs = _get_kwargs(
        issue_id=issue_id,
        body=body,
        variant_id=variant_id,
        collection_item_id=collection_item_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    issue_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateCollectionItemBody | Unset = UNSET,
    variant_id: int | Unset = UNSET,
    collection_item_id: int | Unset = UNSET,
) -> (
    TooManyRequestsError | UnauthorizedError | UpdateCollectionItemResponse200 | UpdateCollectionItemResponse404 | None
):
    """Update collection item.

     Updates metadata on an existing collection entry for an issue.
    Supports partial updates: only send the fields you want to change.

    Args:
        issue_id (int):
        variant_id (int | Unset): Specific variant ID to update (when user has multiple entries).
        collection_item_id (int | Unset): Specific collection item ID to update.
        body (UpdateCollectionItemBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TooManyRequestsError | UnauthorizedError | UpdateCollectionItemResponse200 | UpdateCollectionItemResponse404
    """

    return sync_detailed(
        issue_id=issue_id,
        client=client,
        body=body,
        variant_id=variant_id,
        collection_item_id=collection_item_id,
    ).parsed


async def asyncio_detailed(
    issue_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateCollectionItemBody | Unset = UNSET,
    variant_id: int | Unset = UNSET,
    collection_item_id: int | Unset = UNSET,
) -> Response[
    TooManyRequestsError | UnauthorizedError | UpdateCollectionItemResponse200 | UpdateCollectionItemResponse404
]:
    """Update collection item.

     Updates metadata on an existing collection entry for an issue.
    Supports partial updates: only send the fields you want to change.

    Args:
        issue_id (int):
        variant_id (int | Unset): Specific variant ID to update (when user has multiple entries).
        collection_item_id (int | Unset): Specific collection item ID to update.
        body (UpdateCollectionItemBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TooManyRequestsError | UnauthorizedError | UpdateCollectionItemResponse200 | UpdateCollectionItemResponse404]
    """

    kwargs = _get_kwargs(
        issue_id=issue_id,
        body=body,
        variant_id=variant_id,
        collection_item_id=collection_item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    issue_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateCollectionItemBody | Unset = UNSET,
    variant_id: int | Unset = UNSET,
    collection_item_id: int | Unset = UNSET,
) -> (
    TooManyRequestsError | UnauthorizedError | UpdateCollectionItemResponse200 | UpdateCollectionItemResponse404 | None
):
    """Update collection item.

     Updates metadata on an existing collection entry for an issue.
    Supports partial updates: only send the fields you want to change.

    Args:
        issue_id (int):
        variant_id (int | Unset): Specific variant ID to update (when user has multiple entries).
        collection_item_id (int | Unset): Specific collection item ID to update.
        body (UpdateCollectionItemBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TooManyRequestsError | UnauthorizedError | UpdateCollectionItemResponse200 | UpdateCollectionItemResponse404
    """

    return (
        await asyncio_detailed(
            issue_id=issue_id,
            client=client,
            body=body,
            variant_id=variant_id,
            collection_item_id=collection_item_id,
        )
    ).parsed
