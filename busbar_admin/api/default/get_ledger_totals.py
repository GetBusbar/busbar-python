from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.ledger_totals import LedgerTotals
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/admin/ledger/totals",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | LedgerTotals:
    if response.status_code == 200:
        response_200 = LedgerTotals.from_dict(response.json())

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

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | LedgerTotals]:
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
) -> Response[Error | LedgerTotals]:
    """What the one ledger's counts come to, per key

     Each key's usage counts priced by the one function against the rate card each era was earned under —
    the figure `GET /keys/{id}/usage` derives. A key whose counts the rate card refused to price is
    withheld and named under `refused`; every other key with anything counted is served. A read: it
    mutates nothing, is never posture-gated, and needs no more authority than `GET /usage`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | LedgerTotals]
    """

    kwargs = _get_kwargs()

    response = client._request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Error | LedgerTotals | None:
    """What the one ledger's counts come to, per key

     Each key's usage counts priced by the one function against the rate card each era was earned under —
    the figure `GET /keys/{id}/usage` derives. A key whose counts the rate card refused to price is
    withheld and named under `refused`; every other key with anything counted is served. A read: it
    mutates nothing, is never posture-gated, and needs no more authority than `GET /usage`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | LedgerTotals
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Error | LedgerTotals]:
    """What the one ledger's counts come to, per key

     Each key's usage counts priced by the one function against the rate card each era was earned under —
    the figure `GET /keys/{id}/usage` derives. A key whose counts the rate card refused to price is
    withheld and named under `refused`; every other key with anything counted is served. A read: it
    mutates nothing, is never posture-gated, and needs no more authority than `GET /usage`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | LedgerTotals]
    """

    kwargs = _get_kwargs()

    response = await client._async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Error | LedgerTotals | None:
    """What the one ledger's counts come to, per key

     Each key's usage counts priced by the one function against the rate card each era was earned under —
    the figure `GET /keys/{id}/usage` derives. A key whose counts the rate card refused to price is
    withheld and named under `refused`; every other key with anything counted is served. A read: it
    mutates nothing, is never posture-gated, and needs no more authority than `GET /usage`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | LedgerTotals
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
