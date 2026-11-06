from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.list_request import ListRequest
from ...models.list_view import ListView
from ...types import Response


def _get_kwargs(
    *,
    body: ListRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/admin/ledger/recovery/list",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListView:
    if response.status_code == 200:
        response_200 = ListView.from_dict(response.json())

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

    if response.status_code == 413:
        response_413 = Error.from_dict(response.json())

        return response_413

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())

        return response_503

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListView]:
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
    body: ListRequest,
) -> Response[Error | ListView]:
    """Inspect retained raw ledger operations requiring recovery

     An observation-only POST requiring full scope and the ordinary CRUD budget. The opaque cursor
    belongs to this list; default limit 200, maximum 1000. Rows contain immutable operation identities
    and recovery versions, never raw bodies or mutable dollar balances. Listing does not grant
    resolution authority; can_resolve describes only this node's current authority.

    Args:
        body (ListRequest): The bounded observation request. The cursor belongs only to this
            surface.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListView]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client._request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ListRequest,
) -> Error | ListView | None:
    """Inspect retained raw ledger operations requiring recovery

     An observation-only POST requiring full scope and the ordinary CRUD budget. The opaque cursor
    belongs to this list; default limit 200, maximum 1000. Rows contain immutable operation identities
    and recovery versions, never raw bodies or mutable dollar balances. Listing does not grant
    resolution authority; can_resolve describes only this node's current authority.

    Args:
        body (ListRequest): The bounded observation request. The cursor belongs only to this
            surface.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListView
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ListRequest,
) -> Response[Error | ListView]:
    """Inspect retained raw ledger operations requiring recovery

     An observation-only POST requiring full scope and the ordinary CRUD budget. The opaque cursor
    belongs to this list; default limit 200, maximum 1000. Rows contain immutable operation identities
    and recovery versions, never raw bodies or mutable dollar balances. Listing does not grant
    resolution authority; can_resolve describes only this node's current authority.

    Args:
        body (ListRequest): The bounded observation request. The cursor belongs only to this
            surface.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListView]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client._async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ListRequest,
) -> Error | ListView | None:
    """Inspect retained raw ledger operations requiring recovery

     An observation-only POST requiring full scope and the ordinary CRUD budget. The opaque cursor
    belongs to this list; default limit 200, maximum 1000. Rows contain immutable operation identities
    and recovery versions, never raw bodies or mutable dollar balances. Listing does not grant
    resolution authority; can_resolve describes only this node's current authority.

    Args:
        body (ListRequest): The bounded observation request. The cursor belongs only to this
            surface.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListView
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
