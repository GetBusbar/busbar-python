from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_key_req import CreateKeyReq
from ...models.created_key_view import CreatedKeyView
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateKeyReq,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

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

    if response.status_code == 413:
        response_413 = Error.from_dict(response.json())

        return response_413

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

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
) -> Response[CreatedKeyView | Error]:
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
    body: CreateKeyReq,
    idempotency_key: str | Unset = UNSET,
) -> Response[CreatedKeyView | Error]:
    """Mint a virtual key. The secret is returned EXACTLY once. Honors an `Idempotency-Key` header (per-
    principal ~10min replay)

    Args:
        idempotency_key (str | Unset):
        body (CreateKeyReq): `POST /keys` body (1.5.0 signed-token keys): PURE AUTH + a signed
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
        idempotency_key=idempotency_key,
    )

    response = client._request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateKeyReq,
    idempotency_key: str | Unset = UNSET,
) -> CreatedKeyView | Error | None:
    """Mint a virtual key. The secret is returned EXACTLY once. Honors an `Idempotency-Key` header (per-
    principal ~10min replay)

    Args:
        idempotency_key (str | Unset):
        body (CreateKeyReq): `POST /keys` body (1.5.0 signed-token keys): PURE AUTH + a signed
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
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateKeyReq,
    idempotency_key: str | Unset = UNSET,
) -> Response[CreatedKeyView | Error]:
    """Mint a virtual key. The secret is returned EXACTLY once. Honors an `Idempotency-Key` header (per-
    principal ~10min replay)

    Args:
        idempotency_key (str | Unset):
        body (CreateKeyReq): `POST /keys` body (1.5.0 signed-token keys): PURE AUTH + a signed
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
        idempotency_key=idempotency_key,
    )

    response = await client._async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateKeyReq,
    idempotency_key: str | Unset = UNSET,
) -> CreatedKeyView | Error | None:
    """Mint a virtual key. The secret is returned EXACTLY once. Honors an `Idempotency-Key` header (per-
    principal ~10min replay)

    Args:
        idempotency_key (str | Unset):
        body (CreateKeyReq): `POST /keys` body (1.5.0 signed-token keys): PURE AUTH + a signed
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
            idempotency_key=idempotency_key,
        )
    ).parsed
