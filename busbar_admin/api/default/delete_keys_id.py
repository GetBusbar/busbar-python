from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.mutation_applied_error import MutationAppliedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    if_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/admin/keys/{id}".format(
            id=quote(str(id), safe="").replace(".", "%2E"),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Error | Error | MutationAppliedError | None:
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

        def _parse_response_409(data: object) -> Error | MutationAppliedError:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_409_type_0 = Error.from_dict(data)

                return response_409_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_409_type_1 = MutationAppliedError.from_dict(data)

            return response_409_type_1
            raise ValueError("Invalid value for response_409")

        response_409 = _parse_response_409(response.json())

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


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Error | Error | MutationAppliedError]:
    return Response(
        status_code=HTTPStatus(response.status_code)
        if response.status_code in HTTPStatus._value2member_map_
        else response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    if_match: str | Unset = UNSET,
) -> Response[Any | Error | Error | MutationAppliedError]:
    """Revoke a key: it stops resolving immediately. Optional `If-Match` (the key's ETag)

    Args:
        id (str):
        if_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | Error | MutationAppliedError]
    """

    kwargs = _get_kwargs(
        id=id,
        if_match=if_match,
    )

    response = client._request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    if_match: str | Unset = UNSET,
) -> Any | Error | Error | MutationAppliedError | None:
    """Revoke a key: it stops resolving immediately. Optional `If-Match` (the key's ETag)

    Args:
        id (str):
        if_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | Error | MutationAppliedError
    """

    return sync_detailed(
        id=id,
        client=client,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    if_match: str | Unset = UNSET,
) -> Response[Any | Error | Error | MutationAppliedError]:
    """Revoke a key: it stops resolving immediately. Optional `If-Match` (the key's ETag)

    Args:
        id (str):
        if_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | Error | MutationAppliedError]
    """

    kwargs = _get_kwargs(
        id=id,
        if_match=if_match,
    )

    response = await client._async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    if_match: str | Unset = UNSET,
) -> Any | Error | Error | MutationAppliedError | None:
    """Revoke a key: it stops resolving immediately. Optional `If-Match` (the key's ETag)

    Args:
        id (str):
        if_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | Error | MutationAppliedError
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            if_match=if_match,
        )
    ).parsed
