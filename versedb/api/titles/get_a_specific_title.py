from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_a_specific_title_response_200 import GetASpecificTitleResponse200
from ...models.get_a_specific_title_response_404 import GetASpecificTitleResponse404
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import Response


def _get_kwargs(
    title_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/titles/{title_id}".format(
            title_id=quote(str(title_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetASpecificTitleResponse200 | GetASpecificTitleResponse404 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = GetASpecificTitleResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetASpecificTitleResponse404.from_dict(response.json())

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
) -> Response[GetASpecificTitleResponse200 | GetASpecificTitleResponse404 | TooManyRequestsError | UnauthorizedError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    title_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetASpecificTitleResponse200 | GetASpecificTitleResponse404 | TooManyRequestsError | UnauthorizedError]:
    """Get a specific title

     Returns: id, name, slug, start_year, end_year, status, type,
    image_url, content_rating_label, min_age, is_nsfw, imprint_id, series_count,
    issues_count, average_rating, total_reviews, aliases

    Use relationship endpoints for richer data:
    - /titles/{id}/series - Get series in a title
    - /titles/{id}/issues - Get issues across all series in a title
    - /titles/{id}/creators - Get creators credited on the title
    - /titles/{id}/characters - Get characters associated with the title
    - /titles/{id}/teams - Get teams associated with the title

    Args:
        title_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetASpecificTitleResponse200 | GetASpecificTitleResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        title_id=title_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    title_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetASpecificTitleResponse200 | GetASpecificTitleResponse404 | TooManyRequestsError | UnauthorizedError | None:
    """Get a specific title

     Returns: id, name, slug, start_year, end_year, status, type,
    image_url, content_rating_label, min_age, is_nsfw, imprint_id, series_count,
    issues_count, average_rating, total_reviews, aliases

    Use relationship endpoints for richer data:
    - /titles/{id}/series - Get series in a title
    - /titles/{id}/issues - Get issues across all series in a title
    - /titles/{id}/creators - Get creators credited on the title
    - /titles/{id}/characters - Get characters associated with the title
    - /titles/{id}/teams - Get teams associated with the title

    Args:
        title_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetASpecificTitleResponse200 | GetASpecificTitleResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        title_id=title_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    title_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetASpecificTitleResponse200 | GetASpecificTitleResponse404 | TooManyRequestsError | UnauthorizedError]:
    """Get a specific title

     Returns: id, name, slug, start_year, end_year, status, type,
    image_url, content_rating_label, min_age, is_nsfw, imprint_id, series_count,
    issues_count, average_rating, total_reviews, aliases

    Use relationship endpoints for richer data:
    - /titles/{id}/series - Get series in a title
    - /titles/{id}/issues - Get issues across all series in a title
    - /titles/{id}/creators - Get creators credited on the title
    - /titles/{id}/characters - Get characters associated with the title
    - /titles/{id}/teams - Get teams associated with the title

    Args:
        title_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetASpecificTitleResponse200 | GetASpecificTitleResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        title_id=title_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    title_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetASpecificTitleResponse200 | GetASpecificTitleResponse404 | TooManyRequestsError | UnauthorizedError | None:
    """Get a specific title

     Returns: id, name, slug, start_year, end_year, status, type,
    image_url, content_rating_label, min_age, is_nsfw, imprint_id, series_count,
    issues_count, average_rating, total_reviews, aliases

    Use relationship endpoints for richer data:
    - /titles/{id}/series - Get series in a title
    - /titles/{id}/issues - Get issues across all series in a title
    - /titles/{id}/creators - Get creators credited on the title
    - /titles/{id}/characters - Get characters associated with the title
    - /titles/{id}/teams - Get teams associated with the title

    Args:
        title_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetASpecificTitleResponse200 | GetASpecificTitleResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            title_id=title_id,
            client=client,
        )
    ).parsed
