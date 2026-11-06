from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.audit_chain_record_view import AuditChainRecordView
    from ..models.audit_chain_signed_head import AuditChainSignedHead
    from ..models.audit_range_gap_view import AuditRangeGapView
    from ..models.audit_retention_view import AuditRetentionView


T = TypeVar("T", bound="AuditChainRangeView")


@_attrs_define(repr=False)
class AuditChainRangeView:
    """`GET /audit/range`: records by position, `from` through `to` inclusive, each carrying every
    field its digest was taken over, plus the head this node published at or before `to`.

        Attributes:
            recipe (str):
            signature_domain (str):
            algorithm (str):
            from_ (int):
            to (int):
            anchor (AuditChainSignedHead | None): The head published at or before `to`, or null when none was.
            records (list[AuditChainRecordView]):
            snapshot_to (str): Fixed upper audit position captured on the first page; exact decimal string.
            semantics (str): `bounded_live_range`: upper bound is fixed, retention is live, no snapshot is retained.
            returned_from (None | str):
            returned_to (None | str):
            next_cursor (None | str): Round-trip with the original from/to. May be present even when records is empty.
            truncated (bool): There is more bounded scanning to do.
            complete (bool): True only on the last page when this traversal found every requested position.
            incomplete (bool): A prior or current page had missing/oversized journal data or an audit gap.
            gaps (list[AuditRangeGapView]):
            retention (AuditRetentionView):
            scanned_positions (str):
            scan_limit (str):
    """

    recipe: str
    signature_domain: str
    algorithm: str
    from_: int
    to: int
    anchor: AuditChainSignedHead | None
    records: list[AuditChainRecordView]
    snapshot_to: str
    semantics: str
    returned_from: None | str
    returned_to: None | str
    next_cursor: None | str
    truncated: bool
    complete: bool
    incomplete: bool
    gaps: list[AuditRangeGapView]
    retention: AuditRetentionView
    scanned_positions: str
    scan_limit: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.audit_chain_signed_head import AuditChainSignedHead  # noqa: PLC0415

        recipe = self.recipe

        signature_domain = self.signature_domain

        algorithm = self.algorithm

        from_ = self.from_

        to = self.to

        anchor: dict[str, Any] | None
        if isinstance(self.anchor, AuditChainSignedHead):
            anchor = self.anchor.to_dict()
        else:
            anchor = self.anchor

        records = []
        for records_item_data in self.records:
            records_item = records_item_data.to_dict()
            records.append(records_item)

        snapshot_to = self.snapshot_to

        semantics = self.semantics

        returned_from: None | str
        returned_from = self.returned_from

        returned_to: None | str
        returned_to = self.returned_to

        next_cursor: None | str
        next_cursor = self.next_cursor

        truncated = self.truncated

        complete = self.complete

        incomplete = self.incomplete

        gaps = []
        for gaps_item_data in self.gaps:
            gaps_item = gaps_item_data.to_dict()
            gaps.append(gaps_item)

        retention = self.retention.to_dict()

        scanned_positions = self.scanned_positions

        scan_limit = self.scan_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "recipe": recipe,
                "signature_domain": signature_domain,
                "algorithm": algorithm,
                "from": from_,
                "to": to,
                "anchor": anchor,
                "records": records,
                "snapshot_to": snapshot_to,
                "semantics": semantics,
                "returned_from": returned_from,
                "returned_to": returned_to,
                "next_cursor": next_cursor,
                "truncated": truncated,
                "complete": complete,
                "incomplete": incomplete,
                "gaps": gaps,
                "retention": retention,
                "scanned_positions": scanned_positions,
                "scan_limit": scan_limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_chain_record_view import AuditChainRecordView  # noqa: PLC0415
        from ..models.audit_chain_signed_head import AuditChainSignedHead  # noqa: PLC0415
        from ..models.audit_range_gap_view import AuditRangeGapView  # noqa: PLC0415
        from ..models.audit_retention_view import AuditRetentionView  # noqa: PLC0415

        d = dict(src_dict)
        recipe = d.pop("recipe")

        signature_domain = d.pop("signature_domain")

        algorithm = d.pop("algorithm")

        from_ = d.pop("from")

        to = d.pop("to")

        def _parse_anchor(data: object) -> AuditChainSignedHead | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                anchor_type_0 = AuditChainSignedHead.from_dict(data)

                return anchor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid value for anchor")

        anchor = _parse_anchor(d.pop("anchor"))

        records = []
        _records = d.pop("records")
        for records_item_data in _records:
            records_item = AuditChainRecordView.from_dict(records_item_data)

            records.append(records_item)

        snapshot_to = d.pop("snapshot_to")

        semantics = d.pop("semantics")

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

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        truncated = d.pop("truncated")

        complete = d.pop("complete")

        incomplete = d.pop("incomplete")

        gaps = []
        _gaps = d.pop("gaps")
        for gaps_item_data in _gaps:
            gaps_item = AuditRangeGapView.from_dict(gaps_item_data)

            gaps.append(gaps_item)

        retention = AuditRetentionView.from_dict(d.pop("retention"))

        scanned_positions = d.pop("scanned_positions")

        scan_limit = d.pop("scan_limit")

        audit_chain_range_view = cls(
            recipe=recipe,
            signature_domain=signature_domain,
            algorithm=algorithm,
            from_=from_,
            to=to,
            anchor=anchor,
            records=records,
            snapshot_to=snapshot_to,
            semantics=semantics,
            returned_from=returned_from,
            returned_to=returned_to,
            next_cursor=next_cursor,
            truncated=truncated,
            complete=complete,
            incomplete=incomplete,
            gaps=gaps,
            retention=retention,
            scanned_positions=scanned_positions,
            scan_limit=scan_limit,
        )

        audit_chain_range_view.additional_properties = d
        return audit_chain_range_view

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
