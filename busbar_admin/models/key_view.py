from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KeyView")


@_attrs_define
class KeyView:
    """Virtual-key metadata — the `key_meta()` shape returned by `GET /keys/{id}`, `PATCH /keys/{id}`,
    and as each item of `GET /keys`. Never the secret or its hash.

        Attributes:
            allowed_pools (list[str]):
            budget_period (str):
            created_at (int):
            enabled (bool):
            id (str):
            max_budget_cents (int | None):
            name (str):
            rpm_limit (int | None):
            tpm_limit (int | None):
    """

    allowed_pools: list[str]
    budget_period: str
    created_at: int
    enabled: bool
    id: str
    max_budget_cents: int | None
    name: str
    rpm_limit: int | None
    tpm_limit: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_pools = self.allowed_pools

        budget_period = self.budget_period

        created_at = self.created_at

        enabled = self.enabled

        id = self.id

        max_budget_cents: int | None
        max_budget_cents = self.max_budget_cents

        name = self.name

        rpm_limit: int | None
        rpm_limit = self.rpm_limit

        tpm_limit: int | None
        tpm_limit = self.tpm_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowed_pools": allowed_pools,
                "budget_period": budget_period,
                "created_at": created_at,
                "enabled": enabled,
                "id": id,
                "max_budget_cents": max_budget_cents,
                "name": name,
                "rpm_limit": rpm_limit,
                "tpm_limit": tpm_limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed_pools = cast(list[str], d.pop("allowed_pools"))

        budget_period = d.pop("budget_period")

        created_at = d.pop("created_at")

        enabled = d.pop("enabled")

        id = d.pop("id")

        def _parse_max_budget_cents(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_budget_cents = _parse_max_budget_cents(d.pop("max_budget_cents"))

        name = d.pop("name")

        def _parse_rpm_limit(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        rpm_limit = _parse_rpm_limit(d.pop("rpm_limit"))

        def _parse_tpm_limit(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        tpm_limit = _parse_tpm_limit(d.pop("tpm_limit"))

        key_view = cls(
            allowed_pools=allowed_pools,
            budget_period=budget_period,
            created_at=created_at,
            enabled=enabled,
            id=id,
            max_budget_cents=max_budget_cents,
            name=name,
            rpm_limit=rpm_limit,
            tpm_limit=tpm_limit,
        )

        key_view.additional_properties = d
        return key_view

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
