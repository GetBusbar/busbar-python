from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.config_input_hook import ConfigInputHook


T = TypeVar("T", bound="PostHooksBody")


@_attrs_define(repr=False)
class PostHooksBody:
    """
    Attributes:
        name (str): The hook name.
        config (ConfigInputHook): Admin hook POST/PUT input. module and phase are the canonical names; use phase:[stage]
            for a single stage. This differs from the deploy HookDefinition wrapper. Settings may contain hidden values and
            must never be reconstructed from HookView.
    """

    name: str
    config: ConfigInputHook
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
        from ..models.config_input_hook import ConfigInputHook  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        config = ConfigInputHook.from_dict(d.pop("config"))

        post_hooks_body = cls(
            name=name,
            config=config,
        )

        post_hooks_body.additional_properties = d
        return post_hooks_body

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
