from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.plugin_schema_view import PluginSchemaView
from ...types import Response


def _get_kwargs(
    file: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/admin/plugins/{file}/schema".format(
            file=quote(str(file), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | PluginSchemaView | None:
    if response.status_code == 200:
        response_200 = PluginSchemaView.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

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
    file: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error | PluginSchemaView]:
    """The plugin's self-described settings JSON Schema, read from the SIGNED manifest's `settings_schema`
    field, which works for every plugin kind (store/secret/auth/hook), not just hooks. `hook` plugins
    keep the live describe-proxy behavior when describe answers (source: describe); a loaded hook whose
    describe answers null falls back server-side to the manifest baseline (source: manifest)

    Args:
        file (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PluginSchemaView]
    """

    kwargs = _get_kwargs(
        file=file,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    file: str,
    *,
    client: AuthenticatedClient,
) -> Error | PluginSchemaView | None:
    """The plugin's self-described settings JSON Schema, read from the SIGNED manifest's `settings_schema`
    field, which works for every plugin kind (store/secret/auth/hook), not just hooks. `hook` plugins
    keep the live describe-proxy behavior when describe answers (source: describe); a loaded hook whose
    describe answers null falls back server-side to the manifest baseline (source: manifest)

    Args:
        file (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PluginSchemaView
    """

    return sync_detailed(
        file=file,
        client=client,
    ).parsed


async def asyncio_detailed(
    file: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error | PluginSchemaView]:
    """The plugin's self-described settings JSON Schema, read from the SIGNED manifest's `settings_schema`
    field, which works for every plugin kind (store/secret/auth/hook), not just hooks. `hook` plugins
    keep the live describe-proxy behavior when describe answers (source: describe); a loaded hook whose
    describe answers null falls back server-side to the manifest baseline (source: manifest)

    Args:
        file (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PluginSchemaView]
    """

    kwargs = _get_kwargs(
        file=file,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    file: str,
    *,
    client: AuthenticatedClient,
) -> Error | PluginSchemaView | None:
    """The plugin's self-described settings JSON Schema, read from the SIGNED manifest's `settings_schema`
    field, which works for every plugin kind (store/secret/auth/hook), not just hooks. `hook` plugins
    keep the live describe-proxy behavior when describe answers (source: describe); a loaded hook whose
    describe answers null falls back server-side to the manifest baseline (source: manifest)

    Args:
        file (str):

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
        )
    ).parsed
