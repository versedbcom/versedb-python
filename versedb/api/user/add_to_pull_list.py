from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_to_pull_list_body import AddToPullListBody
from ...models.add_to_pull_list_response_201 import AddToPullListResponse201
from ...models.add_to_pull_list_response_422 import AddToPullListResponse422
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import Response


def _get_kwargs(
    *,
    body: AddToPullListBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/pull-list/items",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddToPullListResponse201 | AddToPullListResponse422 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 201:
        response_201 = AddToPullListResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 422:
        response_422 = AddToPullListResponse422.from_dict(response.json())

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
) -> Response[AddToPullListResponse201 | AddToPullListResponse422 | TooManyRequestsError | UnauthorizedError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AddToPullListBody,
) -> Response[AddToPullListResponse201 | AddToPullListResponse422 | TooManyRequestsError | UnauthorizedError]:
    """Add to pull list.

     Adds a series to the user's pull list to track new releases.

    Args:
        body (AddToPullListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddToPullListResponse201 | AddToPullListResponse422 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: AddToPullListBody,
) -> AddToPullListResponse201 | AddToPullListResponse422 | TooManyRequestsError | UnauthorizedError | None:
    """Add to pull list.

     Adds a series to the user's pull list to track new releases.

    Args:
        body (AddToPullListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddToPullListResponse201 | AddToPullListResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AddToPullListBody,
) -> Response[AddToPullListResponse201 | AddToPullListResponse422 | TooManyRequestsError | UnauthorizedError]:
    """Add to pull list.

     Adds a series to the user's pull list to track new releases.

    Args:
        body (AddToPullListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddToPullListResponse201 | AddToPullListResponse422 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AddToPullListBody,
) -> AddToPullListResponse201 | AddToPullListResponse422 | TooManyRequestsError | UnauthorizedError | None:
    """Add to pull list.

     Adds a series to the user's pull list to track new releases.

    Args:
        body (AddToPullListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddToPullListResponse201 | AddToPullListResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
