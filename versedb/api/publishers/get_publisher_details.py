from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_publisher_details_response_200 import GetPublisherDetailsResponse200
from ...models.get_publisher_details_response_404 import GetPublisherDetailsResponse404
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import Response


def _get_kwargs(
    publisher_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/publishers/{publisher_id}".format(
            publisher_id=quote(str(publisher_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetPublisherDetailsResponse200 | GetPublisherDetailsResponse404 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = GetPublisherDetailsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetPublisherDetailsResponse404.from_dict(response.json())

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
    GetPublisherDetailsResponse200 | GetPublisherDetailsResponse404 | TooManyRequestsError | UnauthorizedError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    publisher_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetPublisherDetailsResponse200 | GetPublisherDetailsResponse404 | TooManyRequestsError | UnauthorizedError
]:
    """Get publisher details

     Returns: id, name, founded_year, first_published_year,
    website, headquarters, parent_company, status, logo_url, aliases

    Use the related endpoints for relationship data:
    - /series?publisher_id={id} - Get series by publisher
    - /publishers/{id}/characters - Get characters by publisher

    Args:
        publisher_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPublisherDetailsResponse200 | GetPublisherDetailsResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        publisher_id=publisher_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    publisher_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetPublisherDetailsResponse200 | GetPublisherDetailsResponse404 | TooManyRequestsError | UnauthorizedError | None:
    """Get publisher details

     Returns: id, name, founded_year, first_published_year,
    website, headquarters, parent_company, status, logo_url, aliases

    Use the related endpoints for relationship data:
    - /series?publisher_id={id} - Get series by publisher
    - /publishers/{id}/characters - Get characters by publisher

    Args:
        publisher_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPublisherDetailsResponse200 | GetPublisherDetailsResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        publisher_id=publisher_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    publisher_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetPublisherDetailsResponse200 | GetPublisherDetailsResponse404 | TooManyRequestsError | UnauthorizedError
]:
    """Get publisher details

     Returns: id, name, founded_year, first_published_year,
    website, headquarters, parent_company, status, logo_url, aliases

    Use the related endpoints for relationship data:
    - /series?publisher_id={id} - Get series by publisher
    - /publishers/{id}/characters - Get characters by publisher

    Args:
        publisher_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPublisherDetailsResponse200 | GetPublisherDetailsResponse404 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        publisher_id=publisher_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    publisher_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetPublisherDetailsResponse200 | GetPublisherDetailsResponse404 | TooManyRequestsError | UnauthorizedError | None:
    """Get publisher details

     Returns: id, name, founded_year, first_published_year,
    website, headquarters, parent_company, status, logo_url, aliases

    Use the related endpoints for relationship data:
    - /series?publisher_id={id} - Get series by publisher
    - /publishers/{id}/characters - Get characters by publisher

    Args:
        publisher_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPublisherDetailsResponse200 | GetPublisherDetailsResponse404 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            publisher_id=publisher_id,
            client=client,
        )
    ).parsed
