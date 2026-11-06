from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KeyMeteringView")


@_attrs_define(repr=False)
class KeyMeteringView:
    """`GET /keys/{id}/usage`: the key's all-time attribution counters (a 1.5.0 key bucket accrues in
    the `total` window; limits live on the bound group's own windows) plus the fraction of the
    tightest `requests`/`tokens` limit across the group chain remaining (`null` = no such limit).

        Attributes:
            id (str):
            budget_period (str): Always `"total"` (the key attribution window).
            window_start (int): Always `0` (the all-time window start).
            as_of (int):
            group (None | str): The bound `groups:` entry (`null` = unlimited key).
            spend_cents (int):
            tokens (float): Exact scale-6 decimal quantity, serialized as a JSON number.
            requests (int):
            rate_headroom (float | None):
    """

    id: str
    budget_period: str
    window_start: int
    as_of: int
    group: None | str
    spend_cents: int
    tokens: float
    requests: int
    rate_headroom: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        budget_period = self.budget_period

        window_start = self.window_start

        as_of = self.as_of

        group: None | str
        group = self.group

        spend_cents = self.spend_cents

        tokens = self.tokens

        requests = self.requests

        rate_headroom: float | None
        rate_headroom = self.rate_headroom

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "budget_period": budget_period,
                "window_start": window_start,
                "as_of": as_of,
                "group": group,
                "spend_cents": spend_cents,
                "tokens": tokens,
                "requests": requests,
                "rate_headroom": rate_headroom,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        budget_period = d.pop("budget_period")

        window_start = d.pop("window_start")

        as_of = d.pop("as_of")

        def _parse_group(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        group = _parse_group(d.pop("group"))

        spend_cents = d.pop("spend_cents")

        tokens = d.pop("tokens")

        requests = d.pop("requests")

        def _parse_rate_headroom(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        rate_headroom = _parse_rate_headroom(d.pop("rate_headroom"))

        key_metering_view = cls(
            id=id,
            budget_period=budget_period,
            window_start=window_start,
            as_of=as_of,
            group=group,
            spend_cents=spend_cents,
            tokens=tokens,
            requests=requests,
            rate_headroom=rate_headroom,
        )

        key_metering_view.additional_properties = d
        return key_metering_view

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
