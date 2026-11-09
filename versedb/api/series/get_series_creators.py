from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_series_creators_response_200 import GetSeriesCreatorsResponse200
from ...models.get_series_creators_response_403 import GetSeriesCreatorsResponse403
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    page: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["languages"] = languages

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/series/{id}/creators".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetSeriesCreatorsResponse200 | GetSeriesCreatorsResponse403 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = GetSeriesCreatorsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetSeriesCreatorsResponse403.from_dict(response.json())

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
) -> Response[GetSeriesCreatorsResponse200 | GetSeriesCreatorsResponse403 | TooManyRequestsError | UnauthorizedError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> Response[GetSeriesCreatorsResponse200 | GetSeriesCreatorsResponse403 | TooManyRequestsError | UnauthorizedError]:
    """Get series creators.

     Returns paginated creators associated with a specific series.

    Args:
        id (int): The series ID.
        page (int | Unset): Page number; meta.last_page says where the list ends.
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSeriesCreatorsResponse200 | GetSeriesCreatorsResponse403 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        id=id,
        page=page,
        languages=languages,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> GetSeriesCreatorsResponse200 | GetSeriesCreatorsResponse403 | TooManyRequestsError | UnauthorizedError | None:
    """Get series creators.

     Returns paginated creators associated with a specific series.

    Args:
        id (int): The series ID.
        page (int | Unset): Page number; meta.last_page says where the list ends.
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSeriesCreatorsResponse200 | GetSeriesCreatorsResponse403 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        id=id,
        client=client,
        page=page,
        languages=languages,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> Response[GetSeriesCreatorsResponse200 | GetSeriesCreatorsResponse403 | TooManyRequestsError | UnauthorizedError]:
    """Get series creators.

     Returns paginated creators associated with a specific series.

    Args:
        id (int): The series ID.
        page (int | Unset): Page number; meta.last_page says where the list ends.
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSeriesCreatorsResponse200 | GetSeriesCreatorsResponse403 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        id=id,
        page=page,
        languages=languages,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    languages: str | Unset = UNSET,
) -> GetSeriesCreatorsResponse200 | GetSeriesCreatorsResponse403 | TooManyRequestsError | UnauthorizedError | None:
    """Get series creators.

     Returns paginated creators associated with a specific series.

    Args:
        id (int): The series ID.
        page (int | Unset): Page number; meta.last_page says where the list ends.
        languages (str | Unset): Keep only these languages in the `_i18n` maps (comma-separated
            BCP 47 tags). No other field changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSeriesCreatorsResponse200 | GetSeriesCreatorsResponse403 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            page=page,
            languages=languages,
        )
    ).parsed
