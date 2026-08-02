from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_key_req import CreateKeyReq
from ...models.created_key_view import CreatedKeyView
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    body: CreateKeyReq,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/admin/keys",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreatedKeyView | Error | None:
    if response.status_code == 201:
        response_201 = CreatedKeyView.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreatedKeyView | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateKeyReq,
) -> Response[CreatedKeyView | Error]:
    """Mint a virtual key. The secret is returned EXACTLY once. Honors an `Idempotency-Key` header (per-
    principal ~10min replay)

    Args:
        body (CreateKeyReq): `POST /keys` body (1.5.0 signed-token keys, S1): PURE AUTH + a signed
            expiring token. A minted
            key is a busbar-signed `{sub, exp, kid}` token, returned ONCE. No rpm/tpm/budget on a key
            - all
            enforcement flows through the bound `group`. `#[serde(deny_unknown_fields)]` so the
            removed
            1.4.x fields (max_budget_cents/rpm_limit/tpm_limit/budget_period) fail loudly.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatedKeyView | Error]
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
    client: AuthenticatedClient,
    body: CreateKeyReq,
) -> CreatedKeyView | Error | None:
    """Mint a virtual key. The secret is returned EXACTLY once. Honors an `Idempotency-Key` header (per-
    principal ~10min replay)

    Args:
        body (CreateKeyReq): `POST /keys` body (1.5.0 signed-token keys, S1): PURE AUTH + a signed
            expiring token. A minted
            key is a busbar-signed `{sub, exp, kid}` token, returned ONCE. No rpm/tpm/budget on a key
            - all
            enforcement flows through the bound `group`. `#[serde(deny_unknown_fields)]` so the
            removed
            1.4.x fields (max_budget_cents/rpm_limit/tpm_limit/budget_period) fail loudly.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatedKeyView | Error
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateKeyReq,
) -> Response[CreatedKeyView | Error]:
    """Mint a virtual key. The secret is returned EXACTLY once. Honors an `Idempotency-Key` header (per-
    principal ~10min replay)

    Args:
        body (CreateKeyReq): `POST /keys` body (1.5.0 signed-token keys, S1): PURE AUTH + a signed
            expiring token. A minted
            key is a busbar-signed `{sub, exp, kid}` token, returned ONCE. No rpm/tpm/budget on a key
            - all
            enforcement flows through the bound `group`. `#[serde(deny_unknown_fields)]` so the
            removed
            1.4.x fields (max_budget_cents/rpm_limit/tpm_limit/budget_period) fail loudly.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatedKeyView | Error]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateKeyReq,
) -> CreatedKeyView | Error | None:
    """Mint a virtual key. The secret is returned EXACTLY once. Honors an `Idempotency-Key` header (per-
    principal ~10min replay)

    Args:
        body (CreateKeyReq): `POST /keys` body (1.5.0 signed-token keys, S1): PURE AUTH + a signed
            expiring token. A minted
            key is a busbar-signed `{sub, exp, kid}` token, returned ONCE. No rpm/tpm/budget on a key
            - all
            enforcement flows through the bound `group`. `#[serde(deny_unknown_fields)]` so the
            removed
            1.4.x fields (max_budget_cents/rpm_limit/tpm_limit/budget_period) fail loudly.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatedKeyView | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
