from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.key_view import KeyView
from ...models.mutation_applied_error import MutationAppliedError
from ...models.update_key_req import UpdateKeyReq
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: UpdateKeyReq,
    if_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/admin/keys/{id}".format(
            id=quote(str(id), safe="").replace(".", "%2E"),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Error | MutationAppliedError | KeyView:
    if response.status_code == 200:
        response_200 = KeyView.from_dict(response.json())

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

    if response.status_code == 409:

        def _parse_response_409(data: object) -> Error | MutationAppliedError:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_409_type_0 = Error.from_dict(data)

                return response_409_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_409_type_1 = MutationAppliedError.from_dict(data)

            return response_409_type_1
            raise ValueError("Invalid value for response_409")

        response_409 = _parse_response_409(response.json())

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

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Error | MutationAppliedError | KeyView]:
    return Response(
        status_code=HTTPStatus(response.status_code)
        if response.status_code in HTTPStatus._value2member_map_
        else response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateKeyReq,
    if_match: str | Unset = UNSET,
) -> Response[Error | Error | MutationAppliedError | KeyView]:
    """Enable/disable a key or rebind its group. Optional `If-Match` for optimistic concurrency

    Args:
        id (str):
        if_match (str | Unset):
        body (UpdateKeyReq): Partial update to an existing key. Keys are PURE AUTH (1.5.0), so the
            mutable surface is
            auth-shaped only. Every field is optional; only the present ones change. The credential,
            name,
            allowed-pools, and labels are immutable here (rotate/recreate for those).

            `group` is THREE-STATE via serde double-option (`Option<Option<String>>`):
            - absent (`#[serde(default)]` -> outer `None`): leave the binding unchanged.
            - JSON `null` (`Some(None)`): UNBIND to no group (authed + unlimited).
            - a value (`Some(Some(name))`): REBIND to that group (must exist; mint-parity check).

            A single `Option<T>` could not tell absent from present-null, so a binding could never be
            cleared once set. `enabled` is a plain `Option<bool>` (a bool has no clear state). The
            1.4.x
            cap fields (`rpm_limit`/`tpm_limit`/`max_budget_cents`) are GONE: limits live on the
            group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Error | MutationAppliedError | KeyView]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        if_match=if_match,
    )

    response = client._request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateKeyReq,
    if_match: str | Unset = UNSET,
) -> Error | Error | MutationAppliedError | KeyView | None:
    """Enable/disable a key or rebind its group. Optional `If-Match` for optimistic concurrency

    Args:
        id (str):
        if_match (str | Unset):
        body (UpdateKeyReq): Partial update to an existing key. Keys are PURE AUTH (1.5.0), so the
            mutable surface is
            auth-shaped only. Every field is optional; only the present ones change. The credential,
            name,
            allowed-pools, and labels are immutable here (rotate/recreate for those).

            `group` is THREE-STATE via serde double-option (`Option<Option<String>>`):
            - absent (`#[serde(default)]` -> outer `None`): leave the binding unchanged.
            - JSON `null` (`Some(None)`): UNBIND to no group (authed + unlimited).
            - a value (`Some(Some(name))`): REBIND to that group (must exist; mint-parity check).

            A single `Option<T>` could not tell absent from present-null, so a binding could never be
            cleared once set. `enabled` is a plain `Option<bool>` (a bool has no clear state). The
            1.4.x
            cap fields (`rpm_limit`/`tpm_limit`/`max_budget_cents`) are GONE: limits live on the
            group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Error | MutationAppliedError | KeyView
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateKeyReq,
    if_match: str | Unset = UNSET,
) -> Response[Error | Error | MutationAppliedError | KeyView]:
    """Enable/disable a key or rebind its group. Optional `If-Match` for optimistic concurrency

    Args:
        id (str):
        if_match (str | Unset):
        body (UpdateKeyReq): Partial update to an existing key. Keys are PURE AUTH (1.5.0), so the
            mutable surface is
            auth-shaped only. Every field is optional; only the present ones change. The credential,
            name,
            allowed-pools, and labels are immutable here (rotate/recreate for those).

            `group` is THREE-STATE via serde double-option (`Option<Option<String>>`):
            - absent (`#[serde(default)]` -> outer `None`): leave the binding unchanged.
            - JSON `null` (`Some(None)`): UNBIND to no group (authed + unlimited).
            - a value (`Some(Some(name))`): REBIND to that group (must exist; mint-parity check).

            A single `Option<T>` could not tell absent from present-null, so a binding could never be
            cleared once set. `enabled` is a plain `Option<bool>` (a bool has no clear state). The
            1.4.x
            cap fields (`rpm_limit`/`tpm_limit`/`max_budget_cents`) are GONE: limits live on the
            group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Error | MutationAppliedError | KeyView]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        if_match=if_match,
    )

    response = await client._async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateKeyReq,
    if_match: str | Unset = UNSET,
) -> Error | Error | MutationAppliedError | KeyView | None:
    """Enable/disable a key or rebind its group. Optional `If-Match` for optimistic concurrency

    Args:
        id (str):
        if_match (str | Unset):
        body (UpdateKeyReq): Partial update to an existing key. Keys are PURE AUTH (1.5.0), so the
            mutable surface is
            auth-shaped only. Every field is optional; only the present ones change. The credential,
            name,
            allowed-pools, and labels are immutable here (rotate/recreate for those).

            `group` is THREE-STATE via serde double-option (`Option<Option<String>>`):
            - absent (`#[serde(default)]` -> outer `None`): leave the binding unchanged.
            - JSON `null` (`Some(None)`): UNBIND to no group (authed + unlimited).
            - a value (`Some(Some(name))`): REBIND to that group (must exist; mint-parity check).

            A single `Option<T>` could not tell absent from present-null, so a binding could never be
            cleared once set. `enabled` is a plain `Option<bool>` (a bool has no clear state). The
            1.4.x
            cap fields (`rpm_limit`/`tpm_limit`/`max_budget_cents`) are GONE: limits live on the
            group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Error | MutationAppliedError | KeyView
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            if_match=if_match,
        )
    ).parsed
