from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.follow_content_body import FollowContentBody
from ...models.follow_content_response_200_type_0 import FollowContentResponse200Type0
from ...models.follow_content_response_200_type_1 import FollowContentResponse200Type1
from ...models.follow_content_response_403 import FollowContentResponse403
from ...models.follow_content_response_404 import FollowContentResponse404
from ...models.follow_content_response_422 import FollowContentResponse422
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import Response


def _get_kwargs(
    *,
    body: FollowContentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/follow",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FollowContentResponse200Type0
    | FollowContentResponse200Type1
    | FollowContentResponse403
    | FollowContentResponse404
    | FollowContentResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    if response.status_code == 200:

        def _parse_response_200(data: object) -> FollowContentResponse200Type0 | FollowContentResponse200Type1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = FollowContentResponse200Type0.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = FollowContentResponse200Type1.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FollowContentResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = FollowContentResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = FollowContentResponse422.from_dict(response.json())

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
    FollowContentResponse200Type0
    | FollowContentResponse200Type1
    | FollowContentResponse403
    | FollowContentResponse404
    | FollowContentResponse422
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
    *,
    client: AuthenticatedClient | Client,
    body: FollowContentBody,
) -> Response[
    FollowContentResponse200Type0
    | FollowContentResponse200Type1
    | FollowContentResponse403
    | FollowContentResponse404
    | FollowContentResponse422
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Follow content.

     Follows a title, character, podcast, creator, publisher, team, story arc, comic shop, event, event
    franchise, or user. Following an event that belongs to a franchise follows the franchise too.

    Args:
        body (FollowContentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FollowContentResponse200Type0 | FollowContentResponse200Type1 | FollowContentResponse403 | FollowContentResponse404 | FollowContentResponse422 | TooManyRequestsError | UnauthorizedError]
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
    body: FollowContentBody,
) -> (
    FollowContentResponse200Type0
    | FollowContentResponse200Type1
    | FollowContentResponse403
    | FollowContentResponse404
    | FollowContentResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Follow content.

     Follows a title, character, podcast, creator, publisher, team, story arc, comic shop, event, event
    franchise, or user. Following an event that belongs to a franchise follows the franchise too.

    Args:
        body (FollowContentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FollowContentResponse200Type0 | FollowContentResponse200Type1 | FollowContentResponse403 | FollowContentResponse404 | FollowContentResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FollowContentBody,
) -> Response[
    FollowContentResponse200Type0
    | FollowContentResponse200Type1
    | FollowContentResponse403
    | FollowContentResponse404
    | FollowContentResponse422
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Follow content.

     Follows a title, character, podcast, creator, publisher, team, story arc, comic shop, event, event
    franchise, or user. Following an event that belongs to a franchise follows the franchise too.

    Args:
        body (FollowContentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FollowContentResponse200Type0 | FollowContentResponse200Type1 | FollowContentResponse403 | FollowContentResponse404 | FollowContentResponse422 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FollowContentBody,
) -> (
    FollowContentResponse200Type0
    | FollowContentResponse200Type1
    | FollowContentResponse403
    | FollowContentResponse404
    | FollowContentResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Follow content.

     Follows a title, character, podcast, creator, publisher, team, story arc, comic shop, event, event
    franchise, or user. Following an event that belongs to a franchise follows the franchise too.

    Args:
        body (FollowContentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FollowContentResponse200Type0 | FollowContentResponse200Type1 | FollowContentResponse403 | FollowContentResponse404 | FollowContentResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
