from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_pull_list_issue_covers_response_200 import GetPullListIssueCoversResponse200
from ...models.get_pull_list_issue_covers_response_403 import GetPullListIssueCoversResponse403
from ...models.get_pull_list_issue_covers_response_404 import GetPullListIssueCoversResponse404
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import Response


def _get_kwargs(
    issue_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/pull-list/issues/{issue_id}/covers".format(
            issue_id=quote(str(issue_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetPullListIssueCoversResponse200
    | GetPullListIssueCoversResponse403
    | GetPullListIssueCoversResponse404
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    if response.status_code == 200:
        response_200 = GetPullListIssueCoversResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetPullListIssueCoversResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetPullListIssueCoversResponse404.from_dict(response.json())

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
) -> Response[
    GetPullListIssueCoversResponse200
    | GetPullListIssueCoversResponse403
    | GetPullListIssueCoversResponse404
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
) -> Response[
    GetPullListIssueCoversResponse200
    | GetPullListIssueCoversResponse403
    | GetPullListIssueCoversResponse404
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Get the covers of a pull list issue.

     Returns the covers of one issue of a series on the user's pull list: the main cover (the standard
    cover), then each variant, regular covers first, then ratio covers, then exclusives, each marked
    `selected` when the user is getting it. A user who has chosen nothing is getting the main cover.

    Needs `read:user`.

    Args:
        issue_id (int): The issue ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPullListIssueCoversResponse200 | GetPullListIssueCoversResponse403 | GetPullListIssueCoversResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        issue_id=issue_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    issue_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetPullListIssueCoversResponse200
    | GetPullListIssueCoversResponse403
    | GetPullListIssueCoversResponse404
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Get the covers of a pull list issue.

     Returns the covers of one issue of a series on the user's pull list: the main cover (the standard
    cover), then each variant, regular covers first, then ratio covers, then exclusives, each marked
    `selected` when the user is getting it. A user who has chosen nothing is getting the main cover.

    Needs `read:user`.

    Args:
        issue_id (int): The issue ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPullListIssueCoversResponse200 | GetPullListIssueCoversResponse403 | GetPullListIssueCoversResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        issue_id=issue_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    issue_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetPullListIssueCoversResponse200
    | GetPullListIssueCoversResponse403
    | GetPullListIssueCoversResponse404
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Get the covers of a pull list issue.

     Returns the covers of one issue of a series on the user's pull list: the main cover (the standard
    cover), then each variant, regular covers first, then ratio covers, then exclusives, each marked
    `selected` when the user is getting it. A user who has chosen nothing is getting the main cover.

    Needs `read:user`.

    Args:
        issue_id (int): The issue ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPullListIssueCoversResponse200 | GetPullListIssueCoversResponse403 | GetPullListIssueCoversResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        issue_id=issue_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    issue_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetPullListIssueCoversResponse200
    | GetPullListIssueCoversResponse403
    | GetPullListIssueCoversResponse404
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Get the covers of a pull list issue.

     Returns the covers of one issue of a series on the user's pull list: the main cover (the standard
    cover), then each variant, regular covers first, then ratio covers, then exclusives, each marked
    `selected` when the user is getting it. A user who has chosen nothing is getting the main cover.

    Needs `read:user`.

    Args:
        issue_id (int): The issue ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPullListIssueCoversResponse200 | GetPullListIssueCoversResponse403 | GetPullListIssueCoversResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            issue_id=issue_id,
            client=client,
        )
    ).parsed
