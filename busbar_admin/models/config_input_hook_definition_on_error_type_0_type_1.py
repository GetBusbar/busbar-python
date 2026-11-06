from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ConfigInputHookDefinitionOnErrorType0Type1")


@_attrs_define(repr=False)
class ConfigInputHookDefinitionOnErrorType0Type1:
    """
    Attributes:
        hook (str):
    """

    hook: str

    def to_dict(self) -> dict[str, Any]:
        hook = self.hook

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "hook": hook,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hook = d.pop("hook")

        if d:
            raise ValueError("Unexpected fields for ConfigInputHookDefinitionOnErrorType0Type1")
        config_input_hook_definition_on_error_type_0_type_1 = cls(
            hook=hook,
        )

        return config_input_hook_definition_on_error_type_0_type_1
