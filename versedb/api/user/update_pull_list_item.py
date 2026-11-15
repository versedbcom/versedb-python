from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...models.update_pull_list_item_body import UpdatePullListItemBody
from ...models.update_pull_list_item_response_200 import UpdatePullListItemResponse200
from ...models.update_pull_list_item_response_403 import UpdatePullListItemResponse403
from ...models.update_pull_list_item_response_404 import UpdatePullListItemResponse404
from ...models.update_pull_list_item_response_422 import UpdatePullListItemResponse422
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: int,
    *,
    body: UpdatePullListItemBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/pull-list/items/{item_id}".format(
            item_id=quote(str(item_id), safe=""),
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
    TooManyRequestsError
    | UnauthorizedError
    | UpdatePullListItemResponse200
    | UpdatePullListItemResponse403
    | UpdatePullListItemResponse404
    | UpdatePullListItemResponse422
    | None
):
    if response.status_code == 200:
        response_200 = UpdatePullListItemResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UpdatePullListItemResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdatePullListItemResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = UpdatePullListItemResponse422.from_dict(response.json())

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
    TooManyRequestsError
    | UnauthorizedError
    | UpdatePullListItemResponse200
    | UpdatePullListItemResponse403
    | UpdatePullListItemResponse404
    | UpdatePullListItemResponse422
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePullListItemBody | Unset = UNSET,
) -> Response[
    TooManyRequestsError
    | UnauthorizedError
    | UpdatePullListItemResponse200
    | UpdatePullListItemResponse403
    | UpdatePullListItemResponse404
    | UpdatePullListItemResponse422
]:
    """Update a pull list entry.

     Changes one series on the authenticated user's pull list: its status, notes, places, or the standing
    cover choice. The standing choice applies to every issue of the series the user hasn't chosen covers
    of (see `setPullListIssueCovers`), covers added to the catalog later included: `standard` the main
    cover; `standard_and_regular` the main cover and every regular cover; `regular` every regular cover
    without the main one, or the main cover when an issue has none. Ratio and exclusive covers are only
    ever chosen per issue. Send at least one field.

    Args:
        item_id (int): The series ID of the pull list entry.
        body (UpdatePullListItemBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TooManyRequestsError | UnauthorizedError | UpdatePullListItemResponse200 | UpdatePullListItemResponse403 | UpdatePullListItemResponse404 | UpdatePullListItemResponse422]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePullListItemBody | Unset = UNSET,
) -> (
    TooManyRequestsError
    | UnauthorizedError
    | UpdatePullListItemResponse200
    | UpdatePullListItemResponse403
    | UpdatePullListItemResponse404
    | UpdatePullListItemResponse422
    | None
):
    """Update a pull list entry.

     Changes one series on the authenticated user's pull list: its status, notes, places, or the standing
    cover choice. The standing choice applies to every issue of the series the user hasn't chosen covers
    of (see `setPullListIssueCovers`), covers added to the catalog later included: `standard` the main
    cover; `standard_and_regular` the main cover and every regular cover; `regular` every regular cover
    without the main one, or the main cover when an issue has none. Ratio and exclusive covers are only
    ever chosen per issue. Send at least one field.

    Args:
        item_id (int): The series ID of the pull list entry.
        body (UpdatePullListItemBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TooManyRequestsError | UnauthorizedError | UpdatePullListItemResponse200 | UpdatePullListItemResponse403 | UpdatePullListItemResponse404 | UpdatePullListItemResponse422
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePullListItemBody | Unset = UNSET,
) -> Response[
    TooManyRequestsError
    | UnauthorizedError
    | UpdatePullListItemResponse200
    | UpdatePullListItemResponse403
    | UpdatePullListItemResponse404
    | UpdatePullListItemResponse422
]:
    """Update a pull list entry.

     Changes one series on the authenticated user's pull list: its status, notes, places, or the standing
    cover choice. The standing choice applies to every issue of the series the user hasn't chosen covers
    of (see `setPullListIssueCovers`), covers added to the catalog later included: `standard` the main
    cover; `standard_and_regular` the main cover and every regular cover; `regular` every regular cover
    without the main one, or the main cover when an issue has none. Ratio and exclusive covers are only
    ever chosen per issue. Send at least one field.

    Args:
        item_id (int): The series ID of the pull list entry.
        body (UpdatePullListItemBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TooManyRequestsError | UnauthorizedError | UpdatePullListItemResponse200 | UpdatePullListItemResponse403 | UpdatePullListItemResponse404 | UpdatePullListItemResponse422]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePullListItemBody | Unset = UNSET,
) -> (
    TooManyRequestsError
    | UnauthorizedError
    | UpdatePullListItemResponse200
    | UpdatePullListItemResponse403
    | UpdatePullListItemResponse404
    | UpdatePullListItemResponse422
    | None
):
    """Update a pull list entry.

     Changes one series on the authenticated user's pull list: its status, notes, places, or the standing
    cover choice. The standing choice applies to every issue of the series the user hasn't chosen covers
    of (see `setPullListIssueCovers`), covers added to the catalog later included: `standard` the main
    cover; `standard_and_regular` the main cover and every regular cover; `regular` every regular cover
    without the main one, or the main cover when an issue has none. Ratio and exclusive covers are only
    ever chosen per issue. Send at least one field.

    Args:
        item_id (int): The series ID of the pull list entry.
        body (UpdatePullListItemBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TooManyRequestsError | UnauthorizedError | UpdatePullListItemResponse200 | UpdatePullListItemResponse403 | UpdatePullListItemResponse404 | UpdatePullListItemResponse422
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            body=body,
        )
    ).parsed
