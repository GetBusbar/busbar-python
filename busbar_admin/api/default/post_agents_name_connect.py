from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.a2a_trust_view import A2ATrustView
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/admin/agents/{name}/connect".format(
            name=quote(str(name), safe="").replace(".", "%2E"),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> A2ATrustView | Error | None:
    if response.status_code == 200:
        response_200 = A2ATrustView.from_dict(response.json())

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
) -> Response[A2ATrustView | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code)
        if response.status_code in HTTPStatus._value2member_map_
        else response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
) -> Response[A2ATrustView | Error]:
    """Fetch a registered agent's card, verify it against the operator's out-of-band root, and report the
    fingerprint. Approves nothing; the card it verified is recorded as the agent's card records, which
    an instance opened again serves from

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[A2ATrustView | Error]
    """

    kwargs = _get_kwargs(
        name=name,
    )

    response = client._request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient,
) -> A2ATrustView | Error | None:
    """Fetch a registered agent's card, verify it against the operator's out-of-band root, and report the
    fingerprint. Approves nothing; the card it verified is recorded as the agent's card records, which
    an instance opened again serves from

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        A2ATrustView | Error
    """

    return sync_detailed(
        name=name,
        client=client,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
) -> Response[A2ATrustView | Error]:
    """Fetch a registered agent's card, verify it against the operator's out-of-band root, and report the
    fingerprint. Approves nothing; the card it verified is recorded as the agent's card records, which
    an instance opened again serves from

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[A2ATrustView | Error]
    """

    kwargs = _get_kwargs(
        name=name,
    )

    response = await client._async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient,
) -> A2ATrustView | Error | None:
    """Fetch a registered agent's card, verify it against the operator's out-of-band root, and report the
    fingerprint. Approves nothing; the card it verified is recorded as the agent's card records, which
    an instance opened again serves from

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        A2ATrustView | Error
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
        )
    ).parsed
