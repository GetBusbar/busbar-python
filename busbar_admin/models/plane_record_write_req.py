from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlaneRecordWriteReq")


@_attrs_define(repr=False)
class PlaneRecordWriteReq:
    """`POST /plane-record-write`: one plane record, upserted by `(kind, id)`.

    Attributes:
        body (Any): The record's row, stored as its JSON bytes and never decoded by the store.
        id (str): The record's identity within its kind.
        kind (str): The record kind.
        plane (str): The key of a plane this node serves.
        parent (None | str | Unset): The parent the record hangs off, for a child kind.
        terminal (bool | None | Unset): Whether retention may drop the record once it is old (default false).
    """

    body: Any
    id: str
    kind: str
    plane: str
    parent: None | str | Unset = UNSET
    terminal: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        id = self.id

        kind = self.kind

        plane = self.plane

        parent: None | str | Unset
        if isinstance(self.parent, Unset):
            parent = UNSET
        else:
            parent = self.parent

        terminal: bool | None | Unset
        if isinstance(self.terminal, Unset):
            terminal = UNSET
        else:
            terminal = self.terminal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
                "id": id,
                "kind": kind,
                "plane": plane,
            }
        )
        if parent is not UNSET:
            field_dict["parent"] = parent
        if terminal is not UNSET:
            field_dict["terminal"] = terminal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        body = d.pop("body")

        id = d.pop("id")

        kind = d.pop("kind")

        plane = d.pop("plane")

        def _parse_parent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent = _parse_parent(d.pop("parent", UNSET))

        def _parse_terminal(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        terminal = _parse_terminal(d.pop("terminal", UNSET))

        plane_record_write_req = cls(
            body=body,
            id=id,
            kind=kind,
            plane=plane,
            parent=parent,
            terminal=terminal,
        )

        plane_record_write_req.additional_properties = d
        return plane_record_write_req

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
