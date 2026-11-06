from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.config_input_limit_type_0_per import ConfigInputLimitType0Per
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigInputLimitType0")


@_attrs_define(repr=False)
class ConfigInputLimitType0:
    """
    Attributes:
        requests (int):
        per (ConfigInputLimitType0Per):
        pool (str | Unset):
    """

    requests: int
    per: ConfigInputLimitType0Per
    pool: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        requests = self.requests

        per = self.per.value

        pool = self.pool

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "requests": requests,
                "per": per,
            }
        )
        if pool is not UNSET:
            field_dict["pool"] = pool

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        requests = d.pop("requests")

        per = ConfigInputLimitType0Per(d.pop("per"))

        pool = d.pop("pool", UNSET)

        if d:
            raise ValueError("Unexpected fields for ConfigInputLimitType0")
        config_input_limit_type_0 = cls(
            requests=requests,
            per=per,
            pool=pool,
        )

        return config_input_limit_type_0
