from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.edit_reading_date_body import EditReadingDateBody
from ...models.edit_reading_date_response_200 import EditReadingDateResponse200
from ...models.edit_reading_date_response_403 import EditReadingDateResponse403
from ...models.edit_reading_date_response_404 import EditReadingDateResponse404
from ...models.edit_reading_date_response_422_type_0 import EditReadingDateResponse422Type0
from ...models.edit_reading_date_response_422_type_1 import EditReadingDateResponse422Type1
from ...models.edit_reading_date_response_422_type_2 import EditReadingDateResponse422Type2
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    issue_id: int,
    *,
    body: EditReadingDateBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/issues/{issue_id}/read-status".format(
            issue_id=quote(str(issue_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | EditReadingDateResponse200
    | EditReadingDateResponse403
    | EditReadingDateResponse404
    | EditReadingDateResponse422Type0
    | EditReadingDateResponse422Type1
    | EditReadingDateResponse422Type2
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    if response.status_code == 200:
        response_200 = EditReadingDateResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = EditReadingDateResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = EditReadingDateResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:

        def _parse_response_422(
            data: object,
        ) -> EditReadingDateResponse422Type0 | EditReadingDateResponse422Type1 | EditReadingDateResponse422Type2:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = EditReadingDateResponse422Type0.from_dict(data)

                return response_422_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_1 = EditReadingDateResponse422Type1.from_dict(data)

                return response_422_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_2 = EditReadingDateResponse422Type2.from_dict(data)

            return response_422_type_2

        response_422 = _parse_response_422(response.json())

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
    Any
    | EditReadingDateResponse200
    | EditReadingDateResponse403
    | EditReadingDateResponse404
    | EditReadingDateResponse422Type0
    | EditReadingDateResponse422Type1
    | EditReadingDateResponse422Type2
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
    body: EditReadingDateBody | Unset = UNSET,
) -> Response[
    Any
    | EditReadingDateResponse200
    | EditReadingDateResponse403
    | EditReadingDateResponse404
    | EditReadingDateResponse422Type0
    | EditReadingDateResponse422Type1
    | EditReadingDateResponse422Type2
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Edit reading date.

     Updates the `read_at` date on an existing read entry, or removes the entry when `read_at` is null.
    If no entry exists yet and a date is provided, one is created (upsert).
    `undated: true` clears the date, or creates a read with no date; sending it with `read_at` is a 422.

    Args:
        issue_id (int): The issue ID.
        body (EditReadingDateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EditReadingDateResponse200 | EditReadingDateResponse403 | EditReadingDateResponse404 | EditReadingDateResponse422Type0 | EditReadingDateResponse422Type1 | EditReadingDateResponse422Type2 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        issue_id=issue_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    issue_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: EditReadingDateBody | Unset = UNSET,
) -> (
    Any
    | EditReadingDateResponse200
    | EditReadingDateResponse403
    | EditReadingDateResponse404
    | EditReadingDateResponse422Type0
    | EditReadingDateResponse422Type1
    | EditReadingDateResponse422Type2
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Edit reading date.

     Updates the `read_at` date on an existing read entry, or removes the entry when `read_at` is null.
    If no entry exists yet and a date is provided, one is created (upsert).
    `undated: true` clears the date, or creates a read with no date; sending it with `read_at` is a 422.

    Args:
        issue_id (int): The issue ID.
        body (EditReadingDateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EditReadingDateResponse200 | EditReadingDateResponse403 | EditReadingDateResponse404 | EditReadingDateResponse422Type0 | EditReadingDateResponse422Type1 | EditReadingDateResponse422Type2 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        issue_id=issue_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    issue_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: EditReadingDateBody | Unset = UNSET,
) -> Response[
    Any
    | EditReadingDateResponse200
    | EditReadingDateResponse403
    | EditReadingDateResponse404
    | EditReadingDateResponse422Type0
    | EditReadingDateResponse422Type1
    | EditReadingDateResponse422Type2
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Edit reading date.

     Updates the `read_at` date on an existing read entry, or removes the entry when `read_at` is null.
    If no entry exists yet and a date is provided, one is created (upsert).
    `undated: true` clears the date, or creates a read with no date; sending it with `read_at` is a 422.

    Args:
        issue_id (int): The issue ID.
        body (EditReadingDateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EditReadingDateResponse200 | EditReadingDateResponse403 | EditReadingDateResponse404 | EditReadingDateResponse422Type0 | EditReadingDateResponse422Type1 | EditReadingDateResponse422Type2 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        issue_id=issue_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    issue_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: EditReadingDateBody | Unset = UNSET,
) -> (
    Any
    | EditReadingDateResponse200
    | EditReadingDateResponse403
    | EditReadingDateResponse404
    | EditReadingDateResponse422Type0
    | EditReadingDateResponse422Type1
    | EditReadingDateResponse422Type2
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Edit reading date.

     Updates the `read_at` date on an existing read entry, or removes the entry when `read_at` is null.
    If no entry exists yet and a date is provided, one is created (upsert).
    `undated: true` clears the date, or creates a read with no date; sending it with `read_at` is a 422.

    Args:
        issue_id (int): The issue ID.
        body (EditReadingDateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EditReadingDateResponse200 | EditReadingDateResponse403 | EditReadingDateResponse404 | EditReadingDateResponse422Type0 | EditReadingDateResponse422Type1 | EditReadingDateResponse422Type2 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            issue_id=issue_id,
            client=client,
            body=body,
        )
    ).parsed
