from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_plugins_file_schema_source import GetPluginsFileSchemaSource
from ...models.plugin_schema_view import PluginSchemaView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    file: str,
    *,
    source: GetPluginsFileSchemaSource | Unset = UNSET,
    expected_archive_sha256: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_source: str | Unset = UNSET
    if not isinstance(source, Unset):
        json_source = source.value

    params["source"] = json_source

    params["expected_archive_sha256"] = expected_archive_sha256

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/admin/plugins/{file}/schema".format(
            file=quote(str(file), safe="").replace(".", "%2E"),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | PluginSchemaView | None:
    if response.status_code == 200:
        response_200 = PluginSchemaView.from_dict(response.json())

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
        response_409 = Error.from_dict(response.json())

        return response_409

    if response.status_code == 413:
        response_413 = Error.from_dict(response.json())

        return response_413

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
) -> Response[Error | PluginSchemaView]:
    return Response(
        status_code=HTTPStatus(response.status_code)
        if response.status_code in HTTPStatus._value2member_map_
        else response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    file: str,
    *,
    client: AuthenticatedClient,
    source: GetPluginsFileSchemaSource | Unset = UNSET,
    expected_archive_sha256: str | Unset = UNSET,
) -> Response[Error | PluginSchemaView]:
    """The plugin settings JSON Schema for every kind. source=installed_archive reads the named disk
    artifact, optionally fenced by expected_archive_sha256; it never substitutes a loaded generation.
    source=linked_statement reads a linked plane/transport declaration cached during startup. Without
    source, resolve the loaded module by name or alias, then the linked declaration cache. Canonical
    Statement first, legacy manifest field only when the Statement carries no schema. Dropped plugins
    are read from the signed manifest without opening the library; linked plugins publish their
    Statement. `hook` plugins keep the live describe-proxy behavior when describe answers (source:
    describe); a loaded hook whose describe answers null falls back server-side to the manifest baseline
    (source: manifest)

    Args:
        file (str):
        source (GetPluginsFileSchemaSource | Unset):
        expected_archive_sha256 (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PluginSchemaView]
    """

    kwargs = _get_kwargs(
        file=file,
        source=source,
        expected_archive_sha256=expected_archive_sha256,
    )

    response = client._request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    file: str,
    *,
    client: AuthenticatedClient,
    source: GetPluginsFileSchemaSource | Unset = UNSET,
    expected_archive_sha256: str | Unset = UNSET,
) -> Error | PluginSchemaView | None:
    """The plugin settings JSON Schema for every kind. source=installed_archive reads the named disk
    artifact, optionally fenced by expected_archive_sha256; it never substitutes a loaded generation.
    source=linked_statement reads a linked plane/transport declaration cached during startup. Without
    source, resolve the loaded module by name or alias, then the linked declaration cache. Canonical
    Statement first, legacy manifest field only when the Statement carries no schema. Dropped plugins
    are read from the signed manifest without opening the library; linked plugins publish their
    Statement. `hook` plugins keep the live describe-proxy behavior when describe answers (source:
    describe); a loaded hook whose describe answers null falls back server-side to the manifest baseline
    (source: manifest)

    Args:
        file (str):
        source (GetPluginsFileSchemaSource | Unset):
        expected_archive_sha256 (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PluginSchemaView
    """

    return sync_detailed(
        file=file,
        client=client,
        source=source,
        expected_archive_sha256=expected_archive_sha256,
    ).parsed


async def asyncio_detailed(
    file: str,
    *,
    client: AuthenticatedClient,
    source: GetPluginsFileSchemaSource | Unset = UNSET,
    expected_archive_sha256: str | Unset = UNSET,
) -> Response[Error | PluginSchemaView]:
    """The plugin settings JSON Schema for every kind. source=installed_archive reads the named disk
    artifact, optionally fenced by expected_archive_sha256; it never substitutes a loaded generation.
    source=linked_statement reads a linked plane/transport declaration cached during startup. Without
    source, resolve the loaded module by name or alias, then the linked declaration cache. Canonical
    Statement first, legacy manifest field only when the Statement carries no schema. Dropped plugins
    are read from the signed manifest without opening the library; linked plugins publish their
    Statement. `hook` plugins keep the live describe-proxy behavior when describe answers (source:
    describe); a loaded hook whose describe answers null falls back server-side to the manifest baseline
    (source: manifest)

    Args:
        file (str):
        source (GetPluginsFileSchemaSource | Unset):
        expected_archive_sha256 (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PluginSchemaView]
    """

    kwargs = _get_kwargs(
        file=file,
        source=source,
        expected_archive_sha256=expected_archive_sha256,
    )

    response = await client._async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    file: str,
    *,
    client: AuthenticatedClient,
    source: GetPluginsFileSchemaSource | Unset = UNSET,
    expected_archive_sha256: str | Unset = UNSET,
) -> Error | PluginSchemaView | None:
    """The plugin settings JSON Schema for every kind. source=installed_archive reads the named disk
    artifact, optionally fenced by expected_archive_sha256; it never substitutes a loaded generation.
    source=linked_statement reads a linked plane/transport declaration cached during startup. Without
    source, resolve the loaded module by name or alias, then the linked declaration cache. Canonical
    Statement first, legacy manifest field only when the Statement carries no schema. Dropped plugins
    are read from the signed manifest without opening the library; linked plugins publish their
    Statement. `hook` plugins keep the live describe-proxy behavior when describe answers (source:
    describe); a loaded hook whose describe answers null falls back server-side to the manifest baseline
    (source: manifest)

    Args:
        file (str):
        source (GetPluginsFileSchemaSource | Unset):
        expected_archive_sha256 (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PluginSchemaView
    """

    return (
        await asyncio_detailed(
            file=file,
            client=client,
            source=source,
            expected_archive_sha256=expected_archive_sha256,
        )
    ).parsed
