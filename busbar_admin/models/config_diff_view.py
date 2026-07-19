from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_diff_global_hooks import ConfigDiffGlobalHooks
    from ..models.config_diff_hooks import ConfigDiffHooks


T = TypeVar("T", bound="ConfigDiffView")


@_attrs_define
class ConfigDiffView:
    """`GET /config/diff` — structured hook-surface diff between two retained versions. `global_hooks` is
    present only when the global wiring differed between the two sides.

        Attributes:
            from_ (int):
            hooks (ConfigDiffHooks): The `hooks` object of a `GET /config/diff` — hook names added / removed / changed
                between the two
                versions.
            to (int):
            global_hooks (ConfigDiffGlobalHooks | None | Unset):
    """

    from_: int
    hooks: ConfigDiffHooks
    to: int
    global_hooks: ConfigDiffGlobalHooks | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.config_diff_global_hooks import ConfigDiffGlobalHooks

        from_ = self.from_

        hooks = self.hooks.to_dict()

        to = self.to

        global_hooks: dict[str, Any] | None | Unset
        if isinstance(self.global_hooks, Unset):
            global_hooks = UNSET
        elif isinstance(self.global_hooks, ConfigDiffGlobalHooks):
            global_hooks = self.global_hooks.to_dict()
        else:
            global_hooks = self.global_hooks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "hooks": hooks,
                "to": to,
            }
        )
        if global_hooks is not UNSET:
            field_dict["global_hooks"] = global_hooks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_diff_global_hooks import ConfigDiffGlobalHooks
        from ..models.config_diff_hooks import ConfigDiffHooks

        d = dict(src_dict)
        from_ = d.pop("from")

        hooks = ConfigDiffHooks.from_dict(d.pop("hooks"))

        to = d.pop("to")

        def _parse_global_hooks(data: object) -> ConfigDiffGlobalHooks | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                global_hooks_type_0 = ConfigDiffGlobalHooks.from_dict(data)

                return global_hooks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConfigDiffGlobalHooks | None | Unset, data)

        global_hooks = _parse_global_hooks(d.pop("global_hooks", UNSET))

        config_diff_view = cls(
            from_=from_,
            hooks=hooks,
            to=to,
            global_hooks=global_hooks,
        )

        config_diff_view.additional_properties = d
        return config_diff_view

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
