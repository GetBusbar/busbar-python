from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.a2a_trust_view import A2ATrustView
from ...models.approve_req import ApproveReq
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    name: str,
    *,
    body: ApproveReq,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/admin/agents/{name}/approve".format(
            name=quote(str(name), safe="").replace(".", "%2E"),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> A2ATrustView | Error | None:
    if response.status_code == 200:
        response_200 = A2ATrustView.from_dict(response.json())

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

    if response.status_code == 413:
        response_413 = Error.from_dict(response.json())

        return response_413

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

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
    body: ApproveReq,
) -> Response[A2ATrustView | Error]:
    """Lock a registered agent to the card fingerprint the operator has SEEN. The card is re-fetched and
    re-verified, and an approval naming any other fingerprint is refused

    Args:
        name (str):
        body (ApproveReq): The `approve` request body. ONE required field, and it is required
            because it is the operator's
            evidence that they looked.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[A2ATrustView | Error]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = client._request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient,
    body: ApproveReq,
) -> A2ATrustView | Error | None:
    """Lock a registered agent to the card fingerprint the operator has SEEN. The card is re-fetched and
    re-verified, and an approval naming any other fingerprint is refused

    Args:
        name (str):
        body (ApproveReq): The `approve` request body. ONE required field, and it is required
            because it is the operator's
            evidence that they looked.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        A2ATrustView | Error
    """

    return sync_detailed(
        name=name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    body: ApproveReq,
) -> Response[A2ATrustView | Error]:
    """Lock a registered agent to the card fingerprint the operator has SEEN. The card is re-fetched and
    re-verified, and an approval naming any other fingerprint is refused

    Args:
        name (str):
        body (ApproveReq): The `approve` request body. ONE required field, and it is required
            because it is the operator's
            evidence that they looked.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[A2ATrustView | Error]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = await client._async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient,
    body: ApproveReq,
) -> A2ATrustView | Error | None:
    """Lock a registered agent to the card fingerprint the operator has SEEN. The card is re-fetched and
    re-verified, and an approval naming any other fingerprint is refused

    Args:
        name (str):
        body (ApproveReq): The `approve` request body. ONE required field, and it is required
            because it is the operator's
            evidence that they looked.

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
            body=body,
        )
    ).parsed
