from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_collection_response_200 import ListCollectionResponse200
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    search: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    graded: bool | Unset = UNSET,
    is_signed: bool | Unset = UNSET,
    condition: str | Unset = UNSET,
    status: str | Unset = UNSET,
    for_sale: bool | Unset = UNSET,
    for_trade: bool | Unset = UNSET,
    read_status: str | Unset = UNSET,
    publisher_id: int | Unset = UNSET,
    series_id: int | Unset = UNSET,
    grade_min: float | Unset = UNSET,
    grade_max: float | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["page"] = page

    params["search"] = search

    params["format"] = format_

    params["graded"] = graded

    params["is_signed"] = is_signed

    params["condition"] = condition

    params["status"] = status

    params["for_sale"] = for_sale

    params["for_trade"] = for_trade

    params["read_status"] = read_status

    params["publisher_id"] = publisher_id

    params["series_id"] = series_id

    params["grade_min"] = grade_min

    params["grade_max"] = grade_max

    params["sort_by"] = sort_by

    params["sort_order"] = sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/user/collections",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListCollectionResponse200 | TooManyRequestsError | UnauthorizedError | None:
    if response.status_code == 200:
        response_200 = ListCollectionResponse200.from_dict(response.json())

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
) -> Response[ListCollectionResponse200 | TooManyRequestsError | UnauthorizedError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    search: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    graded: bool | Unset = UNSET,
    is_signed: bool | Unset = UNSET,
    condition: str | Unset = UNSET,
    status: str | Unset = UNSET,
    for_sale: bool | Unset = UNSET,
    for_trade: bool | Unset = UNSET,
    read_status: str | Unset = UNSET,
    publisher_id: int | Unset = UNSET,
    series_id: int | Unset = UNSET,
    grade_min: float | Unset = UNSET,
    grade_max: float | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
) -> Response[ListCollectionResponse200 | TooManyRequestsError | UnauthorizedError]:
    """List collection.

     Returns all issues in the user's collection with series and publisher info.

    Needs `read:user` or `read:showcase`. A `read:showcase` token gets each copy without
    `price_paid`, `estimated_value`, `value_last_updated`, `price_sold`, `sold_at`,
    `purchased_at`, `purchase_source`, `purchase_store`, `acquisition_method`,
    `comic_shop_id`, `comic_shop`, `notes`, `grader_notes`, `storage_location`,
    `custom_label`, `bagged_at`, `personal_rating`, `tags` or `loan`, leaves out copies
    marked not public, and the `estimated_value` and `price_paid` sorts fall back to `date_added`.

    Args:
        per_page (int | Unset): Items per page (max 100).
        page (int | Unset): Page number.
        search (str | Unset): Filter by issue name, issue number, or series name.
        format_ (str | Unset): Filter by stored format.
        graded (bool | Unset): Filter to graded (true) or raw (false) copies.
        is_signed (bool | Unset): Filter to signed (true) or unsigned (false) copies. PRO; ignored
            for other members.
        condition (str | Unset): Filter by condition grade code.
        status (str | Unset): Which copies to return: owned, for_sale, sold, or all. Sold copies
            are excluded by default.
        for_sale (bool | Unset): Filter to copies marked for sale.
        for_trade (bool | Unset): Filter to copies marked for trade.
        read_status (str | Unset): Filter by read state. One of: read, unread.
        publisher_id (int | Unset): Filter to issues from a publisher.
        series_id (int | Unset): Filter to copies of issues in a series.
        grade_min (float | Unset): Filter to copies with a numeric grade at or above this value.
            PRO; ignored for other members.
        grade_max (float | Unset): Filter to copies with a numeric grade at or below this value.
            PRO; ignored for other members.
        sort_by (str | Unset): Sort field. One of: date_added, title, release_date,
            estimated_value, price_paid.
        sort_order (str | Unset): Sort direction. One of: asc, desc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCollectionResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        page=page,
        search=search,
        format_=format_,
        graded=graded,
        is_signed=is_signed,
        condition=condition,
        status=status,
        for_sale=for_sale,
        for_trade=for_trade,
        read_status=read_status,
        publisher_id=publisher_id,
        series_id=series_id,
        grade_min=grade_min,
        grade_max=grade_max,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    search: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    graded: bool | Unset = UNSET,
    is_signed: bool | Unset = UNSET,
    condition: str | Unset = UNSET,
    status: str | Unset = UNSET,
    for_sale: bool | Unset = UNSET,
    for_trade: bool | Unset = UNSET,
    read_status: str | Unset = UNSET,
    publisher_id: int | Unset = UNSET,
    series_id: int | Unset = UNSET,
    grade_min: float | Unset = UNSET,
    grade_max: float | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
) -> ListCollectionResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """List collection.

     Returns all issues in the user's collection with series and publisher info.

    Needs `read:user` or `read:showcase`. A `read:showcase` token gets each copy without
    `price_paid`, `estimated_value`, `value_last_updated`, `price_sold`, `sold_at`,
    `purchased_at`, `purchase_source`, `purchase_store`, `acquisition_method`,
    `comic_shop_id`, `comic_shop`, `notes`, `grader_notes`, `storage_location`,
    `custom_label`, `bagged_at`, `personal_rating`, `tags` or `loan`, leaves out copies
    marked not public, and the `estimated_value` and `price_paid` sorts fall back to `date_added`.

    Args:
        per_page (int | Unset): Items per page (max 100).
        page (int | Unset): Page number.
        search (str | Unset): Filter by issue name, issue number, or series name.
        format_ (str | Unset): Filter by stored format.
        graded (bool | Unset): Filter to graded (true) or raw (false) copies.
        is_signed (bool | Unset): Filter to signed (true) or unsigned (false) copies. PRO; ignored
            for other members.
        condition (str | Unset): Filter by condition grade code.
        status (str | Unset): Which copies to return: owned, for_sale, sold, or all. Sold copies
            are excluded by default.
        for_sale (bool | Unset): Filter to copies marked for sale.
        for_trade (bool | Unset): Filter to copies marked for trade.
        read_status (str | Unset): Filter by read state. One of: read, unread.
        publisher_id (int | Unset): Filter to issues from a publisher.
        series_id (int | Unset): Filter to copies of issues in a series.
        grade_min (float | Unset): Filter to copies with a numeric grade at or above this value.
            PRO; ignored for other members.
        grade_max (float | Unset): Filter to copies with a numeric grade at or below this value.
            PRO; ignored for other members.
        sort_by (str | Unset): Sort field. One of: date_added, title, release_date,
            estimated_value, price_paid.
        sort_order (str | Unset): Sort direction. One of: asc, desc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCollectionResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        client=client,
        per_page=per_page,
        page=page,
        search=search,
        format_=format_,
        graded=graded,
        is_signed=is_signed,
        condition=condition,
        status=status,
        for_sale=for_sale,
        for_trade=for_trade,
        read_status=read_status,
        publisher_id=publisher_id,
        series_id=series_id,
        grade_min=grade_min,
        grade_max=grade_max,
        sort_by=sort_by,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    search: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    graded: bool | Unset = UNSET,
    is_signed: bool | Unset = UNSET,
    condition: str | Unset = UNSET,
    status: str | Unset = UNSET,
    for_sale: bool | Unset = UNSET,
    for_trade: bool | Unset = UNSET,
    read_status: str | Unset = UNSET,
    publisher_id: int | Unset = UNSET,
    series_id: int | Unset = UNSET,
    grade_min: float | Unset = UNSET,
    grade_max: float | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
) -> Response[ListCollectionResponse200 | TooManyRequestsError | UnauthorizedError]:
    """List collection.

     Returns all issues in the user's collection with series and publisher info.

    Needs `read:user` or `read:showcase`. A `read:showcase` token gets each copy without
    `price_paid`, `estimated_value`, `value_last_updated`, `price_sold`, `sold_at`,
    `purchased_at`, `purchase_source`, `purchase_store`, `acquisition_method`,
    `comic_shop_id`, `comic_shop`, `notes`, `grader_notes`, `storage_location`,
    `custom_label`, `bagged_at`, `personal_rating`, `tags` or `loan`, leaves out copies
    marked not public, and the `estimated_value` and `price_paid` sorts fall back to `date_added`.

    Args:
        per_page (int | Unset): Items per page (max 100).
        page (int | Unset): Page number.
        search (str | Unset): Filter by issue name, issue number, or series name.
        format_ (str | Unset): Filter by stored format.
        graded (bool | Unset): Filter to graded (true) or raw (false) copies.
        is_signed (bool | Unset): Filter to signed (true) or unsigned (false) copies. PRO; ignored
            for other members.
        condition (str | Unset): Filter by condition grade code.
        status (str | Unset): Which copies to return: owned, for_sale, sold, or all. Sold copies
            are excluded by default.
        for_sale (bool | Unset): Filter to copies marked for sale.
        for_trade (bool | Unset): Filter to copies marked for trade.
        read_status (str | Unset): Filter by read state. One of: read, unread.
        publisher_id (int | Unset): Filter to issues from a publisher.
        series_id (int | Unset): Filter to copies of issues in a series.
        grade_min (float | Unset): Filter to copies with a numeric grade at or above this value.
            PRO; ignored for other members.
        grade_max (float | Unset): Filter to copies with a numeric grade at or below this value.
            PRO; ignored for other members.
        sort_by (str | Unset): Sort field. One of: date_added, title, release_date,
            estimated_value, price_paid.
        sort_order (str | Unset): Sort direction. One of: asc, desc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCollectionResponse200 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        page=page,
        search=search,
        format_=format_,
        graded=graded,
        is_signed=is_signed,
        condition=condition,
        status=status,
        for_sale=for_sale,
        for_trade=for_trade,
        read_status=read_status,
        publisher_id=publisher_id,
        series_id=series_id,
        grade_min=grade_min,
        grade_max=grade_max,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    search: str | Unset = UNSET,
    format_: str | Unset = UNSET,
    graded: bool | Unset = UNSET,
    is_signed: bool | Unset = UNSET,
    condition: str | Unset = UNSET,
    status: str | Unset = UNSET,
    for_sale: bool | Unset = UNSET,
    for_trade: bool | Unset = UNSET,
    read_status: str | Unset = UNSET,
    publisher_id: int | Unset = UNSET,
    series_id: int | Unset = UNSET,
    grade_min: float | Unset = UNSET,
    grade_max: float | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
) -> ListCollectionResponse200 | TooManyRequestsError | UnauthorizedError | None:
    """List collection.

     Returns all issues in the user's collection with series and publisher info.

    Needs `read:user` or `read:showcase`. A `read:showcase` token gets each copy without
    `price_paid`, `estimated_value`, `value_last_updated`, `price_sold`, `sold_at`,
    `purchased_at`, `purchase_source`, `purchase_store`, `acquisition_method`,
    `comic_shop_id`, `comic_shop`, `notes`, `grader_notes`, `storage_location`,
    `custom_label`, `bagged_at`, `personal_rating`, `tags` or `loan`, leaves out copies
    marked not public, and the `estimated_value` and `price_paid` sorts fall back to `date_added`.

    Args:
        per_page (int | Unset): Items per page (max 100).
        page (int | Unset): Page number.
        search (str | Unset): Filter by issue name, issue number, or series name.
        format_ (str | Unset): Filter by stored format.
        graded (bool | Unset): Filter to graded (true) or raw (false) copies.
        is_signed (bool | Unset): Filter to signed (true) or unsigned (false) copies. PRO; ignored
            for other members.
        condition (str | Unset): Filter by condition grade code.
        status (str | Unset): Which copies to return: owned, for_sale, sold, or all. Sold copies
            are excluded by default.
        for_sale (bool | Unset): Filter to copies marked for sale.
        for_trade (bool | Unset): Filter to copies marked for trade.
        read_status (str | Unset): Filter by read state. One of: read, unread.
        publisher_id (int | Unset): Filter to issues from a publisher.
        series_id (int | Unset): Filter to copies of issues in a series.
        grade_min (float | Unset): Filter to copies with a numeric grade at or above this value.
            PRO; ignored for other members.
        grade_max (float | Unset): Filter to copies with a numeric grade at or below this value.
            PRO; ignored for other members.
        sort_by (str | Unset): Sort field. One of: date_added, title, release_date,
            estimated_value, price_paid.
        sort_order (str | Unset): Sort direction. One of: asc, desc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCollectionResponse200 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            client=client,
            per_page=per_page,
            page=page,
            search=search,
            format_=format_,
            graded=graded,
            is_signed=is_signed,
            condition=condition,
            status=status,
            for_sale=for_sale,
            for_trade=for_trade,
            read_status=read_status,
            publisher_id=publisher_id,
            series_id=series_id,
            grade_min=grade_min,
            grade_max=grade_max,
            sort_by=sort_by,
            sort_order=sort_order,
        )
    ).parsed
