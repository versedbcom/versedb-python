from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_key_issue_reasons_response_200 import ListKeyIssueReasonsResponse200
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    category: str | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["category"] = category

    params["q"] = q

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/key-issue-reasons",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListKeyIssueReasonsResponse200 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = ListKeyIssueReasonsResponse200.from_dict(response.json())

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
) -> Response[ListKeyIssueReasonsResponse200 | TooManyRequestsError | UnauthorizedError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    category: str | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ListKeyIssueReasonsResponse200 | TooManyRequestsError | UnauthorizedError]:
    """List key issue reasons.

     Returns active key issue reasons, optionally filtered by category or name. Reasons are written
    per issue rather than drawn from a fixed vocabulary, so there are far more of them than the
    category list suggests — pass `q` and `limit` for a picker rather than fetching the lot.

    Args:
        category (str | Unset): Filter by category (appearance, story, creator, market, media).
        q (str | Unset): Match reasons whose name contains this.
        limit (int | Unset): Cap the number returned (1-100). Applied only when q is present.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListKeyIssueReasonsResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        category=category,
        q=q,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    category: str | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ListKeyIssueReasonsResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """List key issue reasons.

     Returns active key issue reasons, optionally filtered by category or name. Reasons are written
    per issue rather than drawn from a fixed vocabulary, so there are far more of them than the
    category list suggests — pass `q` and `limit` for a picker rather than fetching the lot.

    Args:
        category (str | Unset): Filter by category (appearance, story, creator, market, media).
        q (str | Unset): Match reasons whose name contains this.
        limit (int | Unset): Cap the number returned (1-100). Applied only when q is present.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListKeyIssueReasonsResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        client=client,
        category=category,
        q=q,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    category: str | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ListKeyIssueReasonsResponse200 | TooManyRequestsError | UnauthorizedError]:
    """List key issue reasons.

     Returns active key issue reasons, optionally filtered by category or name. Reasons are written
    per issue rather than drawn from a fixed vocabulary, so there are far more of them than the
    category list suggests — pass `q` and `limit` for a picker rather than fetching the lot.

    Args:
        category (str | Unset): Filter by category (appearance, story, creator, market, media).
        q (str | Unset): Match reasons whose name contains this.
        limit (int | Unset): Cap the number returned (1-100). Applied only when q is present.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListKeyIssueReasonsResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        category=category,
        q=q,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    category: str | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ListKeyIssueReasonsResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """List key issue reasons.

     Returns active key issue reasons, optionally filtered by category or name. Reasons are written
    per issue rather than drawn from a fixed vocabulary, so there are far more of them than the
    category list suggests — pass `q` and `limit` for a picker rather than fetching the lot.

    Args:
        category (str | Unset): Filter by category (appearance, story, creator, market, media).
        q (str | Unset): Match reasons whose name contains this.
        limit (int | Unset): Cap the number returned (1-100). Applied only when q is present.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListKeyIssueReasonsResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            client=client,
            category=category,
            q=q,
            limit=limit,
        )
    ).parsed
