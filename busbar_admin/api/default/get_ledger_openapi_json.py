from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_ledger_openapi_json_response_200 import GetLedgerOpenapiJsonResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/admin/ledger/openapi.json",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | GetLedgerOpenapiJsonResponse200 | None:
    if response.status_code == 200:
        response_200 = GetLedgerOpenapiJsonResponse200.from_dict(response.json())

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
) -> Response[Error | GetLedgerOpenapiJsonResponse200]:
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
) -> Response[Error | GetLedgerOpenapiJsonResponse200]:
    """The full administrative OpenAPI 3.1 document, served at the ledger's own path

     The committed, generated document, unfiltered: every operation this BUILD can serve, including each
    plane's. `GET /openapi.json` serves the same document filtered to the planes this node configured.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetLedgerOpenapiJsonResponse200]
    """

    kwargs = _get_kwargs()

    response = client._request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Error | GetLedgerOpenapiJsonResponse200 | None:
    """The full administrative OpenAPI 3.1 document, served at the ledger's own path

     The committed, generated document, unfiltered: every operation this BUILD can serve, including each
    plane's. `GET /openapi.json` serves the same document filtered to the planes this node configured.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetLedgerOpenapiJsonResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Error | GetLedgerOpenapiJsonResponse200]:
    """The full administrative OpenAPI 3.1 document, served at the ledger's own path

     The committed, generated document, unfiltered: every operation this BUILD can serve, including each
    plane's. `GET /openapi.json` serves the same document filtered to the planes this node configured.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetLedgerOpenapiJsonResponse200]
    """

    kwargs = _get_kwargs()

    response = await client._async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Error | GetLedgerOpenapiJsonResponse200 | None:
    """The full administrative OpenAPI 3.1 document, served at the ledger's own path

     The committed, generated document, unfiltered: every operation this BUILD can serve, including each
    plane's. `GET /openapi.json` serves the same document filtered to the planes this node configured.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetLedgerOpenapiJsonResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
