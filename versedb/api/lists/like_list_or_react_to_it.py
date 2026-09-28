from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.like_list_or_react_to_it_body import LikeListOrReactToItBody
from ...models.like_list_or_react_to_it_response_200_type_0 import LikeListOrReactToItResponse200Type0
from ...models.like_list_or_react_to_it_response_200_type_1 import LikeListOrReactToItResponse200Type1
from ...models.like_list_or_react_to_it_response_201 import LikeListOrReactToItResponse201
from ...models.like_list_or_react_to_it_response_403 import LikeListOrReactToItResponse403
from ...models.like_list_or_react_to_it_response_422 import LikeListOrReactToItResponse422
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    list_id: int,
    *,
    body: LikeListOrReactToItBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/lists/{list_id}/like".format(
            list_id=quote(str(list_id), safe=""),
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
    LikeListOrReactToItResponse200Type0
    | LikeListOrReactToItResponse200Type1
    | LikeListOrReactToItResponse201
    | LikeListOrReactToItResponse403
    | LikeListOrReactToItResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> LikeListOrReactToItResponse200Type0 | LikeListOrReactToItResponse200Type1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = LikeListOrReactToItResponse200Type0.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = LikeListOrReactToItResponse200Type1.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = LikeListOrReactToItResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = LikeListOrReactToItResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = LikeListOrReactToItResponse422.from_dict(response.json())

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
    LikeListOrReactToItResponse200Type0
    | LikeListOrReactToItResponse200Type1
    | LikeListOrReactToItResponse201
    | LikeListOrReactToItResponse403
    | LikeListOrReactToItResponse422
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
    list_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: LikeListOrReactToItBody | Unset = UNSET,
) -> Response[
    LikeListOrReactToItResponse200Type0
    | LikeListOrReactToItResponse200Type1
    | LikeListOrReactToItResponse201
    | LikeListOrReactToItResponse403
    | LikeListOrReactToItResponse422
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Like list, or react to it.

     With no body this likes the list. Send `reaction` to leave that reaction instead, or to
    change the one already held; `DELETE` takes it back whichever it is. A member holds one
    reaction per list and every reaction counts toward `likes_count`. Cannot like your own lists.

    Args:
        list_id (int):
        body (LikeListOrReactToItBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LikeListOrReactToItResponse200Type0 | LikeListOrReactToItResponse200Type1 | LikeListOrReactToItResponse201 | LikeListOrReactToItResponse403 | LikeListOrReactToItResponse422 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    list_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: LikeListOrReactToItBody | Unset = UNSET,
) -> (
    LikeListOrReactToItResponse200Type0
    | LikeListOrReactToItResponse200Type1
    | LikeListOrReactToItResponse201
    | LikeListOrReactToItResponse403
    | LikeListOrReactToItResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Like list, or react to it.

     With no body this likes the list. Send `reaction` to leave that reaction instead, or to
    change the one already held; `DELETE` takes it back whichever it is. A member holds one
    reaction per list and every reaction counts toward `likes_count`. Cannot like your own lists.

    Args:
        list_id (int):
        body (LikeListOrReactToItBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LikeListOrReactToItResponse200Type0 | LikeListOrReactToItResponse200Type1 | LikeListOrReactToItResponse201 | LikeListOrReactToItResponse403 | LikeListOrReactToItResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        list_id=list_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    list_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: LikeListOrReactToItBody | Unset = UNSET,
) -> Response[
    LikeListOrReactToItResponse200Type0
    | LikeListOrReactToItResponse200Type1
    | LikeListOrReactToItResponse201
    | LikeListOrReactToItResponse403
    | LikeListOrReactToItResponse422
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Like list, or react to it.

     With no body this likes the list. Send `reaction` to leave that reaction instead, or to
    change the one already held; `DELETE` takes it back whichever it is. A member holds one
    reaction per list and every reaction counts toward `likes_count`. Cannot like your own lists.

    Args:
        list_id (int):
        body (LikeListOrReactToItBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LikeListOrReactToItResponse200Type0 | LikeListOrReactToItResponse200Type1 | LikeListOrReactToItResponse201 | LikeListOrReactToItResponse403 | LikeListOrReactToItResponse422 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    list_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: LikeListOrReactToItBody | Unset = UNSET,
) -> (
    LikeListOrReactToItResponse200Type0
    | LikeListOrReactToItResponse200Type1
    | LikeListOrReactToItResponse201
    | LikeListOrReactToItResponse403
    | LikeListOrReactToItResponse422
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Like list, or react to it.

     With no body this likes the list. Send `reaction` to leave that reaction instead, or to
    change the one already held; `DELETE` takes it back whichever it is. A member holds one
    reaction per list and every reaction counts toward `likes_count`. Cannot like your own lists.

    Args:
        list_id (int):
        body (LikeListOrReactToItBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LikeListOrReactToItResponse200Type0 | LikeListOrReactToItResponse200Type1 | LikeListOrReactToItResponse201 | LikeListOrReactToItResponse403 | LikeListOrReactToItResponse422 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
            body=body,
        )
    ).parsed
