from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.mark_the_copys_open_loan_returned_body import MarkTheCopysOpenLoanReturnedBody
from ...models.mark_the_copys_open_loan_returned_response_200 import MarkTheCopysOpenLoanReturnedResponse200
from ...models.mark_the_copys_open_loan_returned_response_404_type_0 import MarkTheCopysOpenLoanReturnedResponse404Type0
from ...models.mark_the_copys_open_loan_returned_response_404_type_1 import MarkTheCopysOpenLoanReturnedResponse404Type1
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_item_id: int,
    *,
    body: MarkTheCopysOpenLoanReturnedBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/user/collections/{collection_item_id}/loan".format(
            collection_item_id=quote(str(collection_item_id), safe=""),
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
    MarkTheCopysOpenLoanReturnedResponse200
    | MarkTheCopysOpenLoanReturnedResponse404Type0
    | MarkTheCopysOpenLoanReturnedResponse404Type1
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    if response.status_code == 200:
        response_200 = MarkTheCopysOpenLoanReturnedResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 404:

        def _parse_response_404(
            data: object,
        ) -> MarkTheCopysOpenLoanReturnedResponse404Type0 | MarkTheCopysOpenLoanReturnedResponse404Type1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_404_type_0 = MarkTheCopysOpenLoanReturnedResponse404Type0.from_dict(data)

                return response_404_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_404_type_1 = MarkTheCopysOpenLoanReturnedResponse404Type1.from_dict(data)

            return response_404_type_1

        response_404 = _parse_response_404(response.json())

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
    MarkTheCopysOpenLoanReturnedResponse200
    | MarkTheCopysOpenLoanReturnedResponse404Type0
    | MarkTheCopysOpenLoanReturnedResponse404Type1
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
    collection_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: MarkTheCopysOpenLoanReturnedBody | Unset = UNSET,
) -> Response[
    MarkTheCopysOpenLoanReturnedResponse200
    | MarkTheCopysOpenLoanReturnedResponse404Type0
    | MarkTheCopysOpenLoanReturnedResponse404Type1
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Mark the copy's open loan returned.

     Closes the open loan and hands custody back to the owner. A copy with no open loan is a
    404, so a repeat call does not silently succeed.

    Args:
        collection_item_id (int):
        body (MarkTheCopysOpenLoanReturnedBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MarkTheCopysOpenLoanReturnedResponse200 | MarkTheCopysOpenLoanReturnedResponse404Type0 | MarkTheCopysOpenLoanReturnedResponse404Type1 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        collection_item_id=collection_item_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: MarkTheCopysOpenLoanReturnedBody | Unset = UNSET,
) -> (
    MarkTheCopysOpenLoanReturnedResponse200
    | MarkTheCopysOpenLoanReturnedResponse404Type0
    | MarkTheCopysOpenLoanReturnedResponse404Type1
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Mark the copy's open loan returned.

     Closes the open loan and hands custody back to the owner. A copy with no open loan is a
    404, so a repeat call does not silently succeed.

    Args:
        collection_item_id (int):
        body (MarkTheCopysOpenLoanReturnedBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MarkTheCopysOpenLoanReturnedResponse200 | MarkTheCopysOpenLoanReturnedResponse404Type0 | MarkTheCopysOpenLoanReturnedResponse404Type1 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        collection_item_id=collection_item_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    collection_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: MarkTheCopysOpenLoanReturnedBody | Unset = UNSET,
) -> Response[
    MarkTheCopysOpenLoanReturnedResponse200
    | MarkTheCopysOpenLoanReturnedResponse404Type0
    | MarkTheCopysOpenLoanReturnedResponse404Type1
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Mark the copy's open loan returned.

     Closes the open loan and hands custody back to the owner. A copy with no open loan is a
    404, so a repeat call does not silently succeed.

    Args:
        collection_item_id (int):
        body (MarkTheCopysOpenLoanReturnedBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MarkTheCopysOpenLoanReturnedResponse200 | MarkTheCopysOpenLoanReturnedResponse404Type0 | MarkTheCopysOpenLoanReturnedResponse404Type1 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        collection_item_id=collection_item_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_item_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: MarkTheCopysOpenLoanReturnedBody | Unset = UNSET,
) -> (
    MarkTheCopysOpenLoanReturnedResponse200
    | MarkTheCopysOpenLoanReturnedResponse404Type0
    | MarkTheCopysOpenLoanReturnedResponse404Type1
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Mark the copy's open loan returned.

     Closes the open loan and hands custody back to the owner. A copy with no open loan is a
    404, so a repeat call does not silently succeed.

    Args:
        collection_item_id (int):
        body (MarkTheCopysOpenLoanReturnedBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MarkTheCopysOpenLoanReturnedResponse200 | MarkTheCopysOpenLoanReturnedResponse404Type0 | MarkTheCopysOpenLoanReturnedResponse404Type1 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            collection_item_id=collection_item_id,
            client=client,
            body=body,
        )
    ).parsed
