from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.ledger_checkpoints import LedgerCheckpoints
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/admin/ledger/checkpoints",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | LedgerCheckpoints | None:
    if response.status_code == 200:
        response_200 = LedgerCheckpoints.from_dict(response.json())

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


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | LedgerCheckpoints]:
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
) -> Response[Error | LedgerCheckpoints]:
    """The sealed checkpoint figures

     Money is the one ledger's counts x the rate card, recomputed on every read, so no balance checkpoint
    is sealed and the list is empty. The shape is kept for clients that read it. A read: it mutates
    nothing, is never posture-gated, and needs no more authority than `GET /usage`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | LedgerCheckpoints]
    """

    kwargs = _get_kwargs()

    response = client._request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Error | LedgerCheckpoints | None:
    """The sealed checkpoint figures

     Money is the one ledger's counts x the rate card, recomputed on every read, so no balance checkpoint
    is sealed and the list is empty. The shape is kept for clients that read it. A read: it mutates
    nothing, is never posture-gated, and needs no more authority than `GET /usage`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | LedgerCheckpoints
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Error | LedgerCheckpoints]:
    """The sealed checkpoint figures

     Money is the one ledger's counts x the rate card, recomputed on every read, so no balance checkpoint
    is sealed and the list is empty. The shape is kept for clients that read it. A read: it mutates
    nothing, is never posture-gated, and needs no more authority than `GET /usage`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | LedgerCheckpoints]
    """

    kwargs = _get_kwargs()

    response = await client._async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Error | LedgerCheckpoints | None:
    """The sealed checkpoint figures

     Money is the one ledger's counts x the rate card, recomputed on every read, so no balance checkpoint
    is sealed and the list is empty. The shape is kept for clients that read it. A read: it mutates
    nothing, is never posture-gated, and needs no more authority than `GET /usage`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | LedgerCheckpoints
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
