from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.item_view import ItemView
from ...models.resolve_request import ResolveRequest
from ...types import Response


def _get_kwargs(
    *,
    body: ResolveRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/admin/ledger/recovery/resolve",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ItemView:
    if response.status_code == 200:
        response_200 = ItemView.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ItemView]:
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
    body: ResolveRequest,
) -> Response[Error | ItemView]:
    """Record an explicit landed or not-landed verdict for an exact retained operation

     Requires full scope, the original operation id and immutable body fingerprint, the inspected
    recovery version and nonempty evidence (at most 1024 bytes). The instance-bound recovery facade
    checks current authority and confirms a durable, attributed verdict before reposting or releasing
    dependent negative work. An expired receipt never proves not-landed. The same verdict, version,
    actor and reason replays its durable outcome; a conflicting retry is refused. The Store operation
    survives cancellation of the HTTP waiter. No raw payload, credential or mutable dollar balance is
    returned.

    Args:
        body (ResolveRequest): The immutable operation and recovery version inspected by the
            operator.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ItemView]
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
    body: ResolveRequest,
) -> Error | ItemView | None:
    """Record an explicit landed or not-landed verdict for an exact retained operation

     Requires full scope, the original operation id and immutable body fingerprint, the inspected
    recovery version and nonempty evidence (at most 1024 bytes). The instance-bound recovery facade
    checks current authority and confirms a durable, attributed verdict before reposting or releasing
    dependent negative work. An expired receipt never proves not-landed. The same verdict, version,
    actor and reason replays its durable outcome; a conflicting retry is refused. The Store operation
    survives cancellation of the HTTP waiter. No raw payload, credential or mutable dollar balance is
    returned.

    Args:
        body (ResolveRequest): The immutable operation and recovery version inspected by the
            operator.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ItemView
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ResolveRequest,
) -> Response[Error | ItemView]:
    """Record an explicit landed or not-landed verdict for an exact retained operation

     Requires full scope, the original operation id and immutable body fingerprint, the inspected
    recovery version and nonempty evidence (at most 1024 bytes). The instance-bound recovery facade
    checks current authority and confirms a durable, attributed verdict before reposting or releasing
    dependent negative work. An expired receipt never proves not-landed. The same verdict, version,
    actor and reason replays its durable outcome; a conflicting retry is refused. The Store operation
    survives cancellation of the HTTP waiter. No raw payload, credential or mutable dollar balance is
    returned.

    Args:
        body (ResolveRequest): The immutable operation and recovery version inspected by the
            operator.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ItemView]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client._async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ResolveRequest,
) -> Error | ItemView | None:
    """Record an explicit landed or not-landed verdict for an exact retained operation

     Requires full scope, the original operation id and immutable body fingerprint, the inspected
    recovery version and nonempty evidence (at most 1024 bytes). The instance-bound recovery facade
    checks current authority and confirms a durable, attributed verdict before reposting or releasing
    dependent negative work. An expired receipt never proves not-landed. The same verdict, version,
    actor and reason replays its durable outcome; a conflicting retry is refused. The Store operation
    survives cancellation of the HTTP waiter. No raw payload, credential or mutable dollar balance is
    returned.

    Args:
        body (ResolveRequest): The immutable operation and recovery version inspected by the
            operator.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ItemView
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
