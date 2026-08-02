from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.put_groups_name_body_config import PutGroupsNameBodyConfig


T = TypeVar("T", bound="PutGroupsNameBody")


@_attrs_define
class PutGroupsNameBody:
    """
    Attributes:
        config (PutGroupsNameBodyConfig): A `groups:` entry, as JSON. The accepted shape is the config file's own,
            documented in the configuration reference; it is not restated here because several of its types parse a wire
            shape that does not match their field layout.
    """

    config: PutGroupsNameBodyConfig

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
        from ..models.put_groups_name_body_config import PutGroupsNameBodyConfig

        d = dict(src_dict)
        config = PutGroupsNameBodyConfig.from_dict(d.pop("config"))

        put_groups_name_body = cls(
            config=config,
        )

        return put_groups_name_body
