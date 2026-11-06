from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.plane_facts_class import PlaneFactsClass
    from ..models.plane_facts_metric import PlaneFactsMetric
    from ..models.plane_facts_served import PlaneFactsServed


T = TypeVar("T", bound="PlaneFactsView")


@_attrs_define(repr=False)
class PlaneFactsView:
    """`GET /plane-facts`: what a plane this node serves declares about itself.

    Attributes:
        plane (str): The plane's registry key.
        fallback (bool): Whether it is the fallback catch-all plane.
        config_section (str): The config section whose presence declares the plane.
        owned_config_sections (list[str]):
        scope_kinds (list[str]):
        subject_noun (str):
        admin_noun (str):
        audit_kind (str):
        billable_classes (list[PlaneFactsClass]):
        fee_units (list[str]):
        metric_families (list[PlaneFactsMetric]):
        served_op_classes (list[PlaneFactsServed]):
        record_kinds (list[str]): The plane-record kinds the plane keeps; `POST /plane-record-write` writes only these.
    """

    plane: str
    fallback: bool
    config_section: str
    owned_config_sections: list[str]
    scope_kinds: list[str]
    subject_noun: str
    admin_noun: str
    audit_kind: str
    billable_classes: list[PlaneFactsClass]
    fee_units: list[str]
    metric_families: list[PlaneFactsMetric]
    served_op_classes: list[PlaneFactsServed]
    record_kinds: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plane = self.plane

        fallback = self.fallback

        config_section = self.config_section

        owned_config_sections = self.owned_config_sections

        scope_kinds = self.scope_kinds

        subject_noun = self.subject_noun

        admin_noun = self.admin_noun

        audit_kind = self.audit_kind

        billable_classes = []
        for billable_classes_item_data in self.billable_classes:
            billable_classes_item = billable_classes_item_data.to_dict()
            billable_classes.append(billable_classes_item)

        fee_units = self.fee_units

        metric_families = []
        for metric_families_item_data in self.metric_families:
            metric_families_item = metric_families_item_data.to_dict()
            metric_families.append(metric_families_item)

        served_op_classes = []
        for served_op_classes_item_data in self.served_op_classes:
            served_op_classes_item = served_op_classes_item_data.to_dict()
            served_op_classes.append(served_op_classes_item)

        record_kinds = self.record_kinds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plane": plane,
                "fallback": fallback,
                "config_section": config_section,
                "owned_config_sections": owned_config_sections,
                "scope_kinds": scope_kinds,
                "subject_noun": subject_noun,
                "admin_noun": admin_noun,
                "audit_kind": audit_kind,
                "billable_classes": billable_classes,
                "fee_units": fee_units,
                "metric_families": metric_families,
                "served_op_classes": served_op_classes,
                "record_kinds": record_kinds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plane_facts_class import PlaneFactsClass  # noqa: PLC0415
        from ..models.plane_facts_metric import PlaneFactsMetric  # noqa: PLC0415
        from ..models.plane_facts_served import PlaneFactsServed  # noqa: PLC0415

        d = dict(src_dict)
        plane = d.pop("plane")

        fallback = d.pop("fallback")

        config_section = d.pop("config_section")

        owned_config_sections = cast(list[str], d.pop("owned_config_sections"))

        scope_kinds = cast(list[str], d.pop("scope_kinds"))

        subject_noun = d.pop("subject_noun")

        admin_noun = d.pop("admin_noun")

        audit_kind = d.pop("audit_kind")

        billable_classes = []
        _billable_classes = d.pop("billable_classes")
        for billable_classes_item_data in _billable_classes:
            billable_classes_item = PlaneFactsClass.from_dict(billable_classes_item_data)

            billable_classes.append(billable_classes_item)

        fee_units = cast(list[str], d.pop("fee_units"))

        metric_families = []
        _metric_families = d.pop("metric_families")
        for metric_families_item_data in _metric_families:
            metric_families_item = PlaneFactsMetric.from_dict(metric_families_item_data)

            metric_families.append(metric_families_item)

        served_op_classes = []
        _served_op_classes = d.pop("served_op_classes")
        for served_op_classes_item_data in _served_op_classes:
            served_op_classes_item = PlaneFactsServed.from_dict(served_op_classes_item_data)

            served_op_classes.append(served_op_classes_item)

        record_kinds = cast(list[str], d.pop("record_kinds"))

        plane_facts_view = cls(
            plane=plane,
            fallback=fallback,
            config_section=config_section,
            owned_config_sections=owned_config_sections,
            scope_kinds=scope_kinds,
            subject_noun=subject_noun,
            admin_noun=admin_noun,
            audit_kind=audit_kind,
            billable_classes=billable_classes,
            fee_units=fee_units,
            metric_families=metric_families,
            served_op_classes=served_op_classes,
            record_kinds=record_kinds,
        )

        plane_facts_view.additional_properties = d
        return plane_facts_view

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
