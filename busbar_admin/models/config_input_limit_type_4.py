from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.config_input_limit_type_4_per import ConfigInputLimitType4Per
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigInputLimitType4")


@_attrs_define(repr=False)
class ConfigInputLimitType4:
    """
    Attributes:
        tokens_cache_read (int):
        per (ConfigInputLimitType4Per):
        pool (str | Unset):
    """

    tokens_cache_read: int
    per: ConfigInputLimitType4Per
    pool: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        tokens_cache_read = self.tokens_cache_read

        per = self.per.value

        pool = self.pool

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "tokens_cache_read": tokens_cache_read,
                "per": per,
            }
        )
        if pool is not UNSET:
            field_dict["pool"] = pool

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tokens_cache_read = d.pop("tokens_cache_read")

        per = ConfigInputLimitType4Per(d.pop("per"))

        pool = d.pop("pool", UNSET)

        if d:
            raise ValueError("Unexpected fields for ConfigInputLimitType4")
        config_input_limit_type_4 = cls(
            tokens_cache_read=tokens_cache_read,
            per=per,
            pool=pool,
        )

        return config_input_limit_type_4
