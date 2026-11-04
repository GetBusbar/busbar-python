from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.ledger_migration import LedgerMigration
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/admin/ledger/migration",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | LedgerMigration | None:
    if response.status_code == 200:
        response_200 = LedgerMigration.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | LedgerMigration]:
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
) -> Response[Error | LedgerMigration]:
    """The marker the first boot after the upgrade sealed

     The previous release's rows ARE the one ledger's counts, read as they are, so no migration is
    sealed: `migrated` is false and `marker` null. A read: it mutates nothing, is never posture-gated,
    and needs no more authority than `GET /usage`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | LedgerMigration]
    """

    kwargs = _get_kwargs()

    response = client._request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Error | LedgerMigration | None:
    """The marker the first boot after the upgrade sealed

     The previous release's rows ARE the one ledger's counts, read as they are, so no migration is
    sealed: `migrated` is false and `marker` null. A read: it mutates nothing, is never posture-gated,
    and needs no more authority than `GET /usage`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | LedgerMigration
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Error | LedgerMigration]:
    """The marker the first boot after the upgrade sealed

     The previous release's rows ARE the one ledger's counts, read as they are, so no migration is
    sealed: `migrated` is false and `marker` null. A read: it mutates nothing, is never posture-gated,
    and needs no more authority than `GET /usage`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | LedgerMigration]
    """

    kwargs = _get_kwargs()

    response = await client._async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Error | LedgerMigration | None:
    """The marker the first boot after the upgrade sealed

     The previous release's rows ARE the one ledger's counts, read as they are, so no migration is
    sealed: `migrated` is false and `marker` null. A read: it mutates nothing, is never posture-gated,
    and needs no more authority than `GET /usage`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | LedgerMigration
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
