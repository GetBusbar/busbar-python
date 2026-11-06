from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    file: str,
    *,
    expected_archive_sha256: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["expected_archive_sha256"] = expected_archive_sha256

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/admin/plugins/{file}".format(
            file=quote(str(file), safe="").replace(".", "%2E"),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code)
        if response.status_code in HTTPStatus._value2member_map_
        else response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    file: str,
    *,
    client: AuthenticatedClient,
    expected_archive_sha256: str | Unset = UNSET,
) -> Response[Any | Error]:
    """Remove a dynamic-library plugin (library + manifest sidecar) from the plugins directory. A loaded
    store keeps running until the next store (re)load

    Args:
        file (str):
        expected_archive_sha256 (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        file=file,
        expected_archive_sha256=expected_archive_sha256,
    )

    response = client._request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    file: str,
    *,
    client: AuthenticatedClient,
    expected_archive_sha256: str | Unset = UNSET,
) -> Any | Error | None:
    """Remove a dynamic-library plugin (library + manifest sidecar) from the plugins directory. A loaded
    store keeps running until the next store (re)load

    Args:
        file (str):
        expected_archive_sha256 (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return sync_detailed(
        file=file,
        client=client,
        expected_archive_sha256=expected_archive_sha256,
    ).parsed


async def asyncio_detailed(
    file: str,
    *,
    client: AuthenticatedClient,
    expected_archive_sha256: str | Unset = UNSET,
) -> Response[Any | Error]:
    """Remove a dynamic-library plugin (library + manifest sidecar) from the plugins directory. A loaded
    store keeps running until the next store (re)load

    Args:
        file (str):
        expected_archive_sha256 (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        file=file,
        expected_archive_sha256=expected_archive_sha256,
    )

    response = await client._async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    file: str,
    *,
    client: AuthenticatedClient,
    expected_archive_sha256: str | Unset = UNSET,
) -> Any | Error | None:
    """Remove a dynamic-library plugin (library + manifest sidecar) from the plugins directory. A loaded
    store keeps running until the next store (re)load

    Args:
        file (str):
        expected_archive_sha256 (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return (
        await asyncio_detailed(
            file=file,
            client=client,
            expected_archive_sha256=expected_archive_sha256,
        )
    ).parsed
