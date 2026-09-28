from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...models.unsave_list_response_200_type_0 import UnsaveListResponse200Type0
from ...models.unsave_list_response_200_type_1 import UnsaveListResponse200Type1
from ...types import Response


def _get_kwargs(
    list_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/lists/{list_id}/save".format(
            list_id=quote(str(list_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TooManyRequestsError | UnauthorizedError | UnsaveListResponse200Type0 | UnsaveListResponse200Type1 | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> UnsaveListResponse200Type0 | UnsaveListResponse200Type1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = UnsaveListResponse200Type0.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = UnsaveListResponse200Type1.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 429:
        response_429 = TooManyRequestsError.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TooManyRequestsError | UnauthorizedError | UnsaveListResponse200Type0 | UnsaveListResponse200Type1]:
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
) -> Response[TooManyRequestsError | UnauthorizedError | UnsaveListResponse200Type0 | UnsaveListResponse200Type1]:
    """Unsave list.

     Removes a list from the user's saved lists.

    Args:
        list_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TooManyRequestsError | UnauthorizedError | UnsaveListResponse200Type0 | UnsaveListResponse200Type1]
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
) -> TooManyRequestsError | UnauthorizedError | UnsaveListResponse200Type0 | UnsaveListResponse200Type1 | None:
    """Unsave list.

     Removes a list from the user's saved lists.

    Args:
        list_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TooManyRequestsError | UnauthorizedError | UnsaveListResponse200Type0 | UnsaveListResponse200Type1
    """

    return sync_detailed(
        list_id=list_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    list_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[TooManyRequestsError | UnauthorizedError | UnsaveListResponse200Type0 | UnsaveListResponse200Type1]:
    """Unsave list.

     Removes a list from the user's saved lists.

    Args:
        list_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TooManyRequestsError | UnauthorizedError | UnsaveListResponse200Type0 | UnsaveListResponse200Type1]
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
) -> TooManyRequestsError | UnauthorizedError | UnsaveListResponse200Type0 | UnsaveListResponse200Type1 | None:
    """Unsave list.

     Removes a list from the user's saved lists.

    Args:
        list_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TooManyRequestsError | UnauthorizedError | UnsaveListResponse200Type0 | UnsaveListResponse200Type1
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
        )
    ).parsed
