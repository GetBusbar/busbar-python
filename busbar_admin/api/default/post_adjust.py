from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.adjust_req import AdjustReq
from ...models.adjust_view import AdjustView
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    body: AdjustReq,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/admin/adjust",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AdjustView | Error | None:
    if response.status_code == 200:
        response_200 = AdjustView.from_dict(response.json())

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

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AdjustView | Error]:
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
    body: AdjustReq,
) -> Response[AdjustView | Error]:
    """Correct a key's COUNTS by a signed delta, never a money figure

     Money is the one ledger's counts x the rate card, so a correction moves counts: a signed delta per
    class on the key's counts for one lane and one history entry, applied at once, all or nothing, to
    the key's own budget bucket and each group bucket the named pool takes part in, and kept beside the
    day's metering rows so `GET /admin/usage` serves the counts as adjusted. A delta that would take any
    count below zero, or names counts the day's metering does not hold, is refused and nothing is
    applied.

    Args:
        body (AdjustReq): `POST /adjust`: a SIGNED correction to a key's COUNTS on the one ledger,
            never to a money
            figure. It names the key, the lane the counts were earned on, the rate-card history entry
            they
            were priced with, and the pool the unit was dispatched through.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdjustView | Error]
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
    body: AdjustReq,
) -> AdjustView | Error | None:
    """Correct a key's COUNTS by a signed delta, never a money figure

     Money is the one ledger's counts x the rate card, so a correction moves counts: a signed delta per
    class on the key's counts for one lane and one history entry, applied at once, all or nothing, to
    the key's own budget bucket and each group bucket the named pool takes part in, and kept beside the
    day's metering rows so `GET /admin/usage` serves the counts as adjusted. A delta that would take any
    count below zero, or names counts the day's metering does not hold, is refused and nothing is
    applied.

    Args:
        body (AdjustReq): `POST /adjust`: a SIGNED correction to a key's COUNTS on the one ledger,
            never to a money
            figure. It names the key, the lane the counts were earned on, the rate-card history entry
            they
            were priced with, and the pool the unit was dispatched through.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdjustView | Error
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AdjustReq,
) -> Response[AdjustView | Error]:
    """Correct a key's COUNTS by a signed delta, never a money figure

     Money is the one ledger's counts x the rate card, so a correction moves counts: a signed delta per
    class on the key's counts for one lane and one history entry, applied at once, all or nothing, to
    the key's own budget bucket and each group bucket the named pool takes part in, and kept beside the
    day's metering rows so `GET /admin/usage` serves the counts as adjusted. A delta that would take any
    count below zero, or names counts the day's metering does not hold, is refused and nothing is
    applied.

    Args:
        body (AdjustReq): `POST /adjust`: a SIGNED correction to a key's COUNTS on the one ledger,
            never to a money
            figure. It names the key, the lane the counts were earned on, the rate-card history entry
            they
            were priced with, and the pool the unit was dispatched through.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdjustView | Error]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client._async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AdjustReq,
) -> AdjustView | Error | None:
    """Correct a key's COUNTS by a signed delta, never a money figure

     Money is the one ledger's counts x the rate card, so a correction moves counts: a signed delta per
    class on the key's counts for one lane and one history entry, applied at once, all or nothing, to
    the key's own budget bucket and each group bucket the named pool takes part in, and kept beside the
    day's metering rows so `GET /admin/usage` serves the counts as adjusted. A delta that would take any
    count below zero, or names counts the day's metering does not hold, is refused and nothing is
    applied.

    Args:
        body (AdjustReq): `POST /adjust`: a SIGNED correction to a key's COUNTS on the one ledger,
            never to a money
            figure. It names the key, the lane the counts were earned on, the rate-card history entry
            they
            were priced with, and the pool the unit was dispatched through.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdjustView | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
