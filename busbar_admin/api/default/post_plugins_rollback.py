from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.plugin_rollback_req import PluginRollbackReq
from ...models.plugin_rollback_view import PluginRollbackView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PluginRollbackReq,
    if_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/admin/plugins/rollback",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | PluginRollbackView | None:
    if response.status_code == 200:
        response_200 = PluginRollbackView.from_dict(response.json())

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
) -> Response[Error | PluginRollbackView]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PluginRollbackReq,
    if_match: str | Unset = UNSET,
) -> Response[Error | PluginRollbackView]:
    """EXPLICIT, authenticated, audited rollback of a plugin to a PRIOR version (1.5.0). Validates the
    target artifact (structure + trust) with the anti-downgrade floor lowered to EXACTLY the target's
    own version — a lower or untrusted artifact still fails (a rollback authenticates the OPERATOR,
    never the bytes). Persists the version pin to the overlay (survives restart) and hot-swaps via the
    same rebuild-and-swap path as plugins/reload

    Args:
        if_match (str | Unset):
        body (PluginRollbackReq): The `POST /api/v1/admin/plugins/rollback` body: the target
            library FILENAME to roll DOWN to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PluginRollbackView]
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
    body: PluginRollbackReq,
    if_match: str | Unset = UNSET,
) -> Error | PluginRollbackView | None:
    """EXPLICIT, authenticated, audited rollback of a plugin to a PRIOR version (1.5.0). Validates the
    target artifact (structure + trust) with the anti-downgrade floor lowered to EXACTLY the target's
    own version — a lower or untrusted artifact still fails (a rollback authenticates the OPERATOR,
    never the bytes). Persists the version pin to the overlay (survives restart) and hot-swaps via the
    same rebuild-and-swap path as plugins/reload

    Args:
        if_match (str | Unset):
        body (PluginRollbackReq): The `POST /api/v1/admin/plugins/rollback` body: the target
            library FILENAME to roll DOWN to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PluginRollbackView
    """

    return sync_detailed(
        client=client,
        body=body,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PluginRollbackReq,
    if_match: str | Unset = UNSET,
) -> Response[Error | PluginRollbackView]:
    """EXPLICIT, authenticated, audited rollback of a plugin to a PRIOR version (1.5.0). Validates the
    target artifact (structure + trust) with the anti-downgrade floor lowered to EXACTLY the target's
    own version — a lower or untrusted artifact still fails (a rollback authenticates the OPERATOR,
    never the bytes). Persists the version pin to the overlay (survives restart) and hot-swaps via the
    same rebuild-and-swap path as plugins/reload

    Args:
        if_match (str | Unset):
        body (PluginRollbackReq): The `POST /api/v1/admin/plugins/rollback` body: the target
            library FILENAME to roll DOWN to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PluginRollbackView]
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
    body: PluginRollbackReq,
    if_match: str | Unset = UNSET,
) -> Error | PluginRollbackView | None:
    """EXPLICIT, authenticated, audited rollback of a plugin to a PRIOR version (1.5.0). Validates the
    target artifact (structure + trust) with the anti-downgrade floor lowered to EXACTLY the target's
    own version — a lower or untrusted artifact still fails (a rollback authenticates the OPERATOR,
    never the bytes). Persists the version pin to the overlay (survives restart) and hot-swaps via the
    same rebuild-and-swap path as plugins/reload

    Args:
        if_match (str | Unset):
        body (PluginRollbackReq): The `POST /api/v1/admin/plugins/rollback` body: the target
            library FILENAME to roll DOWN to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PluginRollbackView
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            if_match=if_match,
        )
    ).parsed
