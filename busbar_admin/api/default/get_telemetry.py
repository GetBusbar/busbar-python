from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.telemetry_view import TelemetryView
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/admin/telemetry",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | TelemetryView | None:
    if response.status_code == 200:
        response_200 = TelemetryView.from_dict(response.json())

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
) -> Response[Error | TelemetryView]:
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
) -> Response[Error | TelemetryView]:
    """Bounded request-phase telemetry snapshot

     An admin read of already-collected request-phase metrics. At most 32 identities and 65536 JSON
    bytes; omitted identities are explicitly counted. Counts, microsecond sums, bins and uptime are
    exact decimal strings. Bins are exclusive, not Prometheus cumulative buckets. The process boot nonce
    survives config reloads and scrapes; uptime_since_start_ms is monotonic time since shared process
    generation initialization (first info read or recorder setup), not OS process creation.
    LlmProducerDrive ends at producer completion; MountedResponseReady ends when the response is
    returned, before its body completes. Neither phase measures completed client delivery. This opens no
    outbound connection.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TelemetryView]
    """

    kwargs = _get_kwargs()

    response = client._request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Error | TelemetryView | None:
    """Bounded request-phase telemetry snapshot

     An admin read of already-collected request-phase metrics. At most 32 identities and 65536 JSON
    bytes; omitted identities are explicitly counted. Counts, microsecond sums, bins and uptime are
    exact decimal strings. Bins are exclusive, not Prometheus cumulative buckets. The process boot nonce
    survives config reloads and scrapes; uptime_since_start_ms is monotonic time since shared process
    generation initialization (first info read or recorder setup), not OS process creation.
    LlmProducerDrive ends at producer completion; MountedResponseReady ends when the response is
    returned, before its body completes. Neither phase measures completed client delivery. This opens no
    outbound connection.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TelemetryView
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Error | TelemetryView]:
    """Bounded request-phase telemetry snapshot

     An admin read of already-collected request-phase metrics. At most 32 identities and 65536 JSON
    bytes; omitted identities are explicitly counted. Counts, microsecond sums, bins and uptime are
    exact decimal strings. Bins are exclusive, not Prometheus cumulative buckets. The process boot nonce
    survives config reloads and scrapes; uptime_since_start_ms is monotonic time since shared process
    generation initialization (first info read or recorder setup), not OS process creation.
    LlmProducerDrive ends at producer completion; MountedResponseReady ends when the response is
    returned, before its body completes. Neither phase measures completed client delivery. This opens no
    outbound connection.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TelemetryView]
    """

    kwargs = _get_kwargs()

    response = await client._async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Error | TelemetryView | None:
    """Bounded request-phase telemetry snapshot

     An admin read of already-collected request-phase metrics. At most 32 identities and 65536 JSON
    bytes; omitted identities are explicitly counted. Counts, microsecond sums, bins and uptime are
    exact decimal strings. Bins are exclusive, not Prometheus cumulative buckets. The process boot nonce
    survives config reloads and scrapes; uptime_since_start_ms is monotonic time since shared process
    generation initialization (first info read or recorder setup), not OS process creation.
    LlmProducerDrive ends at producer completion; MountedResponseReady ends when the response is
    returned, before its body completes. Neither phase measures completed client delivery. This opens no
    outbound connection.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TelemetryView
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
