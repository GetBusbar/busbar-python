from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.trust_list_view import TrustListView
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/admin/trust",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | TrustListView:
    if response.status_code == 200:
        response_200 = TrustListView.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 413:
        response_413 = Error.from_dict(response.json())

        return response_413

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())

        return response_503

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | TrustListView]:
    return Response(
        status_code=HTTPStatus(response.status_code)
        if response.status_code in HTTPStatus._value2member_map_
        else response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Error | TrustListView]:
    """Every trust key of the kernel's trust book and its state

     The counterparties every plane instance this node serves declares, and the items sighted or approved
    at each: its key, state, what it is approved at and what it was last sighted at. A read: it mutates
    nothing and needs `read-only`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TrustListView]
    """

    kwargs = _get_kwargs()

    response = client._request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Error | TrustListView | None:
    """Every trust key of the kernel's trust book and its state

     The counterparties every plane instance this node serves declares, and the items sighted or approved
    at each: its key, state, what it is approved at and what it was last sighted at. A read: it mutates
    nothing and needs `read-only`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TrustListView
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Error | TrustListView]:
    """Every trust key of the kernel's trust book and its state

     The counterparties every plane instance this node serves declares, and the items sighted or approved
    at each: its key, state, what it is approved at and what it was last sighted at. A read: it mutates
    nothing and needs `read-only`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TrustListView]
    """

    kwargs = _get_kwargs()

    response = await client._async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Error | TrustListView | None:
    """Every trust key of the kernel's trust book and its state

     The counterparties every plane instance this node serves declares, and the items sighted or approved
    at each: its key, state, what it is approved at and what it was last sighted at. A read: it mutates
    nothing and needs `read-only`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TrustListView
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
