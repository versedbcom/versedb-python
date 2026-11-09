from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remove_issue_from_collection_response_403 import RemoveIssueFromCollectionResponse403
from ...models.remove_issue_from_collection_response_404_type_0 import RemoveIssueFromCollectionResponse404Type0
from ...models.remove_issue_from_collection_response_404_type_1 import RemoveIssueFromCollectionResponse404Type1
from ...models.remove_issue_from_collection_response_422 import RemoveIssueFromCollectionResponse422
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    issue_id: int,
    *,
    variant_id: int | Unset = UNSET,
    collection_item_id: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["variant_id"] = variant_id

    params["collection_item_id"] = collection_item_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/issues/{issue_id}/collection".format(
            issue_id=quote(str(issue_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | RemoveIssueFromCollectionResponse403
    | RemoveIssueFromCollectionResponse404Type0
    | RemoveIssueFromCollectionResponse404Type1
    | RemoveIssueFromCollectionResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = RemoveIssueFromCollectionResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:

        def _parse_response_404(
            data: object,
        ) -> RemoveIssueFromCollectionResponse404Type0 | RemoveIssueFromCollectionResponse404Type1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_404_type_0 = RemoveIssueFromCollectionResponse404Type0.from_dict(data)

                return response_404_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_404_type_1 = RemoveIssueFromCollectionResponse404Type1.from_dict(data)

            return response_404_type_1

        response_404 = _parse_response_404(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = RemoveIssueFromCollectionResponse422.from_dict(response.json())

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
    Any
    | RemoveIssueFromCollectionResponse403
    | RemoveIssueFromCollectionResponse404Type0
    | RemoveIssueFromCollectionResponse404Type1
    | RemoveIssueFromCollectionResponse422
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
    variant_id: int | Unset = UNSET,
    collection_item_id: int | Unset = UNSET,
) -> Response[
    Any
    | RemoveIssueFromCollectionResponse403
    | RemoveIssueFromCollectionResponse404Type0
    | RemoveIssueFromCollectionResponse404Type1
    | RemoveIssueFromCollectionResponse422
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Remove issue from collection.

     Removes one of the user's copies of the issue: the copy `collection_item_id` names, else the oldest
    copy (of `variant_id`'s cover when one is sent). Each may come in the query or the body.

    Args:
        issue_id (int): The issue ID.
        variant_id (int | Unset): Specific variant ID to remove (optional).
        collection_item_id (int | Unset): Specific collection item ID to remove (optional).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RemoveIssueFromCollectionResponse403 | RemoveIssueFromCollectionResponse404Type0 | RemoveIssueFromCollectionResponse404Type1 | RemoveIssueFromCollectionResponse422 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        issue_id=issue_id,
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
    variant_id: int | Unset = UNSET,
    collection_item_id: int | Unset = UNSET,
) -> (
    Any
    | RemoveIssueFromCollectionResponse403
    | RemoveIssueFromCollectionResponse404Type0
    | RemoveIssueFromCollectionResponse404Type1
    | RemoveIssueFromCollectionResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Remove issue from collection.

     Removes one of the user's copies of the issue: the copy `collection_item_id` names, else the oldest
    copy (of `variant_id`'s cover when one is sent). Each may come in the query or the body.

    Args:
        issue_id (int): The issue ID.
        variant_id (int | Unset): Specific variant ID to remove (optional).
        collection_item_id (int | Unset): Specific collection item ID to remove (optional).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RemoveIssueFromCollectionResponse403 | RemoveIssueFromCollectionResponse404Type0 | RemoveIssueFromCollectionResponse404Type1 | RemoveIssueFromCollectionResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        issue_id=issue_id,
        client=client,
        variant_id=variant_id,
        collection_item_id=collection_item_id,
    ).parsed


async def asyncio_detailed(
    issue_id: int,
    *,
    client: AuthenticatedClient | Client,
    variant_id: int | Unset = UNSET,
    collection_item_id: int | Unset = UNSET,
) -> Response[
    Any
    | RemoveIssueFromCollectionResponse403
    | RemoveIssueFromCollectionResponse404Type0
    | RemoveIssueFromCollectionResponse404Type1
    | RemoveIssueFromCollectionResponse422
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Remove issue from collection.

     Removes one of the user's copies of the issue: the copy `collection_item_id` names, else the oldest
    copy (of `variant_id`'s cover when one is sent). Each may come in the query or the body.

    Args:
        issue_id (int): The issue ID.
        variant_id (int | Unset): Specific variant ID to remove (optional).
        collection_item_id (int | Unset): Specific collection item ID to remove (optional).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RemoveIssueFromCollectionResponse403 | RemoveIssueFromCollectionResponse404Type0 | RemoveIssueFromCollectionResponse404Type1 | RemoveIssueFromCollectionResponse422 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        issue_id=issue_id,
        variant_id=variant_id,
        collection_item_id=collection_item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    issue_id: int,
    *,
    client: AuthenticatedClient | Client,
    variant_id: int | Unset = UNSET,
    collection_item_id: int | Unset = UNSET,
) -> (
    Any
    | RemoveIssueFromCollectionResponse403
    | RemoveIssueFromCollectionResponse404Type0
    | RemoveIssueFromCollectionResponse404Type1
    | RemoveIssueFromCollectionResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Remove issue from collection.

     Removes one of the user's copies of the issue: the copy `collection_item_id` names, else the oldest
    copy (of `variant_id`'s cover when one is sent). Each may come in the query or the body.

    Args:
        issue_id (int): The issue ID.
        variant_id (int | Unset): Specific variant ID to remove (optional).
        collection_item_id (int | Unset): Specific collection item ID to remove (optional).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RemoveIssueFromCollectionResponse403 | RemoveIssueFromCollectionResponse404Type0 | RemoveIssueFromCollectionResponse404Type1 | RemoveIssueFromCollectionResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            issue_id=issue_id,
            client=client,
            variant_id=variant_id,
            collection_item_id=collection_item_id,
        )
    ).parsed
