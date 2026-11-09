from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_creators_response_200 import ListCreatorsResponse200
from ...models.list_creators_response_403 import ListCreatorsResponse403
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    role_ids: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["role_ids"] = role_ids

    params["sort"] = sort

    params["limit"] = limit

    params["page"] = page

    params["languages"] = languages

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/creators",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListCreatorsResponse200 | ListCreatorsResponse403 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = ListCreatorsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ListCreatorsResponse403.from_dict(response.json())

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
) -> Response[ListCreatorsResponse200 | ListCreatorsResponse403 | TooManyRequestsError | UnauthorizedError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    role_ids: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> Response[ListCreatorsResponse200 | ListCreatorsResponse403 | TooManyRequestsError | UnauthorizedError]:
    """List creators.

     Returns paginated creators by name, with optional search and a role filter.

    Args:
        q (str | Unset): Search by creator name.
        role_ids (str | Unset): Comma-separated creator role IDs. Returns creators with any of
            them as a primary role or on a credit.
        sort (str | Unset): Pass any value to replace the relevance ordering applied to q results
            with the name.
        limit (int | Unset): Results per page (max 50).
        page (int | Unset): Page number; meta.last_page says where the list ends.
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCreatorsResponse200 | ListCreatorsResponse403 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        q=q,
        role_ids=role_ids,
        sort=sort,
        limit=limit,
        page=page,
        languages=languages,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    role_ids: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> ListCreatorsResponse200 | ListCreatorsResponse403 | TooManyRequestsError | UnauthorizedError | None:
    """List creators.

     Returns paginated creators by name, with optional search and a role filter.

    Args:
        q (str | Unset): Search by creator name.
        role_ids (str | Unset): Comma-separated creator role IDs. Returns creators with any of
            them as a primary role or on a credit.
        sort (str | Unset): Pass any value to replace the relevance ordering applied to q results
            with the name.
        limit (int | Unset): Results per page (max 50).
        page (int | Unset): Page number; meta.last_page says where the list ends.
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCreatorsResponse200 | ListCreatorsResponse403 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        client=client,
        q=q,
        role_ids=role_ids,
        sort=sort,
        limit=limit,
        page=page,
        languages=languages,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    role_ids: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> Response[ListCreatorsResponse200 | ListCreatorsResponse403 | TooManyRequestsError | UnauthorizedError]:
    """List creators.

     Returns paginated creators by name, with optional search and a role filter.

    Args:
        q (str | Unset): Search by creator name.
        role_ids (str | Unset): Comma-separated creator role IDs. Returns creators with any of
            them as a primary role or on a credit.
        sort (str | Unset): Pass any value to replace the relevance ordering applied to q results
            with the name.
        limit (int | Unset): Results per page (max 50).
        page (int | Unset): Page number; meta.last_page says where the list ends.
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCreatorsResponse200 | ListCreatorsResponse403 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        q=q,
        role_ids=role_ids,
        sort=sort,
        limit=limit,
        page=page,
        languages=languages,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    role_ids: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> ListCreatorsResponse200 | ListCreatorsResponse403 | TooManyRequestsError | UnauthorizedError | None:
    """List creators.

     Returns paginated creators by name, with optional search and a role filter.

    Args:
        q (str | Unset): Search by creator name.
        role_ids (str | Unset): Comma-separated creator role IDs. Returns creators with any of
            them as a primary role or on a credit.
        sort (str | Unset): Pass any value to replace the relevance ordering applied to q results
            with the name.
        limit (int | Unset): Results per page (max 50).
        page (int | Unset): Page number; meta.last_page says where the list ends.
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCreatorsResponse200 | ListCreatorsResponse403 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            role_ids=role_ids,
            sort=sort,
            limit=limit,
            page=page,
            languages=languages,
        )
    ).parsed
