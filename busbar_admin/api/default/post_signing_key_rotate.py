from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.signing_key_rotate_view import SigningKeyRotateView
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/admin/signing-key/rotate",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | SigningKeyRotateView | None:
    if response.status_code == 200:
        response_200 = SigningKeyRotateView.from_dict(response.json())

        return response_200

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
) -> Response[Error | SigningKeyRotateView]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Error | SigningKeyRotateView]:
    """ROTATE the busbar key-signing key (S2). Rotation is REVOKE-ALL by design: a new signing key means
    every token minted under the OLD key stops verifying, so every outstanding key must be re-minted.
    1.5.0 is single-key, so this reports the intent + current kid; the actual swap is an operator action
    (replace auth.signing_key / the persisted key file and restart/reload every node in lockstep)
    (1.5.0)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SigningKeyRotateView]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Error | SigningKeyRotateView | None:
    """ROTATE the busbar key-signing key (S2). Rotation is REVOKE-ALL by design: a new signing key means
    every token minted under the OLD key stops verifying, so every outstanding key must be re-minted.
    1.5.0 is single-key, so this reports the intent + current kid; the actual swap is an operator action
    (replace auth.signing_key / the persisted key file and restart/reload every node in lockstep)
    (1.5.0)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SigningKeyRotateView
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Error | SigningKeyRotateView]:
    """ROTATE the busbar key-signing key (S2). Rotation is REVOKE-ALL by design: a new signing key means
    every token minted under the OLD key stops verifying, so every outstanding key must be re-minted.
    1.5.0 is single-key, so this reports the intent + current kid; the actual swap is an operator action
    (replace auth.signing_key / the persisted key file and restart/reload every node in lockstep)
    (1.5.0)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SigningKeyRotateView]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Error | SigningKeyRotateView | None:
    """ROTATE the busbar key-signing key (S2). Rotation is REVOKE-ALL by design: a new signing key means
    every token minted under the OLD key stops verifying, so every outstanding key must be re-minted.
    1.5.0 is single-key, so this reports the intent + current kid; the actual swap is an operator action
    (replace auth.signing_key / the persisted key file and restart/reload every node in lockstep)
    (1.5.0)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SigningKeyRotateView
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
