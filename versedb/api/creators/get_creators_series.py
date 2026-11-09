from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_creators_series_response_200 import GetCreatorsSeriesResponse200
from ...models.get_creators_series_response_403 import GetCreatorsSeriesResponse403
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    creator_id: int,
    *,
    limit: int | Unset = UNSET,
    q: str | Unset = UNSET,
    medium: str | Unset = UNSET,
    page: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["q"] = q

    params["medium"] = medium

    params["page"] = page

    params["languages"] = languages

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/creators/{creator_id}/series".format(
            creator_id=quote(str(creator_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCreatorsSeriesResponse200 | GetCreatorsSeriesResponse403 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = GetCreatorsSeriesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetCreatorsSeriesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 429:
        response_429 = TooManyRequestsError.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCreatorsSeriesResponse200 | GetCreatorsSeriesResponse403 | TooManyRequestsError | UnauthorizedError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    creator_id: int,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    q: str | Unset = UNSET,
    medium: str | Unset = UNSET,
    page: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> Response[GetCreatorsSeriesResponse200 | GetCreatorsSeriesResponse403 | TooManyRequestsError | UnauthorizedError]:
    """Get creator's series.

     Returns paginated series where the creator has worked. `creator_issues_count` is how many
    of the series' issues credit this creator; `cached_issues_count` is the whole series.
    A series credited to the creator without any issue credits reports 0.

    Args:
        creator_id (int): The creator ID.
        limit (int | Unset): Results per page (max 50).
        q (str | Unset): Optional case-insensitive search within these results.
        medium (str | Unset): Comma-separated series mediums to filter by (comic, manga, manhwa,
            manhua, bande_dessinee, magazine).
        page (int | Unset): Page number; meta.last_page says where the list ends.
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCreatorsSeriesResponse200 | GetCreatorsSeriesResponse403 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        creator_id=creator_id,
        limit=limit,
        q=q,
        medium=medium,
        page=page,
        languages=languages,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    creator_id: int,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    q: str | Unset = UNSET,
    medium: str | Unset = UNSET,
    page: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> GetCreatorsSeriesResponse200 | GetCreatorsSeriesResponse403 | TooManyRequestsError | UnauthorizedError | None:
    """Get creator's series.

     Returns paginated series where the creator has worked. `creator_issues_count` is how many
    of the series' issues credit this creator; `cached_issues_count` is the whole series.
    A series credited to the creator without any issue credits reports 0.

    Args:
        creator_id (int): The creator ID.
        limit (int | Unset): Results per page (max 50).
        q (str | Unset): Optional case-insensitive search within these results.
        medium (str | Unset): Comma-separated series mediums to filter by (comic, manga, manhwa,
            manhua, bande_dessinee, magazine).
        page (int | Unset): Page number; meta.last_page says where the list ends.
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCreatorsSeriesResponse200 | GetCreatorsSeriesResponse403 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        creator_id=creator_id,
        client=client,
        limit=limit,
        q=q,
        medium=medium,
        page=page,
        languages=languages,
    ).parsed


async def asyncio_detailed(
    creator_id: int,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    q: str | Unset = UNSET,
    medium: str | Unset = UNSET,
    page: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> Response[GetCreatorsSeriesResponse200 | GetCreatorsSeriesResponse403 | TooManyRequestsError | UnauthorizedError]:
    """Get creator's series.

     Returns paginated series where the creator has worked. `creator_issues_count` is how many
    of the series' issues credit this creator; `cached_issues_count` is the whole series.
    A series credited to the creator without any issue credits reports 0.

    Args:
        creator_id (int): The creator ID.
        limit (int | Unset): Results per page (max 50).
        q (str | Unset): Optional case-insensitive search within these results.
        medium (str | Unset): Comma-separated series mediums to filter by (comic, manga, manhwa,
            manhua, bande_dessinee, magazine).
        page (int | Unset): Page number; meta.last_page says where the list ends.
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCreatorsSeriesResponse200 | GetCreatorsSeriesResponse403 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        creator_id=creator_id,
        limit=limit,
        q=q,
        medium=medium,
        page=page,
        languages=languages,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    creator_id: int,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    q: str | Unset = UNSET,
    medium: str | Unset = UNSET,
    page: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> GetCreatorsSeriesResponse200 | GetCreatorsSeriesResponse403 | TooManyRequestsError | UnauthorizedError | None:
    """Get creator's series.

     Returns paginated series where the creator has worked. `creator_issues_count` is how many
    of the series' issues credit this creator; `cached_issues_count` is the whole series.
    A series credited to the creator without any issue credits reports 0.

    Args:
        creator_id (int): The creator ID.
        limit (int | Unset): Results per page (max 50).
        q (str | Unset): Optional case-insensitive search within these results.
        medium (str | Unset): Comma-separated series mediums to filter by (comic, manga, manhwa,
            manhua, bande_dessinee, magazine).
        page (int | Unset): Page number; meta.last_page says where the list ends.
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCreatorsSeriesResponse200 | GetCreatorsSeriesResponse403 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            creator_id=creator_id,
            client=client,
            limit=limit,
            q=q,
            medium=medium,
            page=page,
            languages=languages,
        )
    ).parsed
