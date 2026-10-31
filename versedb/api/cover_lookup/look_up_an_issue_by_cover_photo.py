from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.look_up_an_issue_by_cover_photo_body import LookUpAnIssueByCoverPhotoBody
from ...models.look_up_an_issue_by_cover_photo_response_200 import LookUpAnIssueByCoverPhotoResponse200
from ...models.look_up_an_issue_by_cover_photo_response_422 import LookUpAnIssueByCoverPhotoResponse422
from ...models.look_up_an_issue_by_cover_photo_response_503 import LookUpAnIssueByCoverPhotoResponse503
from ...models.too_many_requests_error import TooManyRequestsError
from ...models.unauthorized_error import UnauthorizedError
from ...types import Response


def _get_kwargs(
    *,
    body: LookUpAnIssueByCoverPhotoBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/lookup/cover",
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    LookUpAnIssueByCoverPhotoResponse200
    | LookUpAnIssueByCoverPhotoResponse422
    | LookUpAnIssueByCoverPhotoResponse503
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    if response.status_code == 200:
        response_200 = LookUpAnIssueByCoverPhotoResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UnauthorizedError.from_dict(response.json())

        return response_401

    if response.status_code == 422:
        response_422 = LookUpAnIssueByCoverPhotoResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = TooManyRequestsError.from_dict(response.json())

        return response_429

    if response.status_code == 503:
        response_503 = LookUpAnIssueByCoverPhotoResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    LookUpAnIssueByCoverPhotoResponse200
    | LookUpAnIssueByCoverPhotoResponse422
    | LookUpAnIssueByCoverPhotoResponse503
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
    *,
    client: AuthenticatedClient | Client,
    body: LookUpAnIssueByCoverPhotoBody,
) -> Response[
    LookUpAnIssueByCoverPhotoResponse200
    | LookUpAnIssueByCoverPhotoResponse422
    | LookUpAnIssueByCoverPhotoResponse503
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Look up an issue by cover photo.

     Upload a photo of a comic cover (bare, bagged or slabbed) as `image`. `clear_match` true means
    the image match is sure of the issue: `issue_id` is it, and `variant_id` is the cover when the
    match also settled which of the issue's covers it is (null is the issue's own cover, or a cover
    it could not tell apart from a same-art sibling such as a newsstand edition). `clear_match`
    false means the image was not sure: `issue_id` is null and `candidates` lists up to five
    issues it could be, best first, each at its best-scoring cover. Only the image is compared;
    no text is read off the cover, so a slab label's grade is not returned. Requires the
    `read:public` scope. Rate limited separately from catalog reads: 5/min and 100/day, or
    15/min and 500/day on PRO.

    Args:
        body (LookUpAnIssueByCoverPhotoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LookUpAnIssueByCoverPhotoResponse200 | LookUpAnIssueByCoverPhotoResponse422 | LookUpAnIssueByCoverPhotoResponse503 | TooManyRequestsError | UnauthorizedError]
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
    body: LookUpAnIssueByCoverPhotoBody,
) -> (
    LookUpAnIssueByCoverPhotoResponse200
    | LookUpAnIssueByCoverPhotoResponse422
    | LookUpAnIssueByCoverPhotoResponse503
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Look up an issue by cover photo.

     Upload a photo of a comic cover (bare, bagged or slabbed) as `image`. `clear_match` true means
    the image match is sure of the issue: `issue_id` is it, and `variant_id` is the cover when the
    match also settled which of the issue's covers it is (null is the issue's own cover, or a cover
    it could not tell apart from a same-art sibling such as a newsstand edition). `clear_match`
    false means the image was not sure: `issue_id` is null and `candidates` lists up to five
    issues it could be, best first, each at its best-scoring cover. Only the image is compared;
    no text is read off the cover, so a slab label's grade is not returned. Requires the
    `read:public` scope. Rate limited separately from catalog reads: 5/min and 100/day, or
    15/min and 500/day on PRO.

    Args:
        body (LookUpAnIssueByCoverPhotoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LookUpAnIssueByCoverPhotoResponse200 | LookUpAnIssueByCoverPhotoResponse422 | LookUpAnIssueByCoverPhotoResponse503 | TooManyRequestsError | UnauthorizedError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LookUpAnIssueByCoverPhotoBody,
) -> Response[
    LookUpAnIssueByCoverPhotoResponse200
    | LookUpAnIssueByCoverPhotoResponse422
    | LookUpAnIssueByCoverPhotoResponse503
    | TooManyRequestsError
    | UnauthorizedError
]:
    """Look up an issue by cover photo.

     Upload a photo of a comic cover (bare, bagged or slabbed) as `image`. `clear_match` true means
    the image match is sure of the issue: `issue_id` is it, and `variant_id` is the cover when the
    match also settled which of the issue's covers it is (null is the issue's own cover, or a cover
    it could not tell apart from a same-art sibling such as a newsstand edition). `clear_match`
    false means the image was not sure: `issue_id` is null and `candidates` lists up to five
    issues it could be, best first, each at its best-scoring cover. Only the image is compared;
    no text is read off the cover, so a slab label's grade is not returned. Requires the
    `read:public` scope. Rate limited separately from catalog reads: 5/min and 100/day, or
    15/min and 500/day on PRO.

    Args:
        body (LookUpAnIssueByCoverPhotoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LookUpAnIssueByCoverPhotoResponse200 | LookUpAnIssueByCoverPhotoResponse422 | LookUpAnIssueByCoverPhotoResponse503 | TooManyRequestsError | UnauthorizedError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: LookUpAnIssueByCoverPhotoBody,
) -> (
    LookUpAnIssueByCoverPhotoResponse200
    | LookUpAnIssueByCoverPhotoResponse422
    | LookUpAnIssueByCoverPhotoResponse503
    | TooManyRequestsError
    | UnauthorizedError
    | None
):
    """Look up an issue by cover photo.

     Upload a photo of a comic cover (bare, bagged or slabbed) as `image`. `clear_match` true means
    the image match is sure of the issue: `issue_id` is it, and `variant_id` is the cover when the
    match also settled which of the issue's covers it is (null is the issue's own cover, or a cover
    it could not tell apart from a same-art sibling such as a newsstand edition). `clear_match`
    false means the image was not sure: `issue_id` is null and `candidates` lists up to five
    issues it could be, best first, each at its best-scoring cover. Only the image is compared;
    no text is read off the cover, so a slab label's grade is not returned. Requires the
    `read:public` scope. Rate limited separately from catalog reads: 5/min and 100/day, or
    15/min and 500/day on PRO.

    Args:
        body (LookUpAnIssueByCoverPhotoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LookUpAnIssueByCoverPhotoResponse200 | LookUpAnIssueByCoverPhotoResponse422 | LookUpAnIssueByCoverPhotoResponse503 | TooManyRequestsError | UnauthorizedError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
