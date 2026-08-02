from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KeyMeteringView")


@_attrs_define
class KeyMeteringView:
    """`GET /keys/{id}/usage`: the key's all-time attribution counters (a 1.5.0 key bucket accrues in
    the `total` window; limits live on the bound group's own windows) plus the fraction of the
    tightest `requests`/`tokens` limit across the group chain remaining (`null` = no such limit).

        Attributes:
            as_of (int):
            budget_period (str): Always `"total"` (the key attribution window).
            group (None | str): The bound `groups:` entry (`null` = unlimited key).
            id (str):
            rate_headroom (float | None):
            requests (int):
            spend_cents (int):
            tokens (int):
            window_start (int): Always `0` (the all-time window start).
    """

    as_of: int
    budget_period: str
    group: None | str
    id: str
    rate_headroom: float | None
    requests: int
    spend_cents: int
    tokens: int
    window_start: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        as_of = self.as_of

        budget_period = self.budget_period

        group: None | str
        group = self.group

        id = self.id

        rate_headroom: float | None
        rate_headroom = self.rate_headroom

        requests = self.requests

        spend_cents = self.spend_cents

        tokens = self.tokens

        window_start = self.window_start

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "as_of": as_of,
                "budget_period": budget_period,
                "group": group,
                "id": id,
                "rate_headroom": rate_headroom,
                "requests": requests,
                "spend_cents": spend_cents,
                "tokens": tokens,
                "window_start": window_start,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        as_of = d.pop("as_of")

        budget_period = d.pop("budget_period")

        def _parse_group(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        group = _parse_group(d.pop("group"))

        id = d.pop("id")

        def _parse_rate_headroom(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        rate_headroom = _parse_rate_headroom(d.pop("rate_headroom"))

        requests = d.pop("requests")

        spend_cents = d.pop("spend_cents")

        tokens = d.pop("tokens")

        window_start = d.pop("window_start")

        key_metering_view = cls(
            as_of=as_of,
            budget_period=budget_period,
            group=group,
            id=id,
            rate_headroom=rate_headroom,
            requests=requests,
            spend_cents=spend_cents,
            tokens=tokens,
            window_start=window_start,
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
