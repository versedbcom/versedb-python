from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.merge_a_list_into_this_one_body import MergeAListIntoThisOneBody
from ...models.merge_a_list_into_this_one_response_200 import MergeAListIntoThisOneResponse200
from ...models.merge_a_list_into_this_one_response_403 import MergeAListIntoThisOneResponse403
from ...models.merge_a_list_into_this_one_response_422 import MergeAListIntoThisOneResponse422
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import Response


def _get_kwargs(
    list_id: int,
    *,
    body: MergeAListIntoThisOneBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/lists/{list_id}/merge".format(
            list_id=quote(str(list_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    MergeAListIntoThisOneResponse200
    | MergeAListIntoThisOneResponse403
    | MergeAListIntoThisOneResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    if response.status_code == 200:
        response_200 = MergeAListIntoThisOneResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = MergeAListIntoThisOneResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = MergeAListIntoThisOneResponse422.from_dict(response.json())

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
    MergeAListIntoThisOneResponse200
    | MergeAListIntoThisOneResponse403
    | MergeAListIntoThisOneResponse422
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
    list_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: MergeAListIntoThisOneBody,
) -> Response[
    MergeAListIntoThisOneResponse200
    | MergeAListIntoThisOneResponse403
    | MergeAListIntoThisOneResponse422
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Merge a list into this one.

     Pulls every item from the source list into this (destination) list, skipping items already
    present (by entity + variant) and appending the rest. Both lists must be owned by the
    authenticated user. Merging items of a different type opens this list to any type.

    Args:
        list_id (int):
        body (MergeAListIntoThisOneBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MergeAListIntoThisOneResponse200 | MergeAListIntoThisOneResponse403 | MergeAListIntoThisOneResponse422 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    list_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: MergeAListIntoThisOneBody,
) -> (
    MergeAListIntoThisOneResponse200
    | MergeAListIntoThisOneResponse403
    | MergeAListIntoThisOneResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Merge a list into this one.

     Pulls every item from the source list into this (destination) list, skipping items already
    present (by entity + variant) and appending the rest. Both lists must be owned by the
    authenticated user. Merging items of a different type opens this list to any type.

    Args:
        list_id (int):
        body (MergeAListIntoThisOneBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MergeAListIntoThisOneResponse200 | MergeAListIntoThisOneResponse403 | MergeAListIntoThisOneResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        list_id=list_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    list_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: MergeAListIntoThisOneBody,
) -> Response[
    MergeAListIntoThisOneResponse200
    | MergeAListIntoThisOneResponse403
    | MergeAListIntoThisOneResponse422
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Merge a list into this one.

     Pulls every item from the source list into this (destination) list, skipping items already
    present (by entity + variant) and appending the rest. Both lists must be owned by the
    authenticated user. Merging items of a different type opens this list to any type.

    Args:
        list_id (int):
        body (MergeAListIntoThisOneBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MergeAListIntoThisOneResponse200 | MergeAListIntoThisOneResponse403 | MergeAListIntoThisOneResponse422 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    list_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: MergeAListIntoThisOneBody,
) -> (
    MergeAListIntoThisOneResponse200
    | MergeAListIntoThisOneResponse403
    | MergeAListIntoThisOneResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Merge a list into this one.

     Pulls every item from the source list into this (destination) list, skipping items already
    present (by entity + variant) and appending the rest. Both lists must be owned by the
    authenticated user. Merging items of a different type opens this list to any type.

    Args:
        list_id (int):
        body (MergeAListIntoThisOneBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MergeAListIntoThisOneResponse200 | MergeAListIntoThisOneResponse403 | MergeAListIntoThisOneResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
            body=body,
        )
    ).parsed
