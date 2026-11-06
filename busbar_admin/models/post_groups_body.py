from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.config_input_group import ConfigInputGroup


T = TypeVar("T", bound="PostGroupsBody")


@_attrs_define(repr=False)
class PostGroupsBody:
    """
    Attributes:
        name (str): The group name.
        config (ConfigInputGroup): Complete authored GroupCfg. Null/absent parent and child_default mean absent on full
            replacement. An empty child_default object is a present empty template and stops ancestor-template lookup. PATCH
            has separate presence/clear semantics.
    """

    name: str
    config: ConfigInputGroup
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        config = self.config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "config": config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_input_group import ConfigInputGroup  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        config = ConfigInputGroup.from_dict(d.pop("config"))

        post_groups_body = cls(
            name=name,
            config=config,
        )

        post_groups_body.additional_properties = d
        return post_groups_body

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
