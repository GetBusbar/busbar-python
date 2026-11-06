from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ledger_migration_marker import LedgerMigrationMarker


T = TypeVar("T", bound="LedgerMigration")


@_attrs_define(repr=False)
class LedgerMigration:
    """`GET /ledger/migration`: whether this deployment has migrated, and the marker if it has.
    `migrated` is a field of its own rather than inferred from a null marker.

        Attributes:
            migrated (bool):
            marker (LedgerMigrationMarker | None):
    """

    migrated: bool
    marker: LedgerMigrationMarker | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ledger_migration_marker import LedgerMigrationMarker  # noqa: PLC0415

        migrated = self.migrated

        marker: dict[str, Any] | None
        if isinstance(self.marker, LedgerMigrationMarker):
            marker = self.marker.to_dict()
        else:
            marker = self.marker

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "migrated": migrated,
                "marker": marker,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ledger_migration_marker import LedgerMigrationMarker  # noqa: PLC0415

        d = dict(src_dict)
        migrated = d.pop("migrated")

        def _parse_marker(data: object) -> LedgerMigrationMarker | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                marker_type_0 = LedgerMigrationMarker.from_dict(data)

                return marker_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid value for marker")

        marker = _parse_marker(d.pop("marker"))

        ledger_migration = cls(
            migrated=migrated,
            marker=marker,
        )

        ledger_migration.additional_properties = d
        return ledger_migration

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
