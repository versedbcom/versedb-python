from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.open_a_list_to_any_type_response_200 import OpenAListToAnyTypeResponse200
from ...models.open_a_list_to_any_type_response_403 import OpenAListToAnyTypeResponse403
from ...models.open_a_list_to_any_type_response_422 import OpenAListToAnyTypeResponse422
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import Response


def _get_kwargs(
    list_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/lists/{list_id}/convert-to-mixed".format(
            list_id=quote(str(list_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    OpenAListToAnyTypeResponse200
    | OpenAListToAnyTypeResponse403
    | OpenAListToAnyTypeResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    if response.status_code == 200:
        response_200 = OpenAListToAnyTypeResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = OpenAListToAnyTypeResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = OpenAListToAnyTypeResponse422.from_dict(response.json())

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
    OpenAListToAnyTypeResponse200
    | OpenAListToAnyTypeResponse403
    | OpenAListToAnyTypeResponse422
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
) -> Response[
    OpenAListToAnyTypeResponse200
    | OpenAListToAnyTypeResponse403
    | OpenAListToAnyTypeResponse422
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Open a list to any type.

     One-way: broadens a single-type list so it can hold items of any type. Existing items keep
    their own type. It cannot be narrowed back, and a wishlist already holds any type.

    Args:
        list_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpenAListToAnyTypeResponse200 | OpenAListToAnyTypeResponse403 | OpenAListToAnyTypeResponse422 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    list_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> (
    OpenAListToAnyTypeResponse200
    | OpenAListToAnyTypeResponse403
    | OpenAListToAnyTypeResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Open a list to any type.

     One-way: broadens a single-type list so it can hold items of any type. Existing items keep
    their own type. It cannot be narrowed back, and a wishlist already holds any type.

    Args:
        list_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpenAListToAnyTypeResponse200 | OpenAListToAnyTypeResponse403 | OpenAListToAnyTypeResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        list_id=list_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    list_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    OpenAListToAnyTypeResponse200
    | OpenAListToAnyTypeResponse403
    | OpenAListToAnyTypeResponse422
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Open a list to any type.

     One-way: broadens a single-type list so it can hold items of any type. Existing items keep
    their own type. It cannot be narrowed back, and a wishlist already holds any type.

    Args:
        list_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpenAListToAnyTypeResponse200 | OpenAListToAnyTypeResponse403 | OpenAListToAnyTypeResponse422 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    list_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> (
    OpenAListToAnyTypeResponse200
    | OpenAListToAnyTypeResponse403
    | OpenAListToAnyTypeResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Open a list to any type.

     One-way: broadens a single-type list so it can hold items of any type. Existing items keep
    their own type. It cannot be narrowed back, and a wishlist already holds any type.

    Args:
        list_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpenAListToAnyTypeResponse200 | OpenAListToAnyTypeResponse403 | OpenAListToAnyTypeResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
        )
    ).parsed
