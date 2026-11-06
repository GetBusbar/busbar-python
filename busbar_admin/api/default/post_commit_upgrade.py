from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.commit_upgrade_req import CommitUpgradeReq
from ...models.commit_upgrade_view import CommitUpgradeView
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CommitUpgradeReq,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/admin/commit-upgrade",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CommitUpgradeView | Error | None:
    if response.status_code == 200:
        response_200 = CommitUpgradeView.from_dict(response.json())

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
) -> Response[CommitUpgradeView | Error]:
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
    body: CommitUpgradeReq,
    idempotency_key: str | Unset = UNSET,
) -> Response[CommitUpgradeView | Error]:
    """Commit the fleet to the release this node runs

     The body names the release; one this node does not run is refused and seals nothing. The committed
    release is sealed on the node journal before the answer names its position and chain hash. Honors an
    `Idempotency-Key` header (per-principal, ~10min replay): a retry with the same key and body answers
    the first commit and seals nothing again.

    Args:
        idempotency_key (str | Unset):
        body (CommitUpgradeReq): `POST /commit-upgrade`: the release the fleet commits to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommitUpgradeView | Error]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client._request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CommitUpgradeReq,
    idempotency_key: str | Unset = UNSET,
) -> CommitUpgradeView | Error | None:
    """Commit the fleet to the release this node runs

     The body names the release; one this node does not run is refused and seals nothing. The committed
    release is sealed on the node journal before the answer names its position and chain hash. Honors an
    `Idempotency-Key` header (per-principal, ~10min replay): a retry with the same key and body answers
    the first commit and seals nothing again.

    Args:
        idempotency_key (str | Unset):
        body (CommitUpgradeReq): `POST /commit-upgrade`: the release the fleet commits to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommitUpgradeView | Error
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CommitUpgradeReq,
    idempotency_key: str | Unset = UNSET,
) -> Response[CommitUpgradeView | Error]:
    """Commit the fleet to the release this node runs

     The body names the release; one this node does not run is refused and seals nothing. The committed
    release is sealed on the node journal before the answer names its position and chain hash. Honors an
    `Idempotency-Key` header (per-principal, ~10min replay): a retry with the same key and body answers
    the first commit and seals nothing again.

    Args:
        idempotency_key (str | Unset):
        body (CommitUpgradeReq): `POST /commit-upgrade`: the release the fleet commits to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommitUpgradeView | Error]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client._async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CommitUpgradeReq,
    idempotency_key: str | Unset = UNSET,
) -> CommitUpgradeView | Error | None:
    """Commit the fleet to the release this node runs

     The body names the release; one this node does not run is refused and seals nothing. The committed
    release is sealed on the node journal before the answer names its position and chain hash. Honors an
    `Idempotency-Key` header (per-principal, ~10min replay): a retry with the same key and body answers
    the first commit and seals nothing again.

    Args:
        idempotency_key (str | Unset):
        body (CommitUpgradeReq): `POST /commit-upgrade`: the release the fleet commits to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommitUpgradeView | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
