from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.install_plugin_req import InstallPluginReq
from ...models.plugin_install_view import PluginInstallView
from ...types import Response


def _get_kwargs(
    *,
    body: InstallPluginReq,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/admin/plugins",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | PluginInstallView | None:
    if response.status_code == 201:
        response_201 = PluginInstallView.from_dict(response.json())

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
) -> Response[Error | PluginInstallView]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: InstallPluginReq,
) -> Response[Error | PluginInstallView]:
    """Install a dynamic-library store plugin: upload the library (base64) + optional signed manifest; the
    engine RE-VERIFIES against the running trust posture, validates the store ABI, and writes it
    atomically into the plugins directory. Takes effect on the next store (re)load

    Args:
        body (InstallPluginReq): The `POST /api/v1/admin/plugins` request body: install a SIGNED
            plugin tarball. The tarball
            bytes ride as base64 (`tarball_b64`) — a plugin artifact is opaque binary, so base64 keeps
            it a
            clean JSON field. The engine RE-VERIFIES the contained signed manifest server-side against
            the
            running `plugins.*` trust posture (the client is never trusted). `file` is the bare
            `.tar.gz`
            filename to store it under (storage only — identity comes from the signed manifest
            inside).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PluginInstallView]
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
    body: InstallPluginReq,
) -> Error | PluginInstallView | None:
    """Install a dynamic-library store plugin: upload the library (base64) + optional signed manifest; the
    engine RE-VERIFIES against the running trust posture, validates the store ABI, and writes it
    atomically into the plugins directory. Takes effect on the next store (re)load

    Args:
        body (InstallPluginReq): The `POST /api/v1/admin/plugins` request body: install a SIGNED
            plugin tarball. The tarball
            bytes ride as base64 (`tarball_b64`) — a plugin artifact is opaque binary, so base64 keeps
            it a
            clean JSON field. The engine RE-VERIFIES the contained signed manifest server-side against
            the
            running `plugins.*` trust posture (the client is never trusted). `file` is the bare
            `.tar.gz`
            filename to store it under (storage only — identity comes from the signed manifest
            inside).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PluginInstallView
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: InstallPluginReq,
) -> Response[Error | PluginInstallView]:
    """Install a dynamic-library store plugin: upload the library (base64) + optional signed manifest; the
    engine RE-VERIFIES against the running trust posture, validates the store ABI, and writes it
    atomically into the plugins directory. Takes effect on the next store (re)load

    Args:
        body (InstallPluginReq): The `POST /api/v1/admin/plugins` request body: install a SIGNED
            plugin tarball. The tarball
            bytes ride as base64 (`tarball_b64`) — a plugin artifact is opaque binary, so base64 keeps
            it a
            clean JSON field. The engine RE-VERIFIES the contained signed manifest server-side against
            the
            running `plugins.*` trust posture (the client is never trusted). `file` is the bare
            `.tar.gz`
            filename to store it under (storage only — identity comes from the signed manifest
            inside).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PluginInstallView]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: InstallPluginReq,
) -> Error | PluginInstallView | None:
    """Install a dynamic-library store plugin: upload the library (base64) + optional signed manifest; the
    engine RE-VERIFIES against the running trust posture, validates the store ABI, and writes it
    atomically into the plugins directory. Takes effect on the next store (re)load

    Args:
        body (InstallPluginReq): The `POST /api/v1/admin/plugins` request body: install a SIGNED
            plugin tarball. The tarball
            bytes ride as base64 (`tarball_b64`) — a plugin artifact is opaque binary, so base64 keeps
            it a
            clean JSON field. The engine RE-VERIFIES the contained signed manifest server-side against
            the
            running `plugins.*` trust posture (the client is never trusted). `file` is the bare
            `.tar.gz`
            filename to store it under (storage only — identity comes from the signed manifest
            inside).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PluginInstallView
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
