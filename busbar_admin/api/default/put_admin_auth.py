from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_auth_put_view import AdminAuthPutView
from ...models.error import Error
from ...models.put_auth_body import PutAuthBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PutAuthBody,
    if_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/admin/admin-auth",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AdminAuthPutView | Error | None:
    if response.status_code == 200:
        response_200 = AdminAuthPutView.from_dict(response.json())

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
) -> Response[AdminAuthPutView | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PutAuthBody,
    if_match: str | Unset = UNSET,
) -> Response[AdminAuthPutView | Error]:
    """Replace the admin_auth chain at runtime, dry-run guarded (the calling credentials must hold full
    scope under the NEW chain, else 409). Live until the next reload/restart

    Args:
        if_match (str | Unset):
        body (PutAuthBody): The `PUT /api/v1/admin/admin-auth` body: the replacement admin auth
            chain.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminAuthPutView | Error]
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
    body: PutAuthBody,
    if_match: str | Unset = UNSET,
) -> AdminAuthPutView | Error | None:
    """Replace the admin_auth chain at runtime, dry-run guarded (the calling credentials must hold full
    scope under the NEW chain, else 409). Live until the next reload/restart

    Args:
        if_match (str | Unset):
        body (PutAuthBody): The `PUT /api/v1/admin/admin-auth` body: the replacement admin auth
            chain.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminAuthPutView | Error
    """

    return sync_detailed(
        client=client,
        body=body,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PutAuthBody,
    if_match: str | Unset = UNSET,
) -> Response[AdminAuthPutView | Error]:
    """Replace the admin_auth chain at runtime, dry-run guarded (the calling credentials must hold full
    scope under the NEW chain, else 409). Live until the next reload/restart

    Args:
        if_match (str | Unset):
        body (PutAuthBody): The `PUT /api/v1/admin/admin-auth` body: the replacement admin auth
            chain.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminAuthPutView | Error]
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
    body: PutAuthBody,
    if_match: str | Unset = UNSET,
) -> AdminAuthPutView | Error | None:
    """Replace the admin_auth chain at runtime, dry-run guarded (the calling credentials must hold full
    scope under the NEW chain, else 409). Live until the next reload/restart

    Args:
        if_match (str | Unset):
        body (PutAuthBody): The `PUT /api/v1/admin/admin-auth` body: the replacement admin auth
            chain.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminAuthPutView | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            if_match=if_match,
        )
    ).parsed
