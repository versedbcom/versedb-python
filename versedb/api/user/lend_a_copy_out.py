from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lend_a_copy_out_body import LendACopyOutBody
from ...models.lend_a_copy_out_response_200 import LendACopyOutResponse200
from ...models.lend_a_copy_out_response_404 import LendACopyOutResponse404
from ...models.lend_a_copy_out_response_409 import LendACopyOutResponse409
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import Response


def _get_kwargs(
    collection_item_id: int,
    *,
    body: LendACopyOutBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/user/collections/{collection_item_id}/loan".format(
            collection_item_id=quote(str(collection_item_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    LendACopyOutResponse200
    | LendACopyOutResponse404
    | LendACopyOutResponse409
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    if response.status_code == 200:
        response_200 = LendACopyOutResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = LendACopyOutResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = LendACopyOutResponse409.from_dict(response.json())

        return response_409

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
    LendACopyOutResponse200
    | LendACopyOutResponse404
    | LendACopyOutResponse409
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
    collection_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: LendACopyOutBody,
) -> Response[
    LendACopyOutResponse200
    | LendACopyOutResponse404
    | LendACopyOutResponse409
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Lend a copy out.

     A copy already out is a 409 rather than a silent replacement: two open loans on one
    physical comic is a mistake to report, and overwriting the first would lose who actually
    has it. Return it, then lend it again.

    Args:
        collection_item_id (int):
        body (LendACopyOutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LendACopyOutResponse200 | LendACopyOutResponse404 | LendACopyOutResponse409 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        collection_item_id=collection_item_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: LendACopyOutBody,
) -> (
    LendACopyOutResponse200
    | LendACopyOutResponse404
    | LendACopyOutResponse409
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Lend a copy out.

     A copy already out is a 409 rather than a silent replacement: two open loans on one
    physical comic is a mistake to report, and overwriting the first would lose who actually
    has it. Return it, then lend it again.

    Args:
        collection_item_id (int):
        body (LendACopyOutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LendACopyOutResponse200 | LendACopyOutResponse404 | LendACopyOutResponse409 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        collection_item_id=collection_item_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    collection_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: LendACopyOutBody,
) -> Response[
    LendACopyOutResponse200
    | LendACopyOutResponse404
    | LendACopyOutResponse409
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Lend a copy out.

     A copy already out is a 409 rather than a silent replacement: two open loans on one
    physical comic is a mistake to report, and overwriting the first would lose who actually
    has it. Return it, then lend it again.

    Args:
        collection_item_id (int):
        body (LendACopyOutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LendACopyOutResponse200 | LendACopyOutResponse404 | LendACopyOutResponse409 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        collection_item_id=collection_item_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: LendACopyOutBody,
) -> (
    LendACopyOutResponse200
    | LendACopyOutResponse404
    | LendACopyOutResponse409
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Lend a copy out.

     A copy already out is a 409 rather than a silent replacement: two open loans on one
    physical comic is a mistake to report, and overwriting the first would lose who actually
    has it. Return it, then lend it again.

    Args:
        collection_item_id (int):
        body (LendACopyOutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LendACopyOutResponse200 | LendACopyOutResponse404 | LendACopyOutResponse409 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            collection_item_id=collection_item_id,
            client=client,
            body=body,
        )
    ).parsed
