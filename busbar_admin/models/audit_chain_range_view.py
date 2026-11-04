from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.audit_chain_record_view import AuditChainRecordView
    from ..models.audit_chain_signed_head import AuditChainSignedHead


T = TypeVar("T", bound="AuditChainRangeView")


@_attrs_define(repr=False)
class AuditChainRangeView:
    """`GET /audit/range`: records by position, `from` through `to` inclusive, each carrying every
    field its digest was taken over, plus the head this node published at or before `to`.

        Attributes:
            algorithm (str):
            anchor (AuditChainSignedHead | None): The head published at or before `to`, or null when none was.
            from_ (int):
            recipe (str):
            records (list[AuditChainRecordView]):
            signature_domain (str):
            to (int):
    """

    algorithm: str
    anchor: AuditChainSignedHead | None
    from_: int
    recipe: str
    records: list[AuditChainRecordView]
    signature_domain: str
    to: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.audit_chain_signed_head import AuditChainSignedHead  # noqa: PLC0415

        algorithm = self.algorithm

        anchor: dict[str, Any] | None
        if isinstance(self.anchor, AuditChainSignedHead):
            anchor = self.anchor.to_dict()
        else:
            anchor = self.anchor

        from_ = self.from_

        recipe = self.recipe

        records = []
        for records_item_data in self.records:
            records_item = records_item_data.to_dict()
            records.append(records_item)

        signature_domain = self.signature_domain

        to = self.to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "algorithm": algorithm,
                "anchor": anchor,
                "from": from_,
                "recipe": recipe,
                "records": records,
                "signature_domain": signature_domain,
                "to": to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_chain_record_view import AuditChainRecordView  # noqa: PLC0415
        from ..models.audit_chain_signed_head import AuditChainSignedHead  # noqa: PLC0415

        d = dict(src_dict)
        algorithm = d.pop("algorithm")

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

        from_ = d.pop("from")

        recipe = d.pop("recipe")

        records = []
        _records = d.pop("records")
        for records_item_data in _records:
            records_item = AuditChainRecordView.from_dict(records_item_data)

            records.append(records_item)

        signature_domain = d.pop("signature_domain")

        to = d.pop("to")

        audit_chain_range_view = cls(
            algorithm=algorithm,
            anchor=anchor,
            from_=from_,
            recipe=recipe,
            records=records,
            signature_domain=signature_domain,
            to=to,
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
