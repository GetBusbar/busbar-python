from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.key_page_view import KeyPageView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    enabled: str | Unset = UNSET,
    prefix: str | Unset = UNSET,
    group: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    include: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["enabled"] = enabled

    params["prefix"] = prefix

    params["group"] = group

    params["limit"] = limit

    params["cursor"] = cursor

    params["include"] = include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/admin/keys",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | KeyPageView | None:
    if response.status_code == 200:
        response_200 = KeyPageView.from_dict(response.json())

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

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | KeyPageView]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    enabled: str | Unset = UNSET,
    prefix: str | Unset = UNSET,
    group: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    include: str | Unset = UNSET,
) -> Response[Error | KeyPageView]:
    """List virtual keys (metadata only; never secrets). Filters: ?enabled=, ?prefix=, ?group= (keys bound
    to a group; a `user:<sub>` leaf's keys are one person's). Paginate: ?limit=, ?cursor= (opaque)

    Args:
        enabled (str | Unset):
        prefix (str | Unset):
        group (str | Unset):
        limit (str | Unset):
        cursor (str | Unset):
        include (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | KeyPageView]
    """

    kwargs = _get_kwargs(
        enabled=enabled,
        prefix=prefix,
        group=group,
        limit=limit,
        cursor=cursor,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    enabled: str | Unset = UNSET,
    prefix: str | Unset = UNSET,
    group: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    include: str | Unset = UNSET,
) -> Error | KeyPageView | None:
    """List virtual keys (metadata only; never secrets). Filters: ?enabled=, ?prefix=, ?group= (keys bound
    to a group; a `user:<sub>` leaf's keys are one person's). Paginate: ?limit=, ?cursor= (opaque)

    Args:
        enabled (str | Unset):
        prefix (str | Unset):
        group (str | Unset):
        limit (str | Unset):
        cursor (str | Unset):
        include (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | KeyPageView
    """

    return sync_detailed(
        client=client,
        enabled=enabled,
        prefix=prefix,
        group=group,
        limit=limit,
        cursor=cursor,
        include=include,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    enabled: str | Unset = UNSET,
    prefix: str | Unset = UNSET,
    group: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    include: str | Unset = UNSET,
) -> Response[Error | KeyPageView]:
    """List virtual keys (metadata only; never secrets). Filters: ?enabled=, ?prefix=, ?group= (keys bound
    to a group; a `user:<sub>` leaf's keys are one person's). Paginate: ?limit=, ?cursor= (opaque)

    Args:
        enabled (str | Unset):
        prefix (str | Unset):
        group (str | Unset):
        limit (str | Unset):
        cursor (str | Unset):
        include (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | KeyPageView]
    """

    kwargs = _get_kwargs(
        enabled=enabled,
        prefix=prefix,
        group=group,
        limit=limit,
        cursor=cursor,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    enabled: str | Unset = UNSET,
    prefix: str | Unset = UNSET,
    group: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    include: str | Unset = UNSET,
) -> Error | KeyPageView | None:
    """List virtual keys (metadata only; never secrets). Filters: ?enabled=, ?prefix=, ?group= (keys bound
    to a group; a `user:<sub>` leaf's keys are one person's). Paginate: ?limit=, ?cursor= (opaque)

    Args:
        enabled (str | Unset):
        prefix (str | Unset):
        group (str | Unset):
        limit (str | Unset):
        cursor (str | Unset):
        include (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | KeyPageView
    """

    return (
        await asyncio_detailed(
            client=client,
            enabled=enabled,
            prefix=prefix,
            group=group,
            limit=limit,
            cursor=cursor,
            include=include,
        )
    ).parsed
