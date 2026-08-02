from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_groups_name_body_child_default import PatchGroupsNameBodyChildDefault
    from ..models.patch_groups_name_body_limits_type_0_item import PatchGroupsNameBodyLimitsType0Item


T = TypeVar("T", bound="PatchGroupsNameBody")


@_attrs_define
class PatchGroupsNameBody:
    """A partial update: only the fields present are changed. `limits` and `child_default` REPLACE their whole value when
    present.

        Attributes:
            child_default (PatchGroupsNameBodyChildDefault | Unset): A `child_default:` template. The accepted shape is the
                config file's own, documented in the configuration reference; it is not restated here because several of its
                types parse a wire shape that does not match their field layout.
            enabled (bool | None | Unset):
            limits (list[PatchGroupsNameBodyLimitsType0Item] | None | Unset):
            parent (None | str | Unset):
    """

    child_default: PatchGroupsNameBodyChildDefault | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    limits: list[PatchGroupsNameBodyLimitsType0Item] | None | Unset = UNSET
    parent: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        child_default: dict[str, Any] | Unset = UNSET
        if not isinstance(self.child_default, Unset):
            child_default = self.child_default.to_dict()

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        limits: list[dict[str, Any]] | None | Unset
        if isinstance(self.limits, Unset):
            limits = UNSET
        elif isinstance(self.limits, list):
            limits = []
            for limits_type_0_item_data in self.limits:
                limits_type_0_item = limits_type_0_item_data.to_dict()
                limits.append(limits_type_0_item)

        else:
            limits = self.limits

        parent: None | str | Unset
        if isinstance(self.parent, Unset):
            parent = UNSET
        else:
            parent = self.parent

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if child_default is not UNSET:
            field_dict["child_default"] = child_default
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if limits is not UNSET:
            field_dict["limits"] = limits
        if parent is not UNSET:
            field_dict["parent"] = parent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_groups_name_body_child_default import PatchGroupsNameBodyChildDefault
        from ..models.patch_groups_name_body_limits_type_0_item import PatchGroupsNameBodyLimitsType0Item

        d = dict(src_dict)
        _child_default = d.pop("child_default", UNSET)
        child_default: PatchGroupsNameBodyChildDefault | Unset
        if isinstance(_child_default, Unset):
            child_default = UNSET
        else:
            child_default = PatchGroupsNameBodyChildDefault.from_dict(_child_default)

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_limits(data: object) -> list[PatchGroupsNameBodyLimitsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                limits_type_0 = []
                _limits_type_0 = data
                for limits_type_0_item_data in _limits_type_0:
                    limits_type_0_item = PatchGroupsNameBodyLimitsType0Item.from_dict(limits_type_0_item_data)

                    limits_type_0.append(limits_type_0_item)

                return limits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PatchGroupsNameBodyLimitsType0Item] | None | Unset, data)

        limits = _parse_limits(d.pop("limits", UNSET))

        def _parse_parent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent = _parse_parent(d.pop("parent", UNSET))

        patch_groups_name_body = cls(
            child_default=child_default,
            enabled=enabled,
            limits=limits,
            parent=parent,
        )

        return patch_groups_name_body
