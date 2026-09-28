from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.mark_as_read_body import MarkAsReadBody
from ...models.mark_as_read_response_201 import MarkAsReadResponse201
from ...models.mark_as_read_response_422 import MarkAsReadResponse422
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    issue_id: int,
    *,
    body: MarkAsReadBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/issues/{issue_id}/read-status".format(
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
) -> MarkAsReadResponse201 | MarkAsReadResponse422 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 201:
        response_201 = MarkAsReadResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 422:
        response_422 = MarkAsReadResponse422.from_dict(response.json())

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
) -> Response[MarkAsReadResponse201 | MarkAsReadResponse422 | TooManyRequestsError | UnauthorizedError]:
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
    body: MarkAsReadBody | Unset = UNSET,
) -> Response[MarkAsReadResponse201 | MarkAsReadResponse422 | TooManyRequestsError | UnauthorizedError]:
    """Mark as read.

     Marks an issue (optionally a specific variant) as read with the current timestamp.

    Args:
        issue_id (int):
        body (MarkAsReadBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MarkAsReadResponse201 | MarkAsReadResponse422 | TooManyRequestsError | UnauthorizedError]
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
    body: MarkAsReadBody | Unset = UNSET,
) -> MarkAsReadResponse201 | MarkAsReadResponse422 | TooManyRequestsError | UnauthorizedError | None:
    """Mark as read.

     Marks an issue (optionally a specific variant) as read with the current timestamp.

    Args:
        issue_id (int):
        body (MarkAsReadBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MarkAsReadResponse201 | MarkAsReadResponse422 | TooManyRequestsError | UnauthorizedError
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
    body: MarkAsReadBody | Unset = UNSET,
) -> Response[MarkAsReadResponse201 | MarkAsReadResponse422 | TooManyRequestsError | UnauthorizedError]:
    """Mark as read.

     Marks an issue (optionally a specific variant) as read with the current timestamp.

    Args:
        issue_id (int):
        body (MarkAsReadBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MarkAsReadResponse201 | MarkAsReadResponse422 | TooManyRequestsError | UnauthorizedError]
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
    body: MarkAsReadBody | Unset = UNSET,
) -> MarkAsReadResponse201 | MarkAsReadResponse422 | TooManyRequestsError | UnauthorizedError | None:
    """Mark as read.

     Marks an issue (optionally a specific variant) as read with the current timestamp.

    Args:
        issue_id (int):
        body (MarkAsReadBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MarkAsReadResponse201 | MarkAsReadResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            issue_id=issue_id,
            client=client,
            body=body,
        )
    ).parsed
