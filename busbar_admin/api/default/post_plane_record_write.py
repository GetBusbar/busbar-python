from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.plane_record_write_req import PlaneRecordWriteReq
from ...models.plane_record_write_view import PlaneRecordWriteView
from ...types import Response


def _get_kwargs(
    *,
    body: PlaneRecordWriteReq,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/admin/plane-record-write",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | PlaneRecordWriteView | None:
    if response.status_code == 200:
        response_200 = PlaneRecordWriteView.from_dict(response.json())

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

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | PlaneRecordWriteView]:
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
    body: PlaneRecordWriteReq,
) -> Response[Error | PlaneRecordWriteView]:
    """Upsert one record of a plane this node serves

     Upserted by `(kind, id)` through the plane-facing store the planes persist through, and only for a
    `kind` the named plane declares in its `record_kinds` (`GET /plane-facts` lists them). `body` is
    stored as its JSON bytes and never decoded by the store; `terminal` is the retention disposition.
    Honors an `Idempotency-Key` header (per-principal, ~10min replay): a retry with the same key and
    body answers the first answer.

    Args:
        body (PlaneRecordWriteReq): `POST /plane-record-write`: one plane record, upserted by
            `(kind, id)`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PlaneRecordWriteView]
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
    body: PlaneRecordWriteReq,
) -> Error | PlaneRecordWriteView | None:
    """Upsert one record of a plane this node serves

     Upserted by `(kind, id)` through the plane-facing store the planes persist through, and only for a
    `kind` the named plane declares in its `record_kinds` (`GET /plane-facts` lists them). `body` is
    stored as its JSON bytes and never decoded by the store; `terminal` is the retention disposition.
    Honors an `Idempotency-Key` header (per-principal, ~10min replay): a retry with the same key and
    body answers the first answer.

    Args:
        body (PlaneRecordWriteReq): `POST /plane-record-write`: one plane record, upserted by
            `(kind, id)`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PlaneRecordWriteView
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PlaneRecordWriteReq,
) -> Response[Error | PlaneRecordWriteView]:
    """Upsert one record of a plane this node serves

     Upserted by `(kind, id)` through the plane-facing store the planes persist through, and only for a
    `kind` the named plane declares in its `record_kinds` (`GET /plane-facts` lists them). `body` is
    stored as its JSON bytes and never decoded by the store; `terminal` is the retention disposition.
    Honors an `Idempotency-Key` header (per-principal, ~10min replay): a retry with the same key and
    body answers the first answer.

    Args:
        body (PlaneRecordWriteReq): `POST /plane-record-write`: one plane record, upserted by
            `(kind, id)`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PlaneRecordWriteView]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client._async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PlaneRecordWriteReq,
) -> Error | PlaneRecordWriteView | None:
    """Upsert one record of a plane this node serves

     Upserted by `(kind, id)` through the plane-facing store the planes persist through, and only for a
    `kind` the named plane declares in its `record_kinds` (`GET /plane-facts` lists them). `body` is
    stored as its JSON bytes and never decoded by the store; `terminal` is the retention disposition.
    Honors an `Idempotency-Key` header (per-principal, ~10min replay): a retry with the same key and
    body answers the first answer.

    Args:
        body (PlaneRecordWriteReq): `POST /plane-record-write`: one plane record, upserted by
            `(kind, id)`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PlaneRecordWriteView
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
