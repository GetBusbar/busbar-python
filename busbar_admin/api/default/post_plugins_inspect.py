from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.inspect_plugin_req import InspectPluginReq
from ...models.plugin_schema_view import PluginSchemaView
from ...types import Response


def _get_kwargs(
    *,
    body: InspectPluginReq,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/admin/plugins/inspect",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
) -> Response[Error | PluginSchemaView]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: InspectPluginReq,
) -> Response[Error | PluginSchemaView]:
    """Stateless read-only preview of a candidate plugin tarball: verify its signature, parse its manifest,
    and report its settings schema WITHOUT installing anything

    Args:
        body (InspectPluginReq): `POST /api/v1/admin/plugins/inspect` request body. SAME shape as
            [`InstallPluginReq`]; `file`
            is accepted for shape parity with the install flow a UI composes around the same upload,
            but is
            otherwise UNUSED here: inspect never writes anything to disk, so there is no filename to
            bind
            an install would need.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PluginSchemaView]
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
    body: InspectPluginReq,
) -> Error | PluginSchemaView | None:
    """Stateless read-only preview of a candidate plugin tarball: verify its signature, parse its manifest,
    and report its settings schema WITHOUT installing anything

    Args:
        body (InspectPluginReq): `POST /api/v1/admin/plugins/inspect` request body. SAME shape as
            [`InstallPluginReq`]; `file`
            is accepted for shape parity with the install flow a UI composes around the same upload,
            but is
            otherwise UNUSED here: inspect never writes anything to disk, so there is no filename to
            bind
            an install would need.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PluginSchemaView
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: InspectPluginReq,
) -> Response[Error | PluginSchemaView]:
    """Stateless read-only preview of a candidate plugin tarball: verify its signature, parse its manifest,
    and report its settings schema WITHOUT installing anything

    Args:
        body (InspectPluginReq): `POST /api/v1/admin/plugins/inspect` request body. SAME shape as
            [`InstallPluginReq`]; `file`
            is accepted for shape parity with the install flow a UI composes around the same upload,
            but is
            otherwise UNUSED here: inspect never writes anything to disk, so there is no filename to
            bind
            an install would need.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PluginSchemaView]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: InspectPluginReq,
) -> Error | PluginSchemaView | None:
    """Stateless read-only preview of a candidate plugin tarball: verify its signature, parse its manifest,
    and report its settings schema WITHOUT installing anything

    Args:
        body (InspectPluginReq): `POST /api/v1/admin/plugins/inspect` request body. SAME shape as
            [`InstallPluginReq`]; `file`
            is accepted for shape parity with the install flow a UI composes around the same upload,
            but is
            otherwise UNUSED here: inspect never writes anything to disk, so there is no filename to
            bind
            an install would need.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PluginSchemaView
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
