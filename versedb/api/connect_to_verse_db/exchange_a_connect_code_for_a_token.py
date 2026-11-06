from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exchange_a_connect_code_for_a_token_body import ExchangeAConnectCodeForATokenBody
from ...models.exchange_a_connect_code_for_a_token_response_200 import ExchangeAConnectCodeForATokenResponse200
from ...models.exchange_a_connect_code_for_a_token_response_400 import ExchangeAConnectCodeForATokenResponse400
from ...models.too_many_requests_error import TooManyRequestsError
from ...types import Response


def _get_kwargs(
    *,
    body: ExchangeAConnectCodeForATokenBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/connect/token",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExchangeAConnectCodeForATokenResponse200 | ExchangeAConnectCodeForATokenResponse400 | TooManyRequestsError | None:
    if response.status_code == 200:
        response_200 = ExchangeAConnectCodeForATokenResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ExchangeAConnectCodeForATokenResponse400.from_dict(response.json())

        return response_400

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
    ExchangeAConnectCodeForATokenResponse200 | ExchangeAConnectCodeForATokenResponse400 | TooManyRequestsError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExchangeAConnectCodeForATokenBody,
) -> Response[
    ExchangeAConnectCodeForATokenResponse200 | ExchangeAConnectCodeForATokenResponse400 | TooManyRequestsError
]:
    """Exchange a Connect code for a token

     Redeems the single-use code from the Connect redirect. A code works once: a second attempt,
    a wrong `code_verifier` or a different `redirect_uri` fails and the code cannot be used again.

    Args:
        body (ExchangeAConnectCodeForATokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeAConnectCodeForATokenResponse200 | ExchangeAConnectCodeForATokenResponse400 | TooManyRequestsError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ExchangeAConnectCodeForATokenBody,
) -> ExchangeAConnectCodeForATokenResponse200 | ExchangeAConnectCodeForATokenResponse400 | TooManyRequestsError | None:
    """Exchange a Connect code for a token

     Redeems the single-use code from the Connect redirect. A code works once: a second attempt,
    a wrong `code_verifier` or a different `redirect_uri` fails and the code cannot be used again.

    Args:
        body (ExchangeAConnectCodeForATokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeAConnectCodeForATokenResponse200 | ExchangeAConnectCodeForATokenResponse400 | TooManyRequestsError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExchangeAConnectCodeForATokenBody,
) -> Response[
    ExchangeAConnectCodeForATokenResponse200 | ExchangeAConnectCodeForATokenResponse400 | TooManyRequestsError
]:
    """Exchange a Connect code for a token

     Redeems the single-use code from the Connect redirect. A code works once: a second attempt,
    a wrong `code_verifier` or a different `redirect_uri` fails and the code cannot be used again.

    Args:
        body (ExchangeAConnectCodeForATokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeAConnectCodeForATokenResponse200 | ExchangeAConnectCodeForATokenResponse400 | TooManyRequestsError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ExchangeAConnectCodeForATokenBody,
) -> ExchangeAConnectCodeForATokenResponse200 | ExchangeAConnectCodeForATokenResponse400 | TooManyRequestsError | None:
    """Exchange a Connect code for a token

     Redeems the single-use code from the Connect redirect. A code works once: a second attempt,
    a wrong `code_verifier` or a different `redirect_uri` fails and the code cannot be used again.

    Args:
        body (ExchangeAConnectCodeForATokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeAConnectCodeForATokenResponse200 | ExchangeAConnectCodeForATokenResponse400 | TooManyRequestsError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
