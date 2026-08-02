from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateKeyReq")


@_attrs_define
class UpdateKeyReq:
    """Partial update to an existing key. Keys are PURE AUTH (1.5.0, S1), so the mutable surface is
    auth-shaped only. Every field is optional; only the present ones change. The credential, name,
    allowed-pools, and labels are immutable here (rotate/recreate for those).

    `group` is THREE-STATE via serde double-option (`Option<Option<String>>`):
    - absent (`#[serde(default)]` -> outer `None`): leave the binding unchanged.
    - JSON `null` (`Some(None)`): UNBIND to no group (authed + unlimited).
    - a value (`Some(Some(name))`): REBIND to that group (must exist; mint-parity check).

    A single `Option<T>` could not tell absent from present-null, so a binding could never be
    cleared once set. `enabled` is a plain `Option<bool>` (a bool has no clear state). The 1.4.x
    cap fields (`rpm_limit`/`tpm_limit`/`max_budget_cents`) are GONE: limits live on the group.

        Attributes:
            enabled (bool | None | Unset):
            group (None | str | Unset): Rebind or UNBIND the key's group. Absent = unchanged; `null` = unbind. The double
                `Option`
                is what distinguishes those two, so the schema describes it as a nullable string.
    """

    enabled: bool | None | Unset = UNSET
    group: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        group: None | str | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if group is not UNSET:
            field_dict["group"] = group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group = _parse_group(d.pop("group", UNSET))

        update_key_req = cls(
            enabled=enabled,
            group=group,
        )

        return update_key_req
