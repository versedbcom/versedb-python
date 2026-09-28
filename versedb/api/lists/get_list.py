from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_list_response_200 import GetListResponse200
from ...models.get_list_response_403 import GetListResponse403
from ...models.get_list_response_404 import GetListResponse404
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    list_id: int,
    *,
    sort: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/lists/{list_id}".format(
            list_id=quote(str(list_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetListResponse200 | GetListResponse403 | GetListResponse404 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = GetListResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetListResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = TooManyRequestsError.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetListResponse200 | GetListResponse403 | GetListResponse404 | TooManyRequestsError | UnauthorizedError]:
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
    sort: str | Unset = UNSET,
) -> Response[GetListResponse200 | GetListResponse403 | GetListResponse404 | TooManyRequestsError | UnauthorizedError]:
    """Get list.

     Returns a single list with all its items. Private lists are only visible to owners.

    Args:
        list_id (int):
        sort (str | Unset): How to order the items. Omit for the list's own order — by
            position when it is ranked, newest added first when it is not. `recent` and `oldest`
            work on any list; the remaining values are the sortable fields for the list's entity
            type (`name`, `release_date`, `start_year`, `issues_count`, `launch_date`, `arc_order`),
            and are ignored on a mixed list, whose items span several tables.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetListResponse200 | GetListResponse403 | GetListResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    list_id: int,
    *,
    client: AuthenticatedClient | Client,
    sort: str | Unset = UNSET,
) -> GetListResponse200 | GetListResponse403 | GetListResponse404 | TooManyRequestsError | UnauthorizedError | None:
    """Get list.

     Returns a single list with all its items. Private lists are only visible to owners.

    Args:
        list_id (int):
        sort (str | Unset): How to order the items. Omit for the list's own order — by
            position when it is ranked, newest added first when it is not. `recent` and `oldest`
            work on any list; the remaining values are the sortable fields for the list's entity
            type (`name`, `release_date`, `start_year`, `issues_count`, `launch_date`, `arc_order`),
            and are ignored on a mixed list, whose items span several tables.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetListResponse200 | GetListResponse403 | GetListResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        list_id=list_id,
        client=client,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    list_id: int,
    *,
    client: AuthenticatedClient | Client,
    sort: str | Unset = UNSET,
) -> Response[GetListResponse200 | GetListResponse403 | GetListResponse404 | TooManyRequestsError | UnauthorizedError]:
    """Get list.

     Returns a single list with all its items. Private lists are only visible to owners.

    Args:
        list_id (int):
        sort (str | Unset): How to order the items. Omit for the list's own order — by
            position when it is ranked, newest added first when it is not. `recent` and `oldest`
            work on any list; the remaining values are the sortable fields for the list's entity
            type (`name`, `release_date`, `start_year`, `issues_count`, `launch_date`, `arc_order`),
            and are ignored on a mixed list, whose items span several tables.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetListResponse200 | GetListResponse403 | GetListResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    list_id: int,
    *,
    client: AuthenticatedClient | Client,
    sort: str | Unset = UNSET,
) -> GetListResponse200 | GetListResponse403 | GetListResponse404 | TooManyRequestsError | UnauthorizedError | None:
    """Get list.

     Returns a single list with all its items. Private lists are only visible to owners.

    Args:
        list_id (int):
        sort (str | Unset): How to order the items. Omit for the list's own order — by
            position when it is ranked, newest added first when it is not. `recent` and `oldest`
            work on any list; the remaining values are the sortable fields for the list's entity
            type (`name`, `release_date`, `start_year`, `issues_count`, `launch_date`, `arc_order`),
            and are ignored on a mixed list, whose items span several tables.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetListResponse200 | GetListResponse403 | GetListResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
            sort=sort,
        )
    ).parsed
