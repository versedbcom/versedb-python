from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_events_response_200 import ListEventsResponse200
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    upcoming: bool | Unset = UNSET,
    past: bool | Unset = UNSET,
    is_online: bool | Unset = UNSET,
    is_fcbd: bool | Unset = UNSET,
    country_code: str | Unset = UNSET,
    region: str | Unset = UNSET,
    weekend: bool | Unset = UNSET,
    month: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["type"] = type_

    params["upcoming"] = upcoming

    params["past"] = past

    params["is_online"] = is_online

    params["is_fcbd"] = is_fcbd

    params["country_code"] = country_code

    params["region"] = region

    params["weekend"] = weekend

    params["month"] = month

    params["sort"] = sort

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListEventsResponse200 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = ListEventsResponse200.from_dict(response.json())

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
) -> Response[ListEventsResponse200 | TooManyRequestsError | UnauthorizedError]:
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
    type_: str | Unset = UNSET,
    upcoming: bool | Unset = UNSET,
    past: bool | Unset = UNSET,
    is_online: bool | Unset = UNSET,
    is_fcbd: bool | Unset = UNSET,
    country_code: str | Unset = UNSET,
    region: str | Unset = UNSET,
    weekend: bool | Unset = UNSET,
    month: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ListEventsResponse200 | TooManyRequestsError | UnauthorizedError]:
    """List events.

     Returns: id, slug, name, type, dates, location info, logo_url

    Args:
        q (str | Unset): Search by event name, city or venue, tolerating small typos for upcoming
            events. Results are ordered by relevance unless `sort` is set.
        type_ (str | Unset): Filter by type (convention, store_event, signing, etc).
        upcoming (bool | Unset): Only show upcoming events.
        past (bool | Unset): Only show past events.
        is_online (bool | Unset): Filter online/in-person events.
        is_fcbd (bool | Unset): Filter Free Comic Book Day events.
        country_code (str | Unset): Filter by country code.
        region (str | Unset): Filter by region, matched exactly against the stored value. Use the
            values from /events/regions.
        weekend (bool | Unset): Only events running this Friday to Sunday.
        month (str | Unset): Only events starting in this month, as YYYY-MM.
        sort (str | Unset): One of date_asc, date_desc, name_asc, name_desc. Defaults to date_desc
            with `past`, date_asc otherwise; a `q` search without `sort` keeps relevance order.
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListEventsResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        q=q,
        type_=type_,
        upcoming=upcoming,
        past=past,
        is_online=is_online,
        is_fcbd=is_fcbd,
        country_code=country_code,
        region=region,
        weekend=weekend,
        month=month,
        sort=sort,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    upcoming: bool | Unset = UNSET,
    past: bool | Unset = UNSET,
    is_online: bool | Unset = UNSET,
    is_fcbd: bool | Unset = UNSET,
    country_code: str | Unset = UNSET,
    region: str | Unset = UNSET,
    weekend: bool | Unset = UNSET,
    month: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ListEventsResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """List events.

     Returns: id, slug, name, type, dates, location info, logo_url

    Args:
        q (str | Unset): Search by event name, city or venue, tolerating small typos for upcoming
            events. Results are ordered by relevance unless `sort` is set.
        type_ (str | Unset): Filter by type (convention, store_event, signing, etc).
        upcoming (bool | Unset): Only show upcoming events.
        past (bool | Unset): Only show past events.
        is_online (bool | Unset): Filter online/in-person events.
        is_fcbd (bool | Unset): Filter Free Comic Book Day events.
        country_code (str | Unset): Filter by country code.
        region (str | Unset): Filter by region, matched exactly against the stored value. Use the
            values from /events/regions.
        weekend (bool | Unset): Only events running this Friday to Sunday.
        month (str | Unset): Only events starting in this month, as YYYY-MM.
        sort (str | Unset): One of date_asc, date_desc, name_asc, name_desc. Defaults to date_desc
            with `past`, date_asc otherwise; a `q` search without `sort` keeps relevance order.
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListEventsResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        client=client,
        q=q,
        type_=type_,
        upcoming=upcoming,
        past=past,
        is_online=is_online,
        is_fcbd=is_fcbd,
        country_code=country_code,
        region=region,
        weekend=weekend,
        month=month,
        sort=sort,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    upcoming: bool | Unset = UNSET,
    past: bool | Unset = UNSET,
    is_online: bool | Unset = UNSET,
    is_fcbd: bool | Unset = UNSET,
    country_code: str | Unset = UNSET,
    region: str | Unset = UNSET,
    weekend: bool | Unset = UNSET,
    month: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ListEventsResponse200 | TooManyRequestsError | UnauthorizedError]:
    """List events.

     Returns: id, slug, name, type, dates, location info, logo_url

    Args:
        q (str | Unset): Search by event name, city or venue, tolerating small typos for upcoming
            events. Results are ordered by relevance unless `sort` is set.
        type_ (str | Unset): Filter by type (convention, store_event, signing, etc).
        upcoming (bool | Unset): Only show upcoming events.
        past (bool | Unset): Only show past events.
        is_online (bool | Unset): Filter online/in-person events.
        is_fcbd (bool | Unset): Filter Free Comic Book Day events.
        country_code (str | Unset): Filter by country code.
        region (str | Unset): Filter by region, matched exactly against the stored value. Use the
            values from /events/regions.
        weekend (bool | Unset): Only events running this Friday to Sunday.
        month (str | Unset): Only events starting in this month, as YYYY-MM.
        sort (str | Unset): One of date_asc, date_desc, name_asc, name_desc. Defaults to date_desc
            with `past`, date_asc otherwise; a `q` search without `sort` keeps relevance order.
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListEventsResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        q=q,
        type_=type_,
        upcoming=upcoming,
        past=past,
        is_online=is_online,
        is_fcbd=is_fcbd,
        country_code=country_code,
        region=region,
        weekend=weekend,
        month=month,
        sort=sort,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    upcoming: bool | Unset = UNSET,
    past: bool | Unset = UNSET,
    is_online: bool | Unset = UNSET,
    is_fcbd: bool | Unset = UNSET,
    country_code: str | Unset = UNSET,
    region: str | Unset = UNSET,
    weekend: bool | Unset = UNSET,
    month: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ListEventsResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """List events.

     Returns: id, slug, name, type, dates, location info, logo_url

    Args:
        q (str | Unset): Search by event name, city or venue, tolerating small typos for upcoming
            events. Results are ordered by relevance unless `sort` is set.
        type_ (str | Unset): Filter by type (convention, store_event, signing, etc).
        upcoming (bool | Unset): Only show upcoming events.
        past (bool | Unset): Only show past events.
        is_online (bool | Unset): Filter online/in-person events.
        is_fcbd (bool | Unset): Filter Free Comic Book Day events.
        country_code (str | Unset): Filter by country code.
        region (str | Unset): Filter by region, matched exactly against the stored value. Use the
            values from /events/regions.
        weekend (bool | Unset): Only events running this Friday to Sunday.
        month (str | Unset): Only events starting in this month, as YYYY-MM.
        sort (str | Unset): One of date_asc, date_desc, name_asc, name_desc. Defaults to date_desc
            with `past`, date_asc otherwise; a `q` search without `sort` keeps relevance order.
        limit (int | Unset): Number of results per page (max 50).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListEventsResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            type_=type_,
            upcoming=upcoming,
            past=past,
            is_online=is_online,
            is_fcbd=is_fcbd,
            country_code=country_code,
            region=region,
            weekend=weekend,
            month=month,
            sort=sort,
            limit=limit,
        )
    ).parsed
