from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cache_flush_view import CacheFlushView
from ...models.error import Error
from ...models.flush_cache_req import FlushCacheReq
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: FlushCacheReq | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/admin/auth/cache/flush",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CacheFlushView | Error | None:
    if response.status_code == 200:
        response_200 = CacheFlushView.from_dict(response.json())

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
) -> Response[CacheFlushView | Error]:
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
    body: FlushCacheReq | Unset = UNSET,
) -> Response[CacheFlushView | Error]:
    """Flush the credential cache: one module's partition (`{module}`) or everything (empty body). Instant
    revocation of the cached-allow window

    Args:
        body (FlushCacheReq | Unset): The `POST /api/v1/admin/auth/cache/flush` body. An absent
            body (or an absent `module`) flushes
            every partition. Deliberately NOT `deny_unknown_fields`: the endpoint has always ignored
            extra
            members, and tightening that would reject a call that works today.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CacheFlushView | Error]
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
    body: FlushCacheReq | Unset = UNSET,
) -> CacheFlushView | Error | None:
    """Flush the credential cache: one module's partition (`{module}`) or everything (empty body). Instant
    revocation of the cached-allow window

    Args:
        body (FlushCacheReq | Unset): The `POST /api/v1/admin/auth/cache/flush` body. An absent
            body (or an absent `module`) flushes
            every partition. Deliberately NOT `deny_unknown_fields`: the endpoint has always ignored
            extra
            members, and tightening that would reject a call that works today.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CacheFlushView | Error
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: FlushCacheReq | Unset = UNSET,
) -> Response[CacheFlushView | Error]:
    """Flush the credential cache: one module's partition (`{module}`) or everything (empty body). Instant
    revocation of the cached-allow window

    Args:
        body (FlushCacheReq | Unset): The `POST /api/v1/admin/auth/cache/flush` body. An absent
            body (or an absent `module`) flushes
            every partition. Deliberately NOT `deny_unknown_fields`: the endpoint has always ignored
            extra
            members, and tightening that would reject a call that works today.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CacheFlushView | Error]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client._async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: FlushCacheReq | Unset = UNSET,
) -> CacheFlushView | Error | None:
    """Flush the credential cache: one module's partition (`{module}`) or everything (empty body). Instant
    revocation of the cached-allow window

    Args:
        body (FlushCacheReq | Unset): The `POST /api/v1/admin/auth/cache/flush` body. An absent
            body (or an absent `module`) flushes
            every partition. Deliberately NOT `deny_unknown_fields`: the endpoint has always ignored
            extra
            members, and tightening that would reject a call that works today.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CacheFlushView | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
