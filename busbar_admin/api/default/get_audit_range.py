from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audit_chain_range_view import AuditChainRangeView
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_: int,
    to: int,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/admin/audit/range",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AuditChainRangeView | Error | None:
    if response.status_code == 200:
        response_200 = AuditChainRangeView.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 413:
        response_413 = Error.from_dict(response.json())

        return response_413

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())

        return response_503

    try:
        response_default = Error.from_dict(response.json())

        return response_default

    except (ValueError, KeyError, TypeError, AttributeError):
        # An intermediary may return an undocumented non-JSON or malformed body.
        # Preserve the raw response and the caller's unexpected-status policy.
        if client.raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content) from None
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AuditChainRangeView | Error]:
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
    from_: int,
    to: int,
    cursor: str | Unset = UNSET,
) -> Response[AuditChainRangeView | Error]:
    """Audit records by position, each with every field its digest was taken over

     A pull, never a push: the node answers and opens no connection. A read: it mutates nothing and is
    never posture-gated.

    Args:
        from_ (int):
        to (int):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditChainRangeView | Error]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        cursor=cursor,
    )

    response = client._request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    from_: int,
    to: int,
    cursor: str | Unset = UNSET,
) -> AuditChainRangeView | Error | None:
    """Audit records by position, each with every field its digest was taken over

     A pull, never a push: the node answers and opens no connection. A read: it mutates nothing and is
    never posture-gated.

    Args:
        from_ (int):
        to (int):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditChainRangeView | Error
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    from_: int,
    to: int,
    cursor: str | Unset = UNSET,
) -> Response[AuditChainRangeView | Error]:
    """Audit records by position, each with every field its digest was taken over

     A pull, never a push: the node answers and opens no connection. A read: it mutates nothing and is
    never posture-gated.

    Args:
        from_ (int):
        to (int):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditChainRangeView | Error]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        cursor=cursor,
    )

    response = await client._async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    from_: int,
    to: int,
    cursor: str | Unset = UNSET,
) -> AuditChainRangeView | Error | None:
    """Audit records by position, each with every field its digest was taken over

     A pull, never a push: the node answers and opens no connection. A read: it mutates nothing and is
    never posture-gated.

    Args:
        from_ (int):
        to (int):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditChainRangeView | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            cursor=cursor,
        )
    ).parsed
