from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.config_version_detail_view import ConfigVersionDetailView
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    v: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/admin/config/versions/{v}".format(
            v=quote(str(v), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConfigVersionDetailView | Error | None:
    if response.status_code == 200:
        response_200 = ConfigVersionDetailView.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ConfigVersionDetailView | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    v: int,
    *,
    client: AuthenticatedClient,
) -> Response[ConfigVersionDetailView | Error]:
    """One retained config version, with its hook-surface snapshot

    Args:
        v (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfigVersionDetailView | Error]
    """

    kwargs = _get_kwargs(
        v=v,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    v: int,
    *,
    client: AuthenticatedClient,
) -> ConfigVersionDetailView | Error | None:
    """One retained config version, with its hook-surface snapshot

    Args:
        v (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfigVersionDetailView | Error
    """

    return sync_detailed(
        v=v,
        client=client,
    ).parsed


async def asyncio_detailed(
    v: int,
    *,
    client: AuthenticatedClient,
) -> Response[ConfigVersionDetailView | Error]:
    """One retained config version, with its hook-surface snapshot

    Args:
        v (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfigVersionDetailView | Error]
    """

    kwargs = _get_kwargs(
        v=v,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    v: int,
    *,
    client: AuthenticatedClient,
) -> ConfigVersionDetailView | Error | None:
    """One retained config version, with its hook-surface snapshot

    Args:
        v (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfigVersionDetailView | Error
    """

    return (
        await asyncio_detailed(
            v=v,
            client=client,
        )
    ).parsed
