from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audit_page_view import AuditPageView
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    action: str | Unset = UNSET,
    resource: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["action"] = action

    params["resource"] = resource

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/admin/audit",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AuditPageView | Error | None:
    if response.status_code == 200:
        response_200 = AuditPageView.from_dict(response.json())

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


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AuditPageView | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    action: str | Unset = UNSET,
    resource: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[AuditPageView | Error]:
    """Admin audit log — every mutation with its outcome (newest first). Page: ?limit=, ?cursor=; returns
    {items, next_cursor}

    Args:
        action (str | Unset):
        resource (str | Unset):
        limit (str | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditPageView | Error]
    """

    kwargs = _get_kwargs(
        action=action,
        resource=resource,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    action: str | Unset = UNSET,
    resource: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> AuditPageView | Error | None:
    """Admin audit log — every mutation with its outcome (newest first). Page: ?limit=, ?cursor=; returns
    {items, next_cursor}

    Args:
        action (str | Unset):
        resource (str | Unset):
        limit (str | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditPageView | Error
    """

    return sync_detailed(
        client=client,
        action=action,
        resource=resource,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    action: str | Unset = UNSET,
    resource: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[AuditPageView | Error]:
    """Admin audit log — every mutation with its outcome (newest first). Page: ?limit=, ?cursor=; returns
    {items, next_cursor}

    Args:
        action (str | Unset):
        resource (str | Unset):
        limit (str | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditPageView | Error]
    """

    kwargs = _get_kwargs(
        action=action,
        resource=resource,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    action: str | Unset = UNSET,
    resource: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> AuditPageView | Error | None:
    """Admin audit log — every mutation with its outcome (newest first). Page: ?limit=, ?cursor=; returns
    {items, next_cursor}

    Args:
        action (str | Unset):
        resource (str | Unset):
        limit (str | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditPageView | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            resource=resource,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
