from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_issue_to_collection_body import AddIssueToCollectionBody
from ...models.add_issue_to_collection_response_201 import AddIssueToCollectionResponse201
from ...models.add_issue_to_collection_response_403 import AddIssueToCollectionResponse403
from ...models.add_issue_to_collection_response_422 import AddIssueToCollectionResponse422
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    issue_id: int,
    *,
    body: AddIssueToCollectionBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

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
    | AddIssueToCollectionResponse403
    | AddIssueToCollectionResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    if response.status_code == 201:
        response_201 = AddIssueToCollectionResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AddIssueToCollectionResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = AddIssueToCollectionResponse422.from_dict(response.json())

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
    | AddIssueToCollectionResponse403
    | AddIssueToCollectionResponse422
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
) -> Response[
    AddIssueToCollectionResponse201
    | AddIssueToCollectionResponse403
    | AddIssueToCollectionResponse422
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Add issue to collection.

     Adds an issue to the user's default collection. Works for all users (no PRO required).
    This is the recommended endpoint for mobile collection management.

    Args:
        issue_id (int):
        body (AddIssueToCollectionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddIssueToCollectionResponse201 | AddIssueToCollectionResponse403 | AddIssueToCollectionResponse422 | TooManyRequestsError | UnauthorizedError]
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
    body: AddIssueToCollectionBody | Unset = UNSET,
) -> (
    AddIssueToCollectionResponse201
    | AddIssueToCollectionResponse403
    | AddIssueToCollectionResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Add issue to collection.

     Adds an issue to the user's default collection. Works for all users (no PRO required).
    This is the recommended endpoint for mobile collection management.

    Args:
        issue_id (int):
        body (AddIssueToCollectionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddIssueToCollectionResponse201 | AddIssueToCollectionResponse403 | AddIssueToCollectionResponse422 | TooManyRequestsError | UnauthorizedError
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
    body: AddIssueToCollectionBody | Unset = UNSET,
) -> Response[
    AddIssueToCollectionResponse201
    | AddIssueToCollectionResponse403
    | AddIssueToCollectionResponse422
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Add issue to collection.

     Adds an issue to the user's default collection. Works for all users (no PRO required).
    This is the recommended endpoint for mobile collection management.

    Args:
        issue_id (int):
        body (AddIssueToCollectionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddIssueToCollectionResponse201 | AddIssueToCollectionResponse403 | AddIssueToCollectionResponse422 | TooManyRequestsError | UnauthorizedError]
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
    body: AddIssueToCollectionBody | Unset = UNSET,
) -> (
    AddIssueToCollectionResponse201
    | AddIssueToCollectionResponse403
    | AddIssueToCollectionResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Add issue to collection.

     Adds an issue to the user's default collection. Works for all users (no PRO required).
    This is the recommended endpoint for mobile collection management.

    Args:
        issue_id (int):
        body (AddIssueToCollectionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddIssueToCollectionResponse201 | AddIssueToCollectionResponse403 | AddIssueToCollectionResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            issue_id=issue_id,
            client=client,
            body=body,
        )
    ).parsed
