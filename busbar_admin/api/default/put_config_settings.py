from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.config_document_mutation_view import ConfigDocumentMutationView
from ...models.config_settings_view import ConfigSettingsView
from ...models.error import Error
from ...models.put_config_settings_config_document_modification import PutConfigSettingsConfigDocumentModification
from ...models.put_config_settings_config_settings_replacement import PutConfigSettingsConfigSettingsReplacement
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PutConfigSettingsConfigDocumentModification | PutConfigSettingsConfigSettingsReplacement,
    if_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/admin/config/settings",
    }

    if isinstance(body, PutConfigSettingsConfigSettingsReplacement):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConfigDocumentMutationView | ConfigSettingsView | Error | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> ConfigDocumentMutationView | ConfigSettingsView:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_config_settings_mutation_view_type_0 = ConfigSettingsView.from_dict(data)

                return componentsschemas_config_settings_mutation_view_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_config_settings_mutation_view_type_1 = ConfigDocumentMutationView.from_dict(data)

            return componentsschemas_config_settings_mutation_view_type_1
            raise ValueError("Invalid value for response_200")

        response_200 = _parse_response_200(response.json())

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
) -> Response[ConfigDocumentMutationView | ConfigSettingsView | Error]:
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
    body: PutConfigSettingsConfigDocumentModification | PutConfigSettingsConfigSettingsReplacement,
    if_match: str | Unset = UNSET,
) -> Response[ConfigDocumentMutationView | ConfigSettingsView | Error]:
    """SET any single-value config section durably (1.5.0 full-config coverage): partial RootSettings
    merged onto the overlay, re-resolved + validated, swapped in.
    rate_card/per_request_fee/security/limits/… go live;
    listen/tls/admin_listen/admin_tls/admin_require_mtls/store are stored + flagged restart-to-apply
    (bound once at start / store reused across a hot reload). NEVER writes config.yaml

    Args:
        if_match (str | Unset):
        body (PutConfigSettingsConfigDocumentModification |
            PutConfigSettingsConfigSettingsReplacement):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfigDocumentMutationView | ConfigSettingsView | Error]
    """

    kwargs = _get_kwargs(
        body=body,
        if_match=if_match,
    )

    response = client._request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PutConfigSettingsConfigDocumentModification | PutConfigSettingsConfigSettingsReplacement,
    if_match: str | Unset = UNSET,
) -> ConfigDocumentMutationView | ConfigSettingsView | Error | None:
    """SET any single-value config section durably (1.5.0 full-config coverage): partial RootSettings
    merged onto the overlay, re-resolved + validated, swapped in.
    rate_card/per_request_fee/security/limits/… go live;
    listen/tls/admin_listen/admin_tls/admin_require_mtls/store are stored + flagged restart-to-apply
    (bound once at start / store reused across a hot reload). NEVER writes config.yaml

    Args:
        if_match (str | Unset):
        body (PutConfigSettingsConfigDocumentModification |
            PutConfigSettingsConfigSettingsReplacement):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfigDocumentMutationView | ConfigSettingsView | Error
    """

    return sync_detailed(
        client=client,
        body=body,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PutConfigSettingsConfigDocumentModification | PutConfigSettingsConfigSettingsReplacement,
    if_match: str | Unset = UNSET,
) -> Response[ConfigDocumentMutationView | ConfigSettingsView | Error]:
    """SET any single-value config section durably (1.5.0 full-config coverage): partial RootSettings
    merged onto the overlay, re-resolved + validated, swapped in.
    rate_card/per_request_fee/security/limits/… go live;
    listen/tls/admin_listen/admin_tls/admin_require_mtls/store are stored + flagged restart-to-apply
    (bound once at start / store reused across a hot reload). NEVER writes config.yaml

    Args:
        if_match (str | Unset):
        body (PutConfigSettingsConfigDocumentModification |
            PutConfigSettingsConfigSettingsReplacement):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfigDocumentMutationView | ConfigSettingsView | Error]
    """

    kwargs = _get_kwargs(
        body=body,
        if_match=if_match,
    )

    response = await client._async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PutConfigSettingsConfigDocumentModification | PutConfigSettingsConfigSettingsReplacement,
    if_match: str | Unset = UNSET,
) -> ConfigDocumentMutationView | ConfigSettingsView | Error | None:
    """SET any single-value config section durably (1.5.0 full-config coverage): partial RootSettings
    merged onto the overlay, re-resolved + validated, swapped in.
    rate_card/per_request_fee/security/limits/… go live;
    listen/tls/admin_listen/admin_tls/admin_require_mtls/store are stored + flagged restart-to-apply
    (bound once at start / store reused across a hot reload). NEVER writes config.yaml

    Args:
        if_match (str | Unset):
        body (PutConfigSettingsConfigDocumentModification |
            PutConfigSettingsConfigSettingsReplacement):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfigDocumentMutationView | ConfigSettingsView | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            if_match=if_match,
        )
    ).parsed
