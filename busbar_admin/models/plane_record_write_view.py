from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PlaneRecordWriteView")


@_attrs_define(repr=False)
class PlaneRecordWriteView:
    """`POST /plane-record-write`'s answer: what was written, and when.

    Attributes:
        id (str):
        kind (str):
        parent (None | str):
        plane (str):
        terminal (bool):
        written_at (int): The arrival second the record was written at.
    """

    id: str
    kind: str
    parent: None | str
    plane: str
    terminal: bool
    written_at: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind = self.kind

        parent: None | str
        parent = self.parent

        plane = self.plane

        terminal = self.terminal

        written_at = self.written_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "parent": parent,
                "plane": plane,
                "terminal": terminal,
                "written_at": written_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        kind = d.pop("kind")

        def _parse_parent(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        parent = _parse_parent(d.pop("parent"))

        plane = d.pop("plane")

        terminal = d.pop("terminal")

        written_at = d.pop("written_at")

        plane_record_write_view = cls(
            id=id,
            kind=kind,
            parent=parent,
            plane=plane,
            terminal=terminal,
            written_at=written_at,
        )

        plane_record_write_view.additional_properties = d
        return plane_record_write_view

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
