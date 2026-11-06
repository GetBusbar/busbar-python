from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.adjust_req import AdjustReq
from ...models.adjust_view import AdjustView
from ...models.adjustment_action_in_flight_error import AdjustmentActionInFlightError
from ...models.adjustment_action_view import AdjustmentActionView
from ...models.error import Error
from ...models.exact_adjust_req import ExactAdjustReq
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: AdjustReq | ExactAdjustReq,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/admin/adjust",
    }

    if isinstance(body, AdjustReq):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AdjustmentActionInFlightError | AdjustmentActionView | Error | AdjustmentActionView | AdjustView | Error:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> AdjustmentActionView | AdjustView:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_adjustment_response_type_0 = AdjustView.from_dict(data)

                return componentsschemas_adjustment_response_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_adjustment_response_type_1 = AdjustmentActionView.from_dict(data)

            return componentsschemas_adjustment_response_type_1
            raise ValueError("Invalid value for response_200")

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:

        def _parse_response_400(data: object) -> AdjustmentActionInFlightError | AdjustmentActionView | Error:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_400_type_0 = Error.from_dict(data)

                return response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_400_type_1 = AdjustmentActionView.from_dict(data)

                return response_400_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_400_type_2 = AdjustmentActionInFlightError.from_dict(data)

            return response_400_type_2
            raise ValueError("Invalid value for response_400")

        response_400 = _parse_response_400(response.json())

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

        def _parse_response_409(data: object) -> AdjustmentActionInFlightError | AdjustmentActionView | Error:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_409_type_0 = Error.from_dict(data)

                return response_409_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_409_type_1 = AdjustmentActionView.from_dict(data)

                return response_409_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_409_type_2 = AdjustmentActionInFlightError.from_dict(data)

            return response_409_type_2
            raise ValueError("Invalid value for response_409")

        response_409 = _parse_response_409(response.json())

        return response_409

    if response.status_code == 413:
        response_413 = Error.from_dict(response.json())

        return response_413

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if response.status_code == 503:

        def _parse_response_503(data: object) -> AdjustmentActionInFlightError | AdjustmentActionView | Error:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_503_type_0 = Error.from_dict(data)

                return response_503_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_503_type_1 = AdjustmentActionView.from_dict(data)

                return response_503_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_503_type_2 = AdjustmentActionInFlightError.from_dict(data)

            return response_503_type_2
            raise ValueError("Invalid value for response_503")

        response_503 = _parse_response_503(response.json())

        return response_503

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AdjustmentActionInFlightError | AdjustmentActionView | Error | AdjustmentActionView | AdjustView | Error]:
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
    body: AdjustReq | ExactAdjustReq,
    idempotency_key: str | Unset = UNSET,
) -> Response[AdjustmentActionInFlightError | AdjustmentActionView | Error | AdjustmentActionView | AdjustView | Error]:
    """Correct a key's COUNTS by a signed delta, never a money figure

     Correct counts at the original card epoch. With Idempotency-Key, the durable exact-Count profile
    binds actor/action to exact bytes and returns AdjustmentActionView. Without it, retain legacy
    signed-integer/nonretryable semantics. Applied, not_applied and unknown are distinct outcomes; never
    infer no effect from a failed response.

    Args:
        idempotency_key (str | Unset):
        body (AdjustReq | ExactAdjustReq): Header-selective profiles: AdjustReq without
            Idempotency-Key, ExactAdjustReq with it. OpenAPI body union alone cannot validate the
            cross-header condition.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdjustmentActionInFlightError | AdjustmentActionView | Error | AdjustmentActionView | AdjustView | Error]
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
    body: AdjustReq | ExactAdjustReq,
    idempotency_key: str | Unset = UNSET,
) -> AdjustmentActionInFlightError | AdjustmentActionView | Error | AdjustmentActionView | AdjustView | Error | None:
    """Correct a key's COUNTS by a signed delta, never a money figure

     Correct counts at the original card epoch. With Idempotency-Key, the durable exact-Count profile
    binds actor/action to exact bytes and returns AdjustmentActionView. Without it, retain legacy
    signed-integer/nonretryable semantics. Applied, not_applied and unknown are distinct outcomes; never
    infer no effect from a failed response.

    Args:
        idempotency_key (str | Unset):
        body (AdjustReq | ExactAdjustReq): Header-selective profiles: AdjustReq without
            Idempotency-Key, ExactAdjustReq with it. OpenAPI body union alone cannot validate the
            cross-header condition.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdjustmentActionInFlightError | AdjustmentActionView | Error | AdjustmentActionView | AdjustView | Error
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AdjustReq | ExactAdjustReq,
    idempotency_key: str | Unset = UNSET,
) -> Response[AdjustmentActionInFlightError | AdjustmentActionView | Error | AdjustmentActionView | AdjustView | Error]:
    """Correct a key's COUNTS by a signed delta, never a money figure

     Correct counts at the original card epoch. With Idempotency-Key, the durable exact-Count profile
    binds actor/action to exact bytes and returns AdjustmentActionView. Without it, retain legacy
    signed-integer/nonretryable semantics. Applied, not_applied and unknown are distinct outcomes; never
    infer no effect from a failed response.

    Args:
        idempotency_key (str | Unset):
        body (AdjustReq | ExactAdjustReq): Header-selective profiles: AdjustReq without
            Idempotency-Key, ExactAdjustReq with it. OpenAPI body union alone cannot validate the
            cross-header condition.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdjustmentActionInFlightError | AdjustmentActionView | Error | AdjustmentActionView | AdjustView | Error]
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
    body: AdjustReq | ExactAdjustReq,
    idempotency_key: str | Unset = UNSET,
) -> AdjustmentActionInFlightError | AdjustmentActionView | Error | AdjustmentActionView | AdjustView | Error | None:
    """Correct a key's COUNTS by a signed delta, never a money figure

     Correct counts at the original card epoch. With Idempotency-Key, the durable exact-Count profile
    binds actor/action to exact bytes and returns AdjustmentActionView. Without it, retain legacy
    signed-integer/nonretryable semantics. Applied, not_applied and unknown are distinct outcomes; never
    infer no effect from a failed response.

    Args:
        idempotency_key (str | Unset):
        body (AdjustReq | ExactAdjustReq): Header-selective profiles: AdjustReq without
            Idempotency-Key, ExactAdjustReq with it. OpenAPI body union alone cannot validate the
            cross-header condition.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdjustmentActionInFlightError | AdjustmentActionView | Error | AdjustmentActionView | AdjustView | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
