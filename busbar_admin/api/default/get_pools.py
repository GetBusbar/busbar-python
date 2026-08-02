from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.page_pool_view import PagePoolView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    detail: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["detail"] = detail

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/admin/pools",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | PagePoolView | None:
    if response.status_code == 200:
        response_200 = PagePoolView.from_dict(response.json())

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

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | PagePoolView]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    detail: str | Unset = UNSET,
) -> Response[Error | PagePoolView]:
    """Pool topology (members + weights). ?detail=true inlines live member status (one call, no N+1)

    Args:
        detail (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PagePoolView]
    """

    kwargs = _get_kwargs(
        detail=detail,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    detail: str | Unset = UNSET,
) -> Error | PagePoolView | None:
    """Pool topology (members + weights). ?detail=true inlines live member status (one call, no N+1)

    Args:
        detail (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PagePoolView
    """

    return sync_detailed(
        client=client,
        detail=detail,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    detail: str | Unset = UNSET,
) -> Response[Error | PagePoolView]:
    """Pool topology (members + weights). ?detail=true inlines live member status (one call, no N+1)

    Args:
        detail (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PagePoolView]
    """

    kwargs = _get_kwargs(
        detail=detail,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    detail: str | Unset = UNSET,
) -> Error | PagePoolView | None:
    """Pool topology (members + weights). ?detail=true inlines live member status (one call, no N+1)

    Args:
        detail (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PagePoolView
    """

    return (
        await asyncio_detailed(
            client=client,
            detail=detail,
        )
    ).parsed
