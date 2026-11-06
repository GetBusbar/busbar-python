from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.audit_entry import AuditEntry


T = TypeVar("T", bound="AuditPageView")


@_attrs_define(repr=False)
class AuditPageView:
    """`GET /audit`: the cursor-paginated audit-log envelope (`{items, next_cursor}`, hand-rolled in the
    audit handler).

        Attributes:
            items (list[AuditEntry]):
            returned_from (None | str): Actual lowest/highest returned sequence, null for an empty page.
            returned_to (None | str):
            retained_from (None | str): Lowest/highest sequence in the unfiltered ring under the same lock as items.
            retained_to (None | str):
            retention_limit (str):
            semantics (str): `live_offset`: concurrent appends/evictions may duplicate or skip rows across pages.
            complete (bool): Always false: this live filtered inventory does not prove complete audit coverage.
            truncated (bool): More matching rows existed in this observation.
            next_cursor (None | str):
    """

    items: list[AuditEntry]
    returned_from: None | str
    returned_to: None | str
    retained_from: None | str
    retained_to: None | str
    retention_limit: str
    semantics: str
    complete: bool
    truncated: bool
    next_cursor: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        returned_from: None | str
        returned_from = self.returned_from

        returned_to: None | str
        returned_to = self.returned_to

        retained_from: None | str
        retained_from = self.retained_from

        retained_to: None | str
        retained_to = self.retained_to

        retention_limit = self.retention_limit

        semantics = self.semantics

        complete = self.complete

        truncated = self.truncated

        next_cursor: None | str
        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "returned_from": returned_from,
                "returned_to": returned_to,
                "retained_from": retained_from,
                "retained_to": retained_to,
                "retention_limit": retention_limit,
                "semantics": semantics,
                "complete": complete,
                "truncated": truncated,
                "next_cursor": next_cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_entry import AuditEntry  # noqa: PLC0415

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = AuditEntry.from_dict(items_item_data)

            items.append(items_item)

        def _parse_returned_from(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        returned_from = _parse_returned_from(d.pop("returned_from"))

        def _parse_returned_to(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        returned_to = _parse_returned_to(d.pop("returned_to"))

        def _parse_retained_from(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        retained_from = _parse_retained_from(d.pop("retained_from"))

        def _parse_retained_to(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        retained_to = _parse_retained_to(d.pop("retained_to"))

        retention_limit = d.pop("retention_limit")

        semantics = d.pop("semantics")

        complete = d.pop("complete")

        truncated = d.pop("truncated")

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        audit_page_view = cls(
            items=items,
            returned_from=returned_from,
            returned_to=returned_to,
            retained_from=retained_from,
            retained_to=retained_to,
            retention_limit=retention_limit,
            semantics=semantics,
            complete=complete,
            truncated=truncated,
            next_cursor=next_cursor,
        )

        audit_page_view.additional_properties = d
        return audit_page_view

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
