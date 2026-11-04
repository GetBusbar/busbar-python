from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.trust_key_req import TrustKeyReq
from ...models.trust_key_view import TrustKeyView
from ...types import Response


def _get_kwargs(
    *,
    body: TrustKeyReq,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/admin/trust/revoke",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | TrustKeyView | None:
    if response.status_code == 200:
        response_200 = TrustKeyView.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | TrustKeyView]:
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
    body: TrustKeyReq,
) -> Response[Error | TrustKeyView]:
    """Revoke one trust key

     Refused until approved again: a counterparty revoked refuses everything at it, an item revoked
    refuses it over its configured approval. The decision is kept durably and outlives a restart.
    Idempotent: the same key twice answers the same row.

    Args:
        body (TrustKeyReq): `POST /trust/approve` and `/trust/revoke`: the trust key decided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TrustKeyView]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client._request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: TrustKeyReq,
) -> Error | TrustKeyView | None:
    """Revoke one trust key

     Refused until approved again: a counterparty revoked refuses everything at it, an item revoked
    refuses it over its configured approval. The decision is kept durably and outlives a restart.
    Idempotent: the same key twice answers the same row.

    Args:
        body (TrustKeyReq): `POST /trust/approve` and `/trust/revoke`: the trust key decided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TrustKeyView
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: TrustKeyReq,
) -> Response[Error | TrustKeyView]:
    """Revoke one trust key

     Refused until approved again: a counterparty revoked refuses everything at it, an item revoked
    refuses it over its configured approval. The decision is kept durably and outlives a restart.
    Idempotent: the same key twice answers the same row.

    Args:
        body (TrustKeyReq): `POST /trust/approve` and `/trust/revoke`: the trust key decided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TrustKeyView]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client._async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: TrustKeyReq,
) -> Error | TrustKeyView | None:
    """Revoke one trust key

     Refused until approved again: a counterparty revoked refuses everything at it, an item revoked
    refuses it over its configured approval. The decision is kept durably and outlives a restart.
    Idempotent: the same key twice answers the same row.

    Args:
        body (TrustKeyReq): `POST /trust/approve` and `/trust/revoke`: the trust key decided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TrustKeyView
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
