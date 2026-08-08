from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.config_settings_view import ConfigSettingsView
from ...models.error import Error
from ...models.put_config_settings_body import PutConfigSettingsBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PutConfigSettingsBody,
    if_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/admin/config/settings",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConfigSettingsView | Error | None:
    if response.status_code == 200:
        response_200 = ConfigSettingsView.from_dict(response.json())

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
) -> Response[ConfigSettingsView | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PutConfigSettingsBody,
    if_match: str | Unset = UNSET,
) -> Response[ConfigSettingsView | Error]:
    """SET any single-value config section durably (1.5.0 full-config coverage): partial RootSettings
    merged onto the overlay, re-resolved + validated, swapped in.
    rate_card/per_request_fee/security/limits/… go live;
    listen/tls/admin_listen/admin_tls/admin_require_mtls/store are stored + flagged restart-to-apply
    (bound once at start / store reused across a hot reload). NEVER writes config.yaml

    Args:
        if_match (str | Unset):
        body (PutConfigSettingsBody): The settings sections to replace, keyed by section name.
            Durable by default (1.5.3): a mutable config always stores the change in its overlay
            (survives restart), and a locked config (`config.locked: true`) refuses ANY change with
            `400`. There is no "apply in memory only" outcome. The optional top-level boolean
            `persist` is accepted for back-compat and boolean-validated (a non-boolean is a 400 naming
            the field), but its value has NO effect: persistence is unconditional on a mutable config
            and refusal is unconditional on a locked one. Every other top-level key must be a known
            settings section; an unknown key is a 400. The accepted shape is the config file's own,
            documented in the configuration reference; it is not restated here because several of its
            types parse a wire shape that does not match their field layout.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfigSettingsView | Error]
    """

    kwargs = _get_kwargs(
        body=body,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PutConfigSettingsBody,
    if_match: str | Unset = UNSET,
) -> ConfigSettingsView | Error | None:
    """SET any single-value config section durably (1.5.0 full-config coverage): partial RootSettings
    merged onto the overlay, re-resolved + validated, swapped in.
    rate_card/per_request_fee/security/limits/… go live;
    listen/tls/admin_listen/admin_tls/admin_require_mtls/store are stored + flagged restart-to-apply
    (bound once at start / store reused across a hot reload). NEVER writes config.yaml

    Args:
        if_match (str | Unset):
        body (PutConfigSettingsBody): The settings sections to replace, keyed by section name.
            Durable by default (1.5.3): a mutable config always stores the change in its overlay
            (survives restart), and a locked config (`config.locked: true`) refuses ANY change with
            `400`. There is no "apply in memory only" outcome. The optional top-level boolean
            `persist` is accepted for back-compat and boolean-validated (a non-boolean is a 400 naming
            the field), but its value has NO effect: persistence is unconditional on a mutable config
            and refusal is unconditional on a locked one. Every other top-level key must be a known
            settings section; an unknown key is a 400. The accepted shape is the config file's own,
            documented in the configuration reference; it is not restated here because several of its
            types parse a wire shape that does not match their field layout.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfigSettingsView | Error
    """

    return sync_detailed(
        client=client,
        body=body,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PutConfigSettingsBody,
    if_match: str | Unset = UNSET,
) -> Response[ConfigSettingsView | Error]:
    """SET any single-value config section durably (1.5.0 full-config coverage): partial RootSettings
    merged onto the overlay, re-resolved + validated, swapped in.
    rate_card/per_request_fee/security/limits/… go live;
    listen/tls/admin_listen/admin_tls/admin_require_mtls/store are stored + flagged restart-to-apply
    (bound once at start / store reused across a hot reload). NEVER writes config.yaml

    Args:
        if_match (str | Unset):
        body (PutConfigSettingsBody): The settings sections to replace, keyed by section name.
            Durable by default (1.5.3): a mutable config always stores the change in its overlay
            (survives restart), and a locked config (`config.locked: true`) refuses ANY change with
            `400`. There is no "apply in memory only" outcome. The optional top-level boolean
            `persist` is accepted for back-compat and boolean-validated (a non-boolean is a 400 naming
            the field), but its value has NO effect: persistence is unconditional on a mutable config
            and refusal is unconditional on a locked one. Every other top-level key must be a known
            settings section; an unknown key is a 400. The accepted shape is the config file's own,
            documented in the configuration reference; it is not restated here because several of its
            types parse a wire shape that does not match their field layout.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfigSettingsView | Error]
    """

    kwargs = _get_kwargs(
        body=body,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PutConfigSettingsBody,
    if_match: str | Unset = UNSET,
) -> ConfigSettingsView | Error | None:
    """SET any single-value config section durably (1.5.0 full-config coverage): partial RootSettings
    merged onto the overlay, re-resolved + validated, swapped in.
    rate_card/per_request_fee/security/limits/… go live;
    listen/tls/admin_listen/admin_tls/admin_require_mtls/store are stored + flagged restart-to-apply
    (bound once at start / store reused across a hot reload). NEVER writes config.yaml

    Args:
        if_match (str | Unset):
        body (PutConfigSettingsBody): The settings sections to replace, keyed by section name.
            Durable by default (1.5.3): a mutable config always stores the change in its overlay
            (survives restart), and a locked config (`config.locked: true`) refuses ANY change with
            `400`. There is no "apply in memory only" outcome. The optional top-level boolean
            `persist` is accepted for back-compat and boolean-validated (a non-boolean is a 400 naming
            the field), but its value has NO effect: persistence is unconditional on a mutable config
            and refusal is unconditional on a locked one. Every other top-level key must be a known
            settings section; an unknown key is a 400. The accepted shape is the config file's own,
            documented in the configuration reference; it is not restated here because several of its
            types parse a wire shape that does not match their field layout.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfigSettingsView | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            if_match=if_match,
        )
    ).parsed
