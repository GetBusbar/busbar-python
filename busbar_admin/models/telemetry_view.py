from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dropped import Dropped
    from ..models.identity import Identity


T = TypeVar("T", bound="TelemetryView")


@_attrs_define(repr=False)
class TelemetryView:
    """Cumulative metrics for one process generation, bounded to 32 identities and 64 KiB.
    This is a process snapshot, not a time window or a history query.

        Attributes:
            process_boot_nonce (str): Random 128-bit process nonce. Stable across scrapes and configuration reloads.
            uptime_since_start_ms (str): Unsigned 64-bit integer as an exact decimal string.
            captured_at_unix_ms (str): Unsigned 64-bit integer as an exact decimal string.
            upper_bounds_ms (list[int | None]): Inclusive upper edge for each exclusive bin; final null means positive
                infinity.
            identities (list[Identity]):
            omitted_identities (str): Unsigned 64-bit integer as an exact decimal string.
            truncated (bool):
            dropped (Dropped):
    """

    process_boot_nonce: str
    uptime_since_start_ms: str
    captured_at_unix_ms: str
    upper_bounds_ms: list[int | None]
    identities: list[Identity]
    omitted_identities: str
    truncated: bool
    dropped: Dropped
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        process_boot_nonce = self.process_boot_nonce

        uptime_since_start_ms = self.uptime_since_start_ms

        captured_at_unix_ms = self.captured_at_unix_ms

        upper_bounds_ms = []
        for upper_bounds_ms_item_data in self.upper_bounds_ms:
            upper_bounds_ms_item: int | None
            upper_bounds_ms_item = upper_bounds_ms_item_data
            upper_bounds_ms.append(upper_bounds_ms_item)

        identities = []
        for identities_item_data in self.identities:
            identities_item = identities_item_data.to_dict()
            identities.append(identities_item)

        omitted_identities = self.omitted_identities

        truncated = self.truncated

        dropped = self.dropped.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "process_boot_nonce": process_boot_nonce,
                "uptime_since_start_ms": uptime_since_start_ms,
                "captured_at_unix_ms": captured_at_unix_ms,
                "upper_bounds_ms": upper_bounds_ms,
                "identities": identities,
                "omitted_identities": omitted_identities,
                "truncated": truncated,
                "dropped": dropped,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dropped import Dropped  # noqa: PLC0415
        from ..models.identity import Identity  # noqa: PLC0415

        d = dict(src_dict)
        process_boot_nonce = d.pop("process_boot_nonce")

        uptime_since_start_ms = d.pop("uptime_since_start_ms")

        captured_at_unix_ms = d.pop("captured_at_unix_ms")

        upper_bounds_ms = []
        _upper_bounds_ms = d.pop("upper_bounds_ms")
        for upper_bounds_ms_item_data in _upper_bounds_ms:

            def _parse_upper_bounds_ms_item(data: object) -> int | None:
                if data is None:
                    return data
                return cast(int | None, data)

            upper_bounds_ms_item = _parse_upper_bounds_ms_item(upper_bounds_ms_item_data)

            upper_bounds_ms.append(upper_bounds_ms_item)

        identities = []
        _identities = d.pop("identities")
        for identities_item_data in _identities:
            identities_item = Identity.from_dict(identities_item_data)

            identities.append(identities_item)

        omitted_identities = d.pop("omitted_identities")

        truncated = d.pop("truncated")

        dropped = Dropped.from_dict(d.pop("dropped"))

        telemetry_view = cls(
            process_boot_nonce=process_boot_nonce,
            uptime_since_start_ms=uptime_since_start_ms,
            captured_at_unix_ms=captured_at_unix_ms,
            upper_bounds_ms=upper_bounds_ms,
            identities=identities,
            omitted_identities=omitted_identities,
            truncated=truncated,
            dropped=dropped,
        )

        telemetry_view.additional_properties = d
        return telemetry_view

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
