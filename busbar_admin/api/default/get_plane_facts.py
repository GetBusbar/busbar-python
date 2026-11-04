from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.plane_facts_view import PlaneFactsView
from ...types import UNSET, Response


def _get_kwargs(
    *,
    plane: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["plane"] = plane

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/admin/plane-facts",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | PlaneFactsView | None:
    if response.status_code == 200:
        response_200 = PlaneFactsView.from_dict(response.json())

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

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | PlaneFactsView]:
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
    plane: str,
) -> Response[Error | PlaneFactsView]:
    """What a plane this node serves declares about itself

     The plane's registry key, config sections, grant kinds, nouns, billable classes, fee units, metric
    families and served operation classes. A read: it mutates nothing and needs `read-only`.

    Args:
        plane (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PlaneFactsView]
    """

    kwargs = _get_kwargs(
        plane=plane,
    )

    response = client._request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    plane: str,
) -> Error | PlaneFactsView | None:
    """What a plane this node serves declares about itself

     The plane's registry key, config sections, grant kinds, nouns, billable classes, fee units, metric
    families and served operation classes. A read: it mutates nothing and needs `read-only`.

    Args:
        plane (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PlaneFactsView
    """

    return sync_detailed(
        client=client,
        plane=plane,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    plane: str,
) -> Response[Error | PlaneFactsView]:
    """What a plane this node serves declares about itself

     The plane's registry key, config sections, grant kinds, nouns, billable classes, fee units, metric
    families and served operation classes. A read: it mutates nothing and needs `read-only`.

    Args:
        plane (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PlaneFactsView]
    """

    kwargs = _get_kwargs(
        plane=plane,
    )

    response = await client._async_request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    plane: str,
) -> Error | PlaneFactsView | None:
    """What a plane this node serves declares about itself

     The plane's registry key, config sections, grant kinds, nouns, billable classes, fee units, metric
    families and served operation classes. A read: it mutates nothing and needs `read-only`.

    Args:
        plane (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PlaneFactsView
    """

    return (
        await asyncio_detailed(
            client=client,
            plane=plane,
        )
    ).parsed
