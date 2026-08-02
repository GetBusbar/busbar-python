from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LimitView")


@_attrs_define
class LimitView:
    """One limit inside a `GroupView`: an explicit `{ metric, amount, per, pool }` projection of a
    config `LimitCfg`. The config file's compact `{ budget: 3000, per: month }` form is
    deserialize-only sugar; the read API projects it explicitly so a consumer never has to know
    the metric is the map key. `per` is `None` only for `concurrent` (an instantaneous gauge, no
    window); `pool` is present only on a pool-scoped limit.

        Attributes:
            amount (int): The cap amount (requests/tokens/cents, or the in-flight gauge for `concurrent`).
            metric (str): One of `requests` | `tokens` | `budget` | `concurrent`.
            downgrade_to (None | str | Unset): Where `on_exhaust: downgrade` sends exhausted traffic. Present iff
                downgrading.
            on_exhaust (None | str | Unset): The budget-exhaustion behavior: `block` or `downgrade`. Absent = block (the
                default).
            per (None | str | Unset): The accounting window: `minute` | `hour` | `day` | `month` | `total`. Absent for
                `concurrent`.
            pool (None | str | Unset): The pool scope: present when the limit carries `pool: <name>` (it accounts and
                enforces
                only that pool's traffic, per `(group, pool)`); absent for a group-wide limit.
    """

    amount: int
    metric: str
    downgrade_to: None | str | Unset = UNSET
    on_exhaust: None | str | Unset = UNSET
    per: None | str | Unset = UNSET
    pool: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        metric = self.metric

        downgrade_to: None | str | Unset
        if isinstance(self.downgrade_to, Unset):
            downgrade_to = UNSET
        else:
            downgrade_to = self.downgrade_to

        on_exhaust: None | str | Unset
        if isinstance(self.on_exhaust, Unset):
            on_exhaust = UNSET
        else:
            on_exhaust = self.on_exhaust

        per: None | str | Unset
        if isinstance(self.per, Unset):
            per = UNSET
        else:
            per = self.per

        pool: None | str | Unset
        if isinstance(self.pool, Unset):
            pool = UNSET
        else:
            pool = self.pool

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "metric": metric,
            }
        )
        if downgrade_to is not UNSET:
            field_dict["downgrade_to"] = downgrade_to
        if on_exhaust is not UNSET:
            field_dict["on_exhaust"] = on_exhaust
        if per is not UNSET:
            field_dict["per"] = per
        if pool is not UNSET:
            field_dict["pool"] = pool

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount")

        metric = d.pop("metric")

        def _parse_downgrade_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        downgrade_to = _parse_downgrade_to(d.pop("downgrade_to", UNSET))

        def _parse_on_exhaust(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        on_exhaust = _parse_on_exhaust(d.pop("on_exhaust", UNSET))

        def _parse_per(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        per = _parse_per(d.pop("per", UNSET))

        def _parse_pool(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pool = _parse_pool(d.pop("pool", UNSET))

        limit_view = cls(
            amount=amount,
            metric=metric,
            downgrade_to=downgrade_to,
            on_exhaust=on_exhaust,
            per=per,
            pool=pool,
        )

        limit_view.additional_properties = d
        return limit_view

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
