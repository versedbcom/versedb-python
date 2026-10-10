from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.view_your_reading_goal_response_200 import ViewYourReadingGoalResponse200
from ...models.view_your_reading_goal_response_401 import ViewYourReadingGoalResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    year: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["year"] = year

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/user/reading-goal",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TooManyRequestsError | ViewYourReadingGoalResponse200 | ViewYourReadingGoalResponse401 | None:
    if response.status_code == 200:
        response_200 = ViewYourReadingGoalResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ViewYourReadingGoalResponse401.from_dict(response.json())

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
) -> Response[TooManyRequestsError | ViewYourReadingGoalResponse200 | ViewYourReadingGoalResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    year: int | Unset = UNSET,
) -> Response[TooManyRequestsError | ViewYourReadingGoalResponse200 | ViewYourReadingGoalResponse401]:
    """View your reading goal.

     Available to every authenticated member. Returns only the caller's goal.

    Needs `read:user` or `read:showcase`. A `read:showcase` token gets the goal without
    `notify_milestones`, `notify_lapses` and `email_updates`.

    Args:
        year (int | Unset): UTC year; defaults to the current year.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TooManyRequestsError | ViewYourReadingGoalResponse200 | ViewYourReadingGoalResponse401]
    """

    kwargs = _get_kwargs(
        year=year,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    year: int | Unset = UNSET,
) -> TooManyRequestsError | ViewYourReadingGoalResponse200 | ViewYourReadingGoalResponse401 | None:
    """View your reading goal.

     Available to every authenticated member. Returns only the caller's goal.

    Needs `read:user` or `read:showcase`. A `read:showcase` token gets the goal without
    `notify_milestones`, `notify_lapses` and `email_updates`.

    Args:
        year (int | Unset): UTC year; defaults to the current year.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TooManyRequestsError | ViewYourReadingGoalResponse200 | ViewYourReadingGoalResponse401
    """

    return sync_detailed(
        client=client,
        year=year,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    year: int | Unset = UNSET,
) -> Response[TooManyRequestsError | ViewYourReadingGoalResponse200 | ViewYourReadingGoalResponse401]:
    """View your reading goal.

     Available to every authenticated member. Returns only the caller's goal.

    Needs `read:user` or `read:showcase`. A `read:showcase` token gets the goal without
    `notify_milestones`, `notify_lapses` and `email_updates`.

    Args:
        year (int | Unset): UTC year; defaults to the current year.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TooManyRequestsError | ViewYourReadingGoalResponse200 | ViewYourReadingGoalResponse401]
    """

    kwargs = _get_kwargs(
        year=year,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    year: int | Unset = UNSET,
) -> TooManyRequestsError | ViewYourReadingGoalResponse200 | ViewYourReadingGoalResponse401 | None:
    """View your reading goal.

     Available to every authenticated member. Returns only the caller's goal.

    Needs `read:user` or `read:showcase`. A `read:showcase` token gets the goal without
    `notify_milestones`, `notify_lapses` and `email_updates`.

    Args:
        year (int | Unset): UTC year; defaults to the current year.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TooManyRequestsError | ViewYourReadingGoalResponse200 | ViewYourReadingGoalResponse401
    """

    return (
        await asyncio_detailed(
            client=client,
            year=year,
        )
    ).parsed
