from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PendingRestartRemovalView")


@_attrs_define(repr=False)
class PendingRestartRemovalView:
    """Restart metadata returned when a stored removal cannot take full effect in this process.

    Attributes:
        note (None | str): The operator-facing explanation of the pending restart.
        reload_to_apply (list[str]): The boot-bound changes that require a process restart to take effect.
    """

    note: None | str
    reload_to_apply: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        note: None | str
        note = self.note

        reload_to_apply = self.reload_to_apply

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "note": note,
                "reload_to_apply": reload_to_apply,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        note = _parse_note(d.pop("note"))

        reload_to_apply = cast(list[str], d.pop("reload_to_apply"))

        pending_restart_removal_view = cls(
            note=note,
            reload_to_apply=reload_to_apply,
        )

        pending_restart_removal_view.additional_properties = d
        return pending_restart_removal_view

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
