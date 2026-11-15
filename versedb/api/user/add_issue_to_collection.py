from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_issue_to_collection_body import AddIssueToCollectionBody
from ...models.add_issue_to_collection_response_201 import AddIssueToCollectionResponse201
from ...models.add_issue_to_collection_response_400 import AddIssueToCollectionResponse400
from ...models.add_issue_to_collection_response_403 import AddIssueToCollectionResponse403
from ...models.add_issue_to_collection_response_404 import AddIssueToCollectionResponse404
from ...models.add_issue_to_collection_response_409 import AddIssueToCollectionResponse409
from ...models.add_issue_to_collection_response_422_type_0 import AddIssueToCollectionResponse422Type0
from ...models.add_issue_to_collection_response_422_type_1 import AddIssueToCollectionResponse422Type1
from ...models.add_issue_to_collection_response_422_type_2 import AddIssueToCollectionResponse422Type2
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    issue_id: int,
    *,
    body: AddIssueToCollectionBody | Unset = UNSET,
    idempotency_key: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = str(idempotency_key)

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/issues/{issue_id}/collection".format(
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
    AddIssueToCollectionResponse201
    | AddIssueToCollectionResponse400
    | AddIssueToCollectionResponse403
    | AddIssueToCollectionResponse404
    | AddIssueToCollectionResponse409
    | AddIssueToCollectionResponse422Type0
    | AddIssueToCollectionResponse422Type1
    | AddIssueToCollectionResponse422Type2
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    if response.status_code == 201:
        response_201 = AddIssueToCollectionResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = AddIssueToCollectionResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AddIssueToCollectionResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = AddIssueToCollectionResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = AddIssueToCollectionResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:

        def _parse_response_422(
            data: object,
        ) -> (
            AddIssueToCollectionResponse422Type0
            | AddIssueToCollectionResponse422Type1
            | AddIssueToCollectionResponse422Type2
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = AddIssueToCollectionResponse422Type0.from_dict(data)

                return response_422_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_1 = AddIssueToCollectionResponse422Type1.from_dict(data)

                return response_422_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_2 = AddIssueToCollectionResponse422Type2.from_dict(data)

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
    AddIssueToCollectionResponse201
    | AddIssueToCollectionResponse400
    | AddIssueToCollectionResponse403
    | AddIssueToCollectionResponse404
    | AddIssueToCollectionResponse409
    | AddIssueToCollectionResponse422Type0
    | AddIssueToCollectionResponse422Type1
    | AddIssueToCollectionResponse422Type2
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
    body: AddIssueToCollectionBody | Unset = UNSET,
    idempotency_key: UUID | Unset = UNSET,
) -> Response[
    AddIssueToCollectionResponse201
    | AddIssueToCollectionResponse400
    | AddIssueToCollectionResponse403
    | AddIssueToCollectionResponse404
    | AddIssueToCollectionResponse409
    | AddIssueToCollectionResponse422Type0
    | AddIssueToCollectionResponse422Type1
    | AddIssueToCollectionResponse422Type2
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Add issue to collection.

     Adds a copy of the issue to the user's collection; every field is optional. When the issue was on
    the user's wishlist it comes off when the user chose that, else `was_on_wishlist` is true so the app
    can offer it. `follow_up` says whether to offer marking it read or reviewing it. Send an
    `Idempotency-Key` to make a retry safe: for 14 days a repeat with the same key, user and issue
    answers the copy the first request added, as it is now, and adds nothing.

    Args:
        issue_id (int): The issue ID.
        idempotency_key (UUID | Unset): A UUID you choose for this add. Repeating the request with
            the same key returns the copy the first request added instead of adding another.
        body (AddIssueToCollectionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddIssueToCollectionResponse201 | AddIssueToCollectionResponse400 | AddIssueToCollectionResponse403 | AddIssueToCollectionResponse404 | AddIssueToCollectionResponse409 | AddIssueToCollectionResponse422Type0 | AddIssueToCollectionResponse422Type1 | AddIssueToCollectionResponse422Type2 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        issue_id=issue_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    issue_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: AddIssueToCollectionBody | Unset = UNSET,
    idempotency_key: UUID | Unset = UNSET,
) -> (
    AddIssueToCollectionResponse201
    | AddIssueToCollectionResponse400
    | AddIssueToCollectionResponse403
    | AddIssueToCollectionResponse404
    | AddIssueToCollectionResponse409
    | AddIssueToCollectionResponse422Type0
    | AddIssueToCollectionResponse422Type1
    | AddIssueToCollectionResponse422Type2
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Add issue to collection.

     Adds a copy of the issue to the user's collection; every field is optional. When the issue was on
    the user's wishlist it comes off when the user chose that, else `was_on_wishlist` is true so the app
    can offer it. `follow_up` says whether to offer marking it read or reviewing it. Send an
    `Idempotency-Key` to make a retry safe: for 14 days a repeat with the same key, user and issue
    answers the copy the first request added, as it is now, and adds nothing.

    Args:
        issue_id (int): The issue ID.
        idempotency_key (UUID | Unset): A UUID you choose for this add. Repeating the request with
            the same key returns the copy the first request added instead of adding another.
        body (AddIssueToCollectionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddIssueToCollectionResponse201 | AddIssueToCollectionResponse400 | AddIssueToCollectionResponse403 | AddIssueToCollectionResponse404 | AddIssueToCollectionResponse409 | AddIssueToCollectionResponse422Type0 | AddIssueToCollectionResponse422Type1 | AddIssueToCollectionResponse422Type2 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        issue_id=issue_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    issue_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: AddIssueToCollectionBody | Unset = UNSET,
    idempotency_key: UUID | Unset = UNSET,
) -> Response[
    AddIssueToCollectionResponse201
    | AddIssueToCollectionResponse400
    | AddIssueToCollectionResponse403
    | AddIssueToCollectionResponse404
    | AddIssueToCollectionResponse409
    | AddIssueToCollectionResponse422Type0
    | AddIssueToCollectionResponse422Type1
    | AddIssueToCollectionResponse422Type2
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Add issue to collection.

     Adds a copy of the issue to the user's collection; every field is optional. When the issue was on
    the user's wishlist it comes off when the user chose that, else `was_on_wishlist` is true so the app
    can offer it. `follow_up` says whether to offer marking it read or reviewing it. Send an
    `Idempotency-Key` to make a retry safe: for 14 days a repeat with the same key, user and issue
    answers the copy the first request added, as it is now, and adds nothing.

    Args:
        issue_id (int): The issue ID.
        idempotency_key (UUID | Unset): A UUID you choose for this add. Repeating the request with
            the same key returns the copy the first request added instead of adding another.
        body (AddIssueToCollectionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddIssueToCollectionResponse201 | AddIssueToCollectionResponse400 | AddIssueToCollectionResponse403 | AddIssueToCollectionResponse404 | AddIssueToCollectionResponse409 | AddIssueToCollectionResponse422Type0 | AddIssueToCollectionResponse422Type1 | AddIssueToCollectionResponse422Type2 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        issue_id=issue_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    issue_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: AddIssueToCollectionBody | Unset = UNSET,
    idempotency_key: UUID | Unset = UNSET,
) -> (
    AddIssueToCollectionResponse201
    | AddIssueToCollectionResponse400
    | AddIssueToCollectionResponse403
    | AddIssueToCollectionResponse404
    | AddIssueToCollectionResponse409
    | AddIssueToCollectionResponse422Type0
    | AddIssueToCollectionResponse422Type1
    | AddIssueToCollectionResponse422Type2
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Add issue to collection.

     Adds a copy of the issue to the user's collection; every field is optional. When the issue was on
    the user's wishlist it comes off when the user chose that, else `was_on_wishlist` is true so the app
    can offer it. `follow_up` says whether to offer marking it read or reviewing it. Send an
    `Idempotency-Key` to make a retry safe: for 14 days a repeat with the same key, user and issue
    answers the copy the first request added, as it is now, and adds nothing.

    Args:
        issue_id (int): The issue ID.
        idempotency_key (UUID | Unset): A UUID you choose for this add. Repeating the request with
            the same key returns the copy the first request added instead of adding another.
        body (AddIssueToCollectionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddIssueToCollectionResponse201 | AddIssueToCollectionResponse400 | AddIssueToCollectionResponse403 | AddIssueToCollectionResponse404 | AddIssueToCollectionResponse409 | AddIssueToCollectionResponse422Type0 | AddIssueToCollectionResponse422Type1 | AddIssueToCollectionResponse422Type2 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            issue_id=issue_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
