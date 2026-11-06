from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.config_input_limit_type_6_admission import ConfigInputLimitType6Admission
from ..models.config_input_limit_type_6_on_exhaust import ConfigInputLimitType6OnExhaust
from ..models.config_input_limit_type_6_on_exhaustion import ConfigInputLimitType6OnExhaustion
from ..models.config_input_limit_type_6_per import ConfigInputLimitType6Per
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigInputLimitType6")


@_attrs_define(repr=False)
class ConfigInputLimitType6:
    """
    Attributes:
        budget (int):
        per (ConfigInputLimitType6Per):
        pool (str | Unset):
        on_exhaust (ConfigInputLimitType6OnExhaust | Unset):
        downgrade_to (str | Unset):
        admission (ConfigInputLimitType6Admission | Unset): Omitted means exact; authored presence is retained in
            readback.
        on_exhaustion (ConfigInputLimitType6OnExhaustion | Unset): In-flight behavior; omitted means finish-unit.
            Distinct from admission-time on_exhaust.
    """

    budget: int
    per: ConfigInputLimitType6Per
    pool: str | Unset = UNSET
    on_exhaust: ConfigInputLimitType6OnExhaust | Unset = UNSET
    downgrade_to: str | Unset = UNSET
    admission: ConfigInputLimitType6Admission | Unset = UNSET
    on_exhaustion: ConfigInputLimitType6OnExhaustion | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        budget = self.budget

        per = self.per.value

        pool = self.pool

        on_exhaust: str | Unset = UNSET
        if not isinstance(self.on_exhaust, Unset):
            on_exhaust = self.on_exhaust.value

        downgrade_to = self.downgrade_to

        admission: str | Unset = UNSET
        if not isinstance(self.admission, Unset):
            admission = self.admission.value

        on_exhaustion: str | Unset = UNSET
        if not isinstance(self.on_exhaustion, Unset):
            on_exhaustion = self.on_exhaustion.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "budget": budget,
                "per": per,
            }
        )
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
        budget = d.pop("budget")

        per = ConfigInputLimitType6Per(d.pop("per"))

        pool = d.pop("pool", UNSET)

        _on_exhaust = d.pop("on_exhaust", UNSET)
        on_exhaust: ConfigInputLimitType6OnExhaust | Unset
        if isinstance(_on_exhaust, Unset):
            on_exhaust = UNSET
        else:
            on_exhaust = ConfigInputLimitType6OnExhaust(_on_exhaust)

        downgrade_to = d.pop("downgrade_to", UNSET)

        _admission = d.pop("admission", UNSET)
        admission: ConfigInputLimitType6Admission | Unset
        if isinstance(_admission, Unset):
            admission = UNSET
        else:
            admission = ConfigInputLimitType6Admission(_admission)

        _on_exhaustion = d.pop("on_exhaustion", UNSET)
        on_exhaustion: ConfigInputLimitType6OnExhaustion | Unset
        if isinstance(_on_exhaustion, Unset):
            on_exhaustion = UNSET
        else:
            on_exhaustion = ConfigInputLimitType6OnExhaustion(_on_exhaustion)

        if d:
            raise ValueError("Unexpected fields for ConfigInputLimitType6")
        config_input_limit_type_6 = cls(
            budget=budget,
            per=per,
            pool=pool,
            on_exhaust=on_exhaust,
            downgrade_to=downgrade_to,
            admission=admission,
            on_exhaustion=on_exhaustion,
        )

        return config_input_limit_type_6
