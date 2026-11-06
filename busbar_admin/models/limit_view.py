from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.limit_view_admission import LimitViewAdmission
from ..models.limit_view_on_exhaustion import LimitViewOnExhaustion
from ..types import UNSET, Unset

T = TypeVar("T", bound="LimitView")


@_attrs_define(repr=False)
class LimitView:
    """One limit inside a `GroupView`: an explicit `{ metric, amount, per, pool }` projection of a
    config `LimitCfg`. The config file's compact `{ budget: 3000, per: month }` form is
    deserialize-only sugar; the read API projects it explicitly so a consumer never has to know
    the metric is the map key. `per` is `None` only for `concurrent` (an instantaneous gauge, no
    window); `pool` is present only on a pool-scoped limit.

        Attributes:
            metric (str): One of `requests` | `tokens` | `budget` | `concurrent`.
            amount (int): The cap amount (requests/tokens/cents, or the in-flight gauge for `concurrent`).
            per (None | str | Unset): The accounting window: `minute` | `hour` | `day` | `month` | `total`. Absent for
                `concurrent`.
            pool (None | str | Unset): The pool scope: present when the limit carries `pool: <name>` (it accounts and
                enforces
                only that pool's traffic, per `(group, pool)`); absent for a group-wide limit.
            on_exhaust (None | str | Unset): The budget-exhaustion behavior: `block` or `downgrade`. Absent = block (the
                default).
            downgrade_to (None | str | Unset): Where `on_exhaust: downgrade` sends exhausted traffic. Present iff
                downgrading.
            admission (LimitViewAdmission | Unset): Authored budget admission policy: exact (default when absent) or
                estimate.
            on_exhaustion (LimitViewOnExhaustion | Unset): Authored in-flight exhaustion policy: finish-unit (default when
                absent) or cut-stream.
    """

    metric: str
    amount: int
    per: None | str | Unset = UNSET
    pool: None | str | Unset = UNSET
    on_exhaust: None | str | Unset = UNSET
    downgrade_to: None | str | Unset = UNSET
    admission: LimitViewAdmission | Unset = UNSET
    on_exhaustion: LimitViewOnExhaustion | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metric = self.metric

        amount = self.amount

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

        on_exhaust: None | str | Unset
        if isinstance(self.on_exhaust, Unset):
            on_exhaust = UNSET
        else:
            on_exhaust = self.on_exhaust

        downgrade_to: None | str | Unset
        if isinstance(self.downgrade_to, Unset):
            downgrade_to = UNSET
        else:
            downgrade_to = self.downgrade_to

        admission: str | Unset = UNSET
        if not isinstance(self.admission, Unset):
            admission = self.admission.value

        on_exhaustion: str | Unset = UNSET
        if not isinstance(self.on_exhaustion, Unset):
            on_exhaustion = self.on_exhaustion.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metric": metric,
                "amount": amount,
            }
        )
        if per is not UNSET:
            field_dict["per"] = per
        if pool is not UNSET:
            field_dict["pool"] = pool
        if on_exhaust is not UNSET:
            field_dict["on_exhaust"] = on_exhaust
        if downgrade_to is not UNSET:
            field_dict["downgrade_to"] = downgrade_to
        if admission is not UNSET:
            field_dict["admission"] = admission
        if on_exhaustion is not UNSET:
            field_dict["on_exhaustion"] = on_exhaustion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        metric = d.pop("metric")

        amount = d.pop("amount")

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

        def _parse_on_exhaust(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        on_exhaust = _parse_on_exhaust(d.pop("on_exhaust", UNSET))

        def _parse_downgrade_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        downgrade_to = _parse_downgrade_to(d.pop("downgrade_to", UNSET))

        _admission = d.pop("admission", UNSET)
        admission: LimitViewAdmission | Unset
        if isinstance(_admission, Unset):
            admission = UNSET
        else:
            admission = LimitViewAdmission(_admission)

        _on_exhaustion = d.pop("on_exhaustion", UNSET)
        on_exhaustion: LimitViewOnExhaustion | Unset
        if isinstance(_on_exhaustion, Unset):
            on_exhaustion = UNSET
        else:
            on_exhaustion = LimitViewOnExhaustion(_on_exhaustion)

        limit_view = cls(
            metric=metric,
            amount=amount,
            per=per,
            pool=pool,
            on_exhaust=on_exhaust,
            downgrade_to=downgrade_to,
            admission=admission,
            on_exhaustion=on_exhaustion,
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
