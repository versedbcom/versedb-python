from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.check_issue_in_collection_response_200 import CheckIssueInCollectionResponse200
from ...models.check_issue_in_collection_response_403 import CheckIssueInCollectionResponse403
from ...models.check_issue_in_collection_response_422 import CheckIssueInCollectionResponse422
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    issue_id: int,
    *,
    variant_id: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["variant_id"] = variant_id

    params["languages"] = languages

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/issues/{issue_id}/collection/check".format(
            issue_id=quote(str(issue_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CheckIssueInCollectionResponse200
    | CheckIssueInCollectionResponse403
    | CheckIssueInCollectionResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    if response.status_code == 200:
        response_200 = CheckIssueInCollectionResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = CheckIssueInCollectionResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = CheckIssueInCollectionResponse422.from_dict(response.json())

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
    CheckIssueInCollectionResponse200
    | CheckIssueInCollectionResponse403
    | CheckIssueInCollectionResponse422
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
    variant_id: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> Response[
    CheckIssueInCollectionResponse200
    | CheckIssueInCollectionResponse403
    | CheckIssueInCollectionResponse422
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Check issue in collection.

     Checks if an issue (optionally a specific variant) is in the user's collection: the copies still
    held (sold ones
    left out), oldest first, and the first of them in full.

    Needs `read:user`.

    Args:
        issue_id (int): The issue ID.
        variant_id (int | Unset): Specific variant ID to check (optional).
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckIssueInCollectionResponse200 | CheckIssueInCollectionResponse403 | CheckIssueInCollectionResponse422 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        issue_id=issue_id,
        variant_id=variant_id,
        languages=languages,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    issue_id: int,
    *,
    client: AuthenticatedClient | Client,
    variant_id: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> (
    CheckIssueInCollectionResponse200
    | CheckIssueInCollectionResponse403
    | CheckIssueInCollectionResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Check issue in collection.

     Checks if an issue (optionally a specific variant) is in the user's collection: the copies still
    held (sold ones
    left out), oldest first, and the first of them in full.

    Needs `read:user`.

    Args:
        issue_id (int): The issue ID.
        variant_id (int | Unset): Specific variant ID to check (optional).
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckIssueInCollectionResponse200 | CheckIssueInCollectionResponse403 | CheckIssueInCollectionResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        issue_id=issue_id,
        client=client,
        variant_id=variant_id,
        languages=languages,
    ).parsed


async def asyncio_detailed(
    issue_id: int,
    *,
    client: AuthenticatedClient | Client,
    variant_id: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> Response[
    CheckIssueInCollectionResponse200
    | CheckIssueInCollectionResponse403
    | CheckIssueInCollectionResponse422
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Check issue in collection.

     Checks if an issue (optionally a specific variant) is in the user's collection: the copies still
    held (sold ones
    left out), oldest first, and the first of them in full.

    Needs `read:user`.

    Args:
        issue_id (int): The issue ID.
        variant_id (int | Unset): Specific variant ID to check (optional).
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckIssueInCollectionResponse200 | CheckIssueInCollectionResponse403 | CheckIssueInCollectionResponse422 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        issue_id=issue_id,
        variant_id=variant_id,
        languages=languages,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    issue_id: int,
    *,
    client: AuthenticatedClient | Client,
    variant_id: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> (
    CheckIssueInCollectionResponse200
    | CheckIssueInCollectionResponse403
    | CheckIssueInCollectionResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Check issue in collection.

     Checks if an issue (optionally a specific variant) is in the user's collection: the copies still
    held (sold ones
    left out), oldest first, and the first of them in full.

    Needs `read:user`.

    Args:
        issue_id (int): The issue ID.
        variant_id (int | Unset): Specific variant ID to check (optional).
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckIssueInCollectionResponse200 | CheckIssueInCollectionResponse403 | CheckIssueInCollectionResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            issue_id=issue_id,
            client=client,
            variant_id=variant_id,
            languages=languages,
        )
    ).parsed
