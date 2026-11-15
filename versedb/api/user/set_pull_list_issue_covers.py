from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.set_pull_list_issue_covers_body import SetPullListIssueCoversBody
from ...models.set_pull_list_issue_covers_response_200 import SetPullListIssueCoversResponse200
from ...models.set_pull_list_issue_covers_response_403 import SetPullListIssueCoversResponse403
from ...models.set_pull_list_issue_covers_response_404 import SetPullListIssueCoversResponse404
from ...models.set_pull_list_issue_covers_response_422 import SetPullListIssueCoversResponse422
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import Response


def _get_kwargs(
    issue_id: int,
    *,
    body: SetPullListIssueCoversBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/pull-list/issues/{issue_id}/covers".format(
            issue_id=quote(str(issue_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    SetPullListIssueCoversResponse200
    | SetPullListIssueCoversResponse403
    | SetPullListIssueCoversResponse404
    | SetPullListIssueCoversResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    if response.status_code == 200:
        response_200 = SetPullListIssueCoversResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = SetPullListIssueCoversResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = SetPullListIssueCoversResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = SetPullListIssueCoversResponse422.from_dict(response.json())

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
    SetPullListIssueCoversResponse200
    | SetPullListIssueCoversResponse403
    | SetPullListIssueCoversResponse404
    | SetPullListIssueCoversResponse422
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
    body: SetPullListIssueCoversBody,
) -> Response[
    SetPullListIssueCoversResponse200
    | SetPullListIssueCoversResponse403
    | SetPullListIssueCoversResponse404
    | SetPullListIssueCoversResponse422
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Set the covers of a pull list issue.

     Sets which covers of one issue the user is getting, replacing any earlier choice for that issue.
    Only variants of that issue count. Choosing exactly what the series' standing cover choice gives
    (`updatePullListItem`) clears the issue's own choice, so it follows the series again. Saving also
    takes the issue out of the user's skipped issues.

    Args:
        issue_id (int): The issue ID.
        body (SetPullListIssueCoversBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SetPullListIssueCoversResponse200 | SetPullListIssueCoversResponse403 | SetPullListIssueCoversResponse404 | SetPullListIssueCoversResponse422 | TooManyRequestsError | UnauthorizedError]
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
    body: SetPullListIssueCoversBody,
) -> (
    SetPullListIssueCoversResponse200
    | SetPullListIssueCoversResponse403
    | SetPullListIssueCoversResponse404
    | SetPullListIssueCoversResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Set the covers of a pull list issue.

     Sets which covers of one issue the user is getting, replacing any earlier choice for that issue.
    Only variants of that issue count. Choosing exactly what the series' standing cover choice gives
    (`updatePullListItem`) clears the issue's own choice, so it follows the series again. Saving also
    takes the issue out of the user's skipped issues.

    Args:
        issue_id (int): The issue ID.
        body (SetPullListIssueCoversBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SetPullListIssueCoversResponse200 | SetPullListIssueCoversResponse403 | SetPullListIssueCoversResponse404 | SetPullListIssueCoversResponse422 | TooManyRequestsError | UnauthorizedError
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
    body: SetPullListIssueCoversBody,
) -> Response[
    SetPullListIssueCoversResponse200
    | SetPullListIssueCoversResponse403
    | SetPullListIssueCoversResponse404
    | SetPullListIssueCoversResponse422
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Set the covers of a pull list issue.

     Sets which covers of one issue the user is getting, replacing any earlier choice for that issue.
    Only variants of that issue count. Choosing exactly what the series' standing cover choice gives
    (`updatePullListItem`) clears the issue's own choice, so it follows the series again. Saving also
    takes the issue out of the user's skipped issues.

    Args:
        issue_id (int): The issue ID.
        body (SetPullListIssueCoversBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SetPullListIssueCoversResponse200 | SetPullListIssueCoversResponse403 | SetPullListIssueCoversResponse404 | SetPullListIssueCoversResponse422 | TooManyRequestsError | UnauthorizedError]
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
    body: SetPullListIssueCoversBody,
) -> (
    SetPullListIssueCoversResponse200
    | SetPullListIssueCoversResponse403
    | SetPullListIssueCoversResponse404
    | SetPullListIssueCoversResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Set the covers of a pull list issue.

     Sets which covers of one issue the user is getting, replacing any earlier choice for that issue.
    Only variants of that issue count. Choosing exactly what the series' standing cover choice gives
    (`updatePullListItem`) clears the issue's own choice, so it follows the series again. Saving also
    takes the issue out of the user's skipped issues.

    Args:
        issue_id (int): The issue ID.
        body (SetPullListIssueCoversBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SetPullListIssueCoversResponse200 | SetPullListIssueCoversResponse403 | SetPullListIssueCoversResponse404 | SetPullListIssueCoversResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            issue_id=issue_id,
            client=client,
            body=body,
        )
    ).parsed
