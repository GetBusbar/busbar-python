from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.group_view import GroupView
from ...models.patch_groups_name_body import PatchGroupsNameBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    *,
    body: PatchGroupsNameBody,
    if_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/admin/groups/{name}".format(
            name=quote(str(name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GroupView | None:
    if response.status_code == 200:
        response_200 = GroupView.from_dict(response.json())

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

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GroupView]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    body: PatchGroupsNameBody,
    if_match: str | Unset = UNSET,
) -> Response[Error | GroupView]:
    """Partial update: change only the fields present (e.g. raise a budget, freeze a group)

    Args:
        name (str):
        if_match (str | Unset):
        body (PatchGroupsNameBody): A partial update: only the fields present are changed.
            `limits` and `child_default` REPLACE their whole value when present.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GroupView]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient,
    body: PatchGroupsNameBody,
    if_match: str | Unset = UNSET,
) -> Error | GroupView | None:
    """Partial update: change only the fields present (e.g. raise a budget, freeze a group)

    Args:
        name (str):
        if_match (str | Unset):
        body (PatchGroupsNameBody): A partial update: only the fields present are changed.
            `limits` and `child_default` REPLACE their whole value when present.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GroupView
    """

    return sync_detailed(
        name=name,
        client=client,
        body=body,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    body: PatchGroupsNameBody,
    if_match: str | Unset = UNSET,
) -> Response[Error | GroupView]:
    """Partial update: change only the fields present (e.g. raise a budget, freeze a group)

    Args:
        name (str):
        if_match (str | Unset):
        body (PatchGroupsNameBody): A partial update: only the fields present are changed.
            `limits` and `child_default` REPLACE their whole value when present.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GroupView]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient,
    body: PatchGroupsNameBody,
    if_match: str | Unset = UNSET,
) -> Error | GroupView | None:
    """Partial update: change only the fields present (e.g. raise a budget, freeze a group)

    Args:
        name (str):
        if_match (str | Unset):
        body (PatchGroupsNameBody): A partial update: only the fields present are changed.
            `limits` and `child_default` REPLACE their whole value when present.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GroupView
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            body=body,
            if_match=if_match,
        )
    ).parsed
