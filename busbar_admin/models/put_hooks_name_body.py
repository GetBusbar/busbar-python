from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.put_hooks_name_body_config import PutHooksNameBodyConfig


T = TypeVar("T", bound="PutHooksNameBody")


@_attrs_define
class PutHooksNameBody:
    """
    Attributes:
        config (PutHooksNameBodyConfig): A `hooks:` entry, as JSON. The accepted shape is the config file's own,
            documented in the configuration reference; it is not restated here because several of its types parse a wire
            shape that does not match their field layout.
    """

    config: PutHooksNameBodyConfig

    def to_dict(self) -> dict[str, Any]:
        config = self.config.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "config": config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_hooks_name_body_config import PutHooksNameBodyConfig

        d = dict(src_dict)
        config = PutHooksNameBodyConfig.from_dict(d.pop("config"))

        put_hooks_name_body = cls(
            config=config,
        )

        return put_hooks_name_body
