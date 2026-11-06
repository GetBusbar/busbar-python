from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.verify_view import VerifyView
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/admin/verify",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | VerifyView | None:
    if response.status_code == 200:
        response_200 = VerifyView.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 413:
        response_413 = Error.from_dict(response.json())

        return response_413

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())

        return response_503

    try:
        response_default = Error.from_dict(response.json())

        return response_default

    except (ValueError, KeyError, TypeError, AttributeError):
        # An intermediary may return an undocumented non-JSON or malformed body.
        # Preserve the raw response and the caller's unexpected-status policy.
        if client.raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content) from None
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | VerifyView]:
    return Response(
        status_code=HTTPStatus(response.status_code)
        if response.status_code in HTTPStatus._value2member_map_
        else response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Error | VerifyView]:
    """Verify this node's ledger: checkpoints, sequences, the book and the identity

     Every sealed checkpoint must re-hash to its own body, no node's sequence may go backwards between
    two checkpoints, the book as it stands is measured against the last checkpoint, and the ledger's
    postings must reconcile with the previous release's rows. A failed verification is still a 200: `ok`
    is the answer and `findings` says why. A read: it mutates nothing and needs `read-only`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | VerifyView]
    """

    kwargs = _get_kwargs()

    response = client._request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Error | VerifyView | None:
    """Verify this node's ledger: checkpoints, sequences, the book and the identity

     Every sealed checkpoint must re-hash to its own body, no node's sequence may go backwards between
    two checkpoints, the book as it stands is measured against the last checkpoint, and the ledger's
    postings must reconcile with the previous release's rows. A failed verification is still a 200: `ok`
    is the answer and `findings` says why. A read: it mutates nothing and needs `read-only`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | VerifyView
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Error | VerifyView]:
    """Verify this node's ledger: checkpoints, sequences, the book and the identity

     Every sealed checkpoint must re-hash to its own body, no node's sequence may go backwards between
    two checkpoints, the book as it stands is measured against the last checkpoint, and the ledger's
    postings must reconcile with the previous release's rows. A failed verification is still a 200: `ok`
    is the answer and `findings` says why. A read: it mutates nothing and needs `read-only`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | VerifyView]
    """

    kwargs = _get_kwargs()

    response = await client._async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Error | VerifyView | None:
    """Verify this node's ledger: checkpoints, sequences, the book and the identity

     Every sealed checkpoint must re-hash to its own body, no node's sequence may go backwards between
    two checkpoints, the book as it stands is measured against the last checkpoint, and the ledger's
    postings must reconcile with the previous release's rows. A failed verification is still a 200: `ok`
    is the answer and `findings` says why. A read: it mutates nothing and needs `read-only`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | VerifyView
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
