from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KeyMeteringView")


@_attrs_define
class KeyMeteringView:
    """`GET /keys/{id}/usage` — the current budget-window counters for one key, plus the fraction of the
    tightest RPM/TPM cap remaining (`null` = uncapped). `budget_period`/`window_start` are `null`
    when the key record could not be read.

        Attributes:
            as_of (int):
            budget_period (None | str):
            id (str):
            rate_headroom (float | None):
            requests (int):
            spend_cents (int):
            tokens (int):
            window_start (int | None):
    """

    as_of: int
    budget_period: None | str
    id: str
    rate_headroom: float | None
    requests: int
    spend_cents: int
    tokens: int
    window_start: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        as_of = self.as_of

        budget_period: None | str
        budget_period = self.budget_period

        id = self.id

        rate_headroom: float | None
        rate_headroom = self.rate_headroom

        requests = self.requests

        spend_cents = self.spend_cents

        tokens = self.tokens

        window_start: int | None
        window_start = self.window_start

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "as_of": as_of,
                "budget_period": budget_period,
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

        def _parse_budget_period(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        budget_period = _parse_budget_period(d.pop("budget_period"))

        id = d.pop("id")

        def _parse_rate_headroom(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        rate_headroom = _parse_rate_headroom(d.pop("rate_headroom"))

        requests = d.pop("requests")

        spend_cents = d.pop("spend_cents")

        tokens = d.pop("tokens")

        def _parse_window_start(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        window_start = _parse_window_start(d.pop("window_start"))

        key_metering_view = cls(
            as_of=as_of,
            budget_period=budget_period,
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
