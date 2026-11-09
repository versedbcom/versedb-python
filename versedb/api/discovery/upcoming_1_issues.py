from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...models.upcoming_1_issues_response_200 import Upcoming1IssuesResponse200
from ...models.upcoming_1_issues_response_403 import Upcoming1IssuesResponse403
from ...models.upcoming_1_issues_response_422 import Upcoming1IssuesResponse422
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    days: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["page"] = page

    params["days"] = days

    params["languages"] = languages

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/discovery/upcoming-firsts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TooManyRequestsError
    | UnauthorizedError
    | Upcoming1IssuesResponse200
    | Upcoming1IssuesResponse403
    | Upcoming1IssuesResponse422
    | None
):
    if response.status_code == 200:
        response_200 = Upcoming1IssuesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Upcoming1IssuesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = Upcoming1IssuesResponse422.from_dict(response.json())

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
    | Upcoming1IssuesResponse200
    | Upcoming1IssuesResponse403
    | Upcoming1IssuesResponse422
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
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    days: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> Response[
    TooManyRequestsError
    | UnauthorizedError
    | Upcoming1IssuesResponse200
    | Upcoming1IssuesResponse403
    | Upcoming1IssuesResponse422
]:
    """Upcoming #1 issues.

     Returns upcoming first issues (#1) from new ongoing series within the next N days.
    Useful for discovering new series launches.

    Args:
        limit (int | Unset): Results per page (1-50).
        page (int | Unset): Page number; meta.last_page says where the list ends.
        days (int | Unset): Lookahead window in days (1-90).
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TooManyRequestsError | UnauthorizedError | Upcoming1IssuesResponse200 | Upcoming1IssuesResponse403 | Upcoming1IssuesResponse422]
    """

    kwargs = _get_kwargs(
        limit=limit,
        page=page,
        days=days,
        languages=languages,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    days: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> (
    TooManyRequestsError
    | UnauthorizedError
    | Upcoming1IssuesResponse200
    | Upcoming1IssuesResponse403
    | Upcoming1IssuesResponse422
    | None
):
    """Upcoming #1 issues.

     Returns upcoming first issues (#1) from new ongoing series within the next N days.
    Useful for discovering new series launches.

    Args:
        limit (int | Unset): Results per page (1-50).
        page (int | Unset): Page number; meta.last_page says where the list ends.
        days (int | Unset): Lookahead window in days (1-90).
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TooManyRequestsError | UnauthorizedError | Upcoming1IssuesResponse200 | Upcoming1IssuesResponse403 | Upcoming1IssuesResponse422
    """

    return sync_detailed(
        client=client,
        limit=limit,
        page=page,
        days=days,
        languages=languages,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    days: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> Response[
    TooManyRequestsError
    | UnauthorizedError
    | Upcoming1IssuesResponse200
    | Upcoming1IssuesResponse403
    | Upcoming1IssuesResponse422
]:
    """Upcoming #1 issues.

     Returns upcoming first issues (#1) from new ongoing series within the next N days.
    Useful for discovering new series launches.

    Args:
        limit (int | Unset): Results per page (1-50).
        page (int | Unset): Page number; meta.last_page says where the list ends.
        days (int | Unset): Lookahead window in days (1-90).
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TooManyRequestsError | UnauthorizedError | Upcoming1IssuesResponse200 | Upcoming1IssuesResponse403 | Upcoming1IssuesResponse422]
    """

    kwargs = _get_kwargs(
        limit=limit,
        page=page,
        days=days,
        languages=languages,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    days: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> (
    TooManyRequestsError
    | UnauthorizedError
    | Upcoming1IssuesResponse200
    | Upcoming1IssuesResponse403
    | Upcoming1IssuesResponse422
    | None
):
    """Upcoming #1 issues.

     Returns upcoming first issues (#1) from new ongoing series within the next N days.
    Useful for discovering new series launches.

    Args:
        limit (int | Unset): Results per page (1-50).
        page (int | Unset): Page number; meta.last_page says where the list ends.
        days (int | Unset): Lookahead window in days (1-90).
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TooManyRequestsError | UnauthorizedError | Upcoming1IssuesResponse200 | Upcoming1IssuesResponse403 | Upcoming1IssuesResponse422
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            page=page,
            days=days,
            languages=languages,
        )
    ).parsed
