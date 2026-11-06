from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.config_input_limit_type_5_per import ConfigInputLimitType5Per
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigInputLimitType5")


@_attrs_define(repr=False)
class ConfigInputLimitType5:
    """
    Attributes:
        tokens_cache_write (int):
        per (ConfigInputLimitType5Per):
        pool (str | Unset):
    """

    tokens_cache_write: int
    per: ConfigInputLimitType5Per
    pool: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        tokens_cache_write = self.tokens_cache_write

        per = self.per.value

        pool = self.pool

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "tokens_cache_write": tokens_cache_write,
                "per": per,
            }
        )
        if pool is not UNSET:
            field_dict["pool"] = pool

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tokens_cache_write = d.pop("tokens_cache_write")

        per = ConfigInputLimitType5Per(d.pop("per"))

        pool = d.pop("pool", UNSET)

        if d:
            raise ValueError("Unexpected fields for ConfigInputLimitType5")
        config_input_limit_type_5 = cls(
            tokens_cache_write=tokens_cache_write,
            per=per,
            pool=pool,
        )

        return config_input_limit_type_5
