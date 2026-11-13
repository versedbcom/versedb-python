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
from ...models.update_collection_item_response_403 import UpdateCollectionItemResponse403
from ...models.update_collection_item_response_404_type_0 import UpdateCollectionItemResponse404Type0
from ...models.update_collection_item_response_404_type_1 import UpdateCollectionItemResponse404Type1
from ...models.update_collection_item_response_422_type_0 import UpdateCollectionItemResponse422Type0
from ...models.update_collection_item_response_422_type_1 import UpdateCollectionItemResponse422Type1
from ...models.update_collection_item_response_422_type_2 import UpdateCollectionItemResponse422Type2
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
    TooManyRequestsError
    | UnauthorizedError
    | UpdateCollectionItemResponse200
    | UpdateCollectionItemResponse403
    | UpdateCollectionItemResponse404Type0
    | UpdateCollectionItemResponse404Type1
    | UpdateCollectionItemResponse422Type0
    | UpdateCollectionItemResponse422Type1
    | UpdateCollectionItemResponse422Type2
    | None
):
    if response.status_code == 200:
        response_200 = UpdateCollectionItemResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UpdateCollectionItemResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:

        def _parse_response_404(
            data: object,
        ) -> UpdateCollectionItemResponse404Type0 | UpdateCollectionItemResponse404Type1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_404_type_0 = UpdateCollectionItemResponse404Type0.from_dict(data)

                return response_404_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_404_type_1 = UpdateCollectionItemResponse404Type1.from_dict(data)

            return response_404_type_1

        response_404 = _parse_response_404(response.json())

        return response_404

    if response.status_code == 422:

        def _parse_response_422(
            data: object,
        ) -> (
            UpdateCollectionItemResponse422Type0
            | UpdateCollectionItemResponse422Type1
            | UpdateCollectionItemResponse422Type2
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = UpdateCollectionItemResponse422Type0.from_dict(data)

                return response_422_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_1 = UpdateCollectionItemResponse422Type1.from_dict(data)

                return response_422_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_2 = UpdateCollectionItemResponse422Type2.from_dict(data)

            return response_422_type_2

        response_422 = _parse_response_422(response.json())

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
    TooManyRequestsError
    | UnauthorizedError
    | UpdateCollectionItemResponse200
    | UpdateCollectionItemResponse403
    | UpdateCollectionItemResponse404Type0
    | UpdateCollectionItemResponse404Type1
    | UpdateCollectionItemResponse422Type0
    | UpdateCollectionItemResponse422Type1
    | UpdateCollectionItemResponse422Type2
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
    TooManyRequestsError
    | UnauthorizedError
    | UpdateCollectionItemResponse200
    | UpdateCollectionItemResponse403
    | UpdateCollectionItemResponse404Type0
    | UpdateCollectionItemResponse404Type1
    | UpdateCollectionItemResponse422Type0
    | UpdateCollectionItemResponse422Type1
    | UpdateCollectionItemResponse422Type2
]:
    """Update collection item.

     Updates one of the user's copies of the issue: the copy `collection_item_id` names (query or body),
    else the oldest copy (of the query's `variant_id` cover when one is sent). Only the fields sent
    change; `tags` replaces the copy's tags. `is_read`, `read_at` and `read_undated` set the issue's
    read status too: `is_read` with no `read_at` marks it read with no date (an existing read keeps its
    date).

    Args:
        issue_id (int): The issue ID.
        variant_id (int | Unset): Specific variant ID to update (when user has multiple entries).
        collection_item_id (int | Unset): Specific collection item ID to update.
        body (UpdateCollectionItemBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TooManyRequestsError | UnauthorizedError | UpdateCollectionItemResponse200 | UpdateCollectionItemResponse403 | UpdateCollectionItemResponse404Type0 | UpdateCollectionItemResponse404Type1 | UpdateCollectionItemResponse422Type0 | UpdateCollectionItemResponse422Type1 | UpdateCollectionItemResponse422Type2]
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
    TooManyRequestsError
    | UnauthorizedError
    | UpdateCollectionItemResponse200
    | UpdateCollectionItemResponse403
    | UpdateCollectionItemResponse404Type0
    | UpdateCollectionItemResponse404Type1
    | UpdateCollectionItemResponse422Type0
    | UpdateCollectionItemResponse422Type1
    | UpdateCollectionItemResponse422Type2
    | None
):
    """Update collection item.

     Updates one of the user's copies of the issue: the copy `collection_item_id` names (query or body),
    else the oldest copy (of the query's `variant_id` cover when one is sent). Only the fields sent
    change; `tags` replaces the copy's tags. `is_read`, `read_at` and `read_undated` set the issue's
    read status too: `is_read` with no `read_at` marks it read with no date (an existing read keeps its
    date).

    Args:
        issue_id (int): The issue ID.
        variant_id (int | Unset): Specific variant ID to update (when user has multiple entries).
        collection_item_id (int | Unset): Specific collection item ID to update.
        body (UpdateCollectionItemBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TooManyRequestsError | UnauthorizedError | UpdateCollectionItemResponse200 | UpdateCollectionItemResponse403 | UpdateCollectionItemResponse404Type0 | UpdateCollectionItemResponse404Type1 | UpdateCollectionItemResponse422Type0 | UpdateCollectionItemResponse422Type1 | UpdateCollectionItemResponse422Type2
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
    TooManyRequestsError
    | UnauthorizedError
    | UpdateCollectionItemResponse200
    | UpdateCollectionItemResponse403
    | UpdateCollectionItemResponse404Type0
    | UpdateCollectionItemResponse404Type1
    | UpdateCollectionItemResponse422Type0
    | UpdateCollectionItemResponse422Type1
    | UpdateCollectionItemResponse422Type2
]:
    """Update collection item.

     Updates one of the user's copies of the issue: the copy `collection_item_id` names (query or body),
    else the oldest copy (of the query's `variant_id` cover when one is sent). Only the fields sent
    change; `tags` replaces the copy's tags. `is_read`, `read_at` and `read_undated` set the issue's
    read status too: `is_read` with no `read_at` marks it read with no date (an existing read keeps its
    date).

    Args:
        issue_id (int): The issue ID.
        variant_id (int | Unset): Specific variant ID to update (when user has multiple entries).
        collection_item_id (int | Unset): Specific collection item ID to update.
        body (UpdateCollectionItemBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TooManyRequestsError | UnauthorizedError | UpdateCollectionItemResponse200 | UpdateCollectionItemResponse403 | UpdateCollectionItemResponse404Type0 | UpdateCollectionItemResponse404Type1 | UpdateCollectionItemResponse422Type0 | UpdateCollectionItemResponse422Type1 | UpdateCollectionItemResponse422Type2]
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
    TooManyRequestsError
    | UnauthorizedError
    | UpdateCollectionItemResponse200
    | UpdateCollectionItemResponse403
    | UpdateCollectionItemResponse404Type0
    | UpdateCollectionItemResponse404Type1
    | UpdateCollectionItemResponse422Type0
    | UpdateCollectionItemResponse422Type1
    | UpdateCollectionItemResponse422Type2
    | None
):
    """Update collection item.

     Updates one of the user's copies of the issue: the copy `collection_item_id` names (query or body),
    else the oldest copy (of the query's `variant_id` cover when one is sent). Only the fields sent
    change; `tags` replaces the copy's tags. `is_read`, `read_at` and `read_undated` set the issue's
    read status too: `is_read` with no `read_at` marks it read with no date (an existing read keeps its
    date).

    Args:
        issue_id (int): The issue ID.
        variant_id (int | Unset): Specific variant ID to update (when user has multiple entries).
        collection_item_id (int | Unset): Specific collection item ID to update.
        body (UpdateCollectionItemBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TooManyRequestsError | UnauthorizedError | UpdateCollectionItemResponse200 | UpdateCollectionItemResponse403 | UpdateCollectionItemResponse404Type0 | UpdateCollectionItemResponse404Type1 | UpdateCollectionItemResponse422Type0 | UpdateCollectionItemResponse422Type1 | UpdateCollectionItemResponse422Type2
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
