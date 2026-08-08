from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.restart_req import RestartReq
from ...models.restart_view import RestartView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RestartReq | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/admin/restart",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | RestartView | None:
    if response.status_code == 202:
        response_202 = RestartView.from_dict(response.json())

        return response_202

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | RestartView]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RestartReq | Unset = UNSET,
) -> Response[Error | RestartView]:
    """Restart busbar to apply the restart-scoped settings (listen, admin_listen, tls, admin_tls,
    admin_require_mtls, store). Drains first; the supervisor brings it back

    Args:
        body (RestartReq | Unset): The `POST /api/v1/admin/restart` body. Absent is the same as
            `{}`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RestartView]
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
    body: RestartReq | Unset = UNSET,
) -> Error | RestartView | None:
    """Restart busbar to apply the restart-scoped settings (listen, admin_listen, tls, admin_tls,
    admin_require_mtls, store). Drains first; the supervisor brings it back

    Args:
        body (RestartReq | Unset): The `POST /api/v1/admin/restart` body. Absent is the same as
            `{}`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RestartView
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RestartReq | Unset = UNSET,
) -> Response[Error | RestartView]:
    """Restart busbar to apply the restart-scoped settings (listen, admin_listen, tls, admin_tls,
    admin_require_mtls, store). Drains first; the supervisor brings it back

    Args:
        body (RestartReq | Unset): The `POST /api/v1/admin/restart` body. Absent is the same as
            `{}`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RestartView]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RestartReq | Unset = UNSET,
) -> Error | RestartView | None:
    """Restart busbar to apply the restart-scoped settings (listen, admin_listen, tls, admin_tls,
    admin_require_mtls, store). Drains first; the supervisor brings it back

    Args:
        body (RestartReq | Unset): The `POST /api/v1/admin/restart` body. Absent is the same as
            `{}`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RestartView
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
