from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_creator_details_response_200 import GetCreatorDetailsResponse200
from ...models.get_creator_details_response_403 import GetCreatorDetailsResponse403
from ...models.get_creator_details_response_404 import GetCreatorDetailsResponse404
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    creator_id: int,
    *,
    languages: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["languages"] = languages

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/creators/{creator_id}".format(
            creator_id=quote(str(creator_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetCreatorDetailsResponse200
    | GetCreatorDetailsResponse403
    | GetCreatorDetailsResponse404
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    if response.status_code == 200:
        response_200 = GetCreatorDetailsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetCreatorDetailsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetCreatorDetailsResponse404.from_dict(response.json())

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
    GetCreatorDetailsResponse200
    | GetCreatorDetailsResponse403
    | GetCreatorDetailsResponse404
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
    creator_id: int,
    *,
    client: AuthenticatedClient | Client,
    languages: str | Unset = UNSET,
) -> Response[
    GetCreatorDetailsResponse200
    | GetCreatorDetailsResponse403
    | GetCreatorDetailsResponse404
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Get creator details.

     Returns a single creator with full details including role and awards.

    Args:
        creator_id (int): The creator ID.
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCreatorDetailsResponse200 | GetCreatorDetailsResponse403 | GetCreatorDetailsResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        creator_id=creator_id,
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
    languages: str | Unset = UNSET,
) -> (
    GetCreatorDetailsResponse200
    | GetCreatorDetailsResponse403
    | GetCreatorDetailsResponse404
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Get creator details.

     Returns a single creator with full details including role and awards.

    Args:
        creator_id (int): The creator ID.
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCreatorDetailsResponse200 | GetCreatorDetailsResponse403 | GetCreatorDetailsResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        creator_id=creator_id,
        client=client,
        languages=languages,
    ).parsed


async def asyncio_detailed(
    creator_id: int,
    *,
    client: AuthenticatedClient | Client,
    languages: str | Unset = UNSET,
) -> Response[
    GetCreatorDetailsResponse200
    | GetCreatorDetailsResponse403
    | GetCreatorDetailsResponse404
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Get creator details.

     Returns a single creator with full details including role and awards.

    Args:
        creator_id (int): The creator ID.
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCreatorDetailsResponse200 | GetCreatorDetailsResponse403 | GetCreatorDetailsResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        creator_id=creator_id,
        languages=languages,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    creator_id: int,
    *,
    client: AuthenticatedClient | Client,
    languages: str | Unset = UNSET,
) -> (
    GetCreatorDetailsResponse200
    | GetCreatorDetailsResponse403
    | GetCreatorDetailsResponse404
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Get creator details.

     Returns a single creator with full details including role and awards.

    Args:
        creator_id (int): The creator ID.
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCreatorDetailsResponse200 | GetCreatorDetailsResponse403 | GetCreatorDetailsResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            creator_id=creator_id,
            client=client,
            languages=languages,
        )
    ).parsed
