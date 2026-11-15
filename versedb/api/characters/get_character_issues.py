from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_character_issues_response_200 import GetCharacterIssuesResponse200
from ...models.get_character_issues_response_403 import GetCharacterIssuesResponse403
from ...models.get_character_issues_response_404 import GetCharacterIssuesResponse404
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    character_id: int,
    *,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    medium: str | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["limit"] = limit

    params["page"] = page

    params["medium"] = medium

    params["languages"] = languages

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/characters/{character_id}/issues".format(
            character_id=quote(str(character_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetCharacterIssuesResponse200
    | GetCharacterIssuesResponse403
    | GetCharacterIssuesResponse404
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    if response.status_code == 200:
        response_200 = GetCharacterIssuesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetCharacterIssuesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetCharacterIssuesResponse404.from_dict(response.json())

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
    GetCharacterIssuesResponse200
    | GetCharacterIssuesResponse403
    | GetCharacterIssuesResponse404
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
    character_id: int,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    medium: str | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> Response[
    GetCharacterIssuesResponse200
    | GetCharacterIssuesResponse403
    | GetCharacterIssuesResponse404
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Get character issues.

     Returns paginated issues where the character appears, ordered by release date.

    Args:
        character_id (int): The character ID.
        q (str | Unset): Optional case-insensitive search within these results.
        limit (int | Unset): Results per page (max 50).
        page (int | Unset): Page number; meta.last_page says where the list ends.
        medium (str | Unset): Comma-separated series mediums to filter by (comic, manga, manhwa,
            manhua, bande_dessinee, magazine).
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCharacterIssuesResponse200 | GetCharacterIssuesResponse403 | GetCharacterIssuesResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        character_id=character_id,
        q=q,
        limit=limit,
        page=page,
        medium=medium,
        languages=languages,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    character_id: int,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    medium: str | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> (
    GetCharacterIssuesResponse200
    | GetCharacterIssuesResponse403
    | GetCharacterIssuesResponse404
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Get character issues.

     Returns paginated issues where the character appears, ordered by release date.

    Args:
        character_id (int): The character ID.
        q (str | Unset): Optional case-insensitive search within these results.
        limit (int | Unset): Results per page (max 50).
        page (int | Unset): Page number; meta.last_page says where the list ends.
        medium (str | Unset): Comma-separated series mediums to filter by (comic, manga, manhwa,
            manhua, bande_dessinee, magazine).
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCharacterIssuesResponse200 | GetCharacterIssuesResponse403 | GetCharacterIssuesResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        character_id=character_id,
        client=client,
        q=q,
        limit=limit,
        page=page,
        medium=medium,
        languages=languages,
    ).parsed


async def asyncio_detailed(
    character_id: int,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    medium: str | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> Response[
    GetCharacterIssuesResponse200
    | GetCharacterIssuesResponse403
    | GetCharacterIssuesResponse404
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Get character issues.

     Returns paginated issues where the character appears, ordered by release date.

    Args:
        character_id (int): The character ID.
        q (str | Unset): Optional case-insensitive search within these results.
        limit (int | Unset): Results per page (max 50).
        page (int | Unset): Page number; meta.last_page says where the list ends.
        medium (str | Unset): Comma-separated series mediums to filter by (comic, manga, manhwa,
            manhua, bande_dessinee, magazine).
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCharacterIssuesResponse200 | GetCharacterIssuesResponse403 | GetCharacterIssuesResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        character_id=character_id,
        q=q,
        limit=limit,
        page=page,
        medium=medium,
        languages=languages,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    character_id: int,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    medium: str | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> (
    GetCharacterIssuesResponse200
    | GetCharacterIssuesResponse403
    | GetCharacterIssuesResponse404
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Get character issues.

     Returns paginated issues where the character appears, ordered by release date.

    Args:
        character_id (int): The character ID.
        q (str | Unset): Optional case-insensitive search within these results.
        limit (int | Unset): Results per page (max 50).
        page (int | Unset): Page number; meta.last_page says where the list ends.
        medium (str | Unset): Comma-separated series mediums to filter by (comic, manga, manhwa,
            manhua, bande_dessinee, magazine).
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCharacterIssuesResponse200 | GetCharacterIssuesResponse403 | GetCharacterIssuesResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            character_id=character_id,
            client=client,
            q=q,
            limit=limit,
            page=page,
            medium=medium,
            languages=languages,
        )
    ).parsed
