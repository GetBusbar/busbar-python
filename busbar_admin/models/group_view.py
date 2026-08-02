from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.limit_view import LimitView


T = TypeVar("T", bound="GroupView")


@_attrs_define
class GroupView:
    """A group definition in the registry read (`GET /api/v1/admin/groups`,
    `GET /api/v1/admin/groups/{name}`) — the limit-tree read surface. Projects the `groups:` config
    entry faithfully (parent chain, enabled freeze flag, the ordered limits, the `child_default`
    budget template for auto-provisioned children), never a secret. This is the READ shape; the
    WRITE verbs accept a `GroupCfg` verbatim (paste a config.yaml group block). Additive-only.

        Attributes:
            enabled (bool): `false` FREEZES the group (every request charging through it is rejected; history kept).
            limits (list[LimitView]): The group's own limits, enforced together (AND). Order preserved from config.
            name (str):
            child_default (list[LimitView] | None | Unset): The limit template stamped onto children auto-provisioned under
                this group (e.g. a
                `user:<sub>` leaf on first self-mint). Skipped from the body when the group sets none.
            parent (None | str | Unset): The parent group whose limits this one is ANDed under (the enforcement chain).
                `None` = a
                root group. Skipped from the body when absent.
    """

    enabled: bool
    limits: list[LimitView]
    name: str
    child_default: list[LimitView] | None | Unset = UNSET
    parent: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        limits = []
        for limits_item_data in self.limits:
            limits_item = limits_item_data.to_dict()
            limits.append(limits_item)

        name = self.name

        child_default: list[dict[str, Any]] | None | Unset
        if isinstance(self.child_default, Unset):
            child_default = UNSET
        elif isinstance(self.child_default, list):
            child_default = []
            for child_default_type_0_item_data in self.child_default:
                child_default_type_0_item = child_default_type_0_item_data.to_dict()
                child_default.append(child_default_type_0_item)

        else:
            child_default = self.child_default

        parent: None | str | Unset
        if isinstance(self.parent, Unset):
            parent = UNSET
        else:
            parent = self.parent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "limits": limits,
                "name": name,
            }
        )
        if child_default is not UNSET:
            field_dict["child_default"] = child_default
        if parent is not UNSET:
            field_dict["parent"] = parent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.limit_view import LimitView

        d = dict(src_dict)
        enabled = d.pop("enabled")

        limits = []
        _limits = d.pop("limits")
        for limits_item_data in _limits:
            limits_item = LimitView.from_dict(limits_item_data)

            limits.append(limits_item)

        name = d.pop("name")

        def _parse_child_default(data: object) -> list[LimitView] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                child_default_type_0 = []
                _child_default_type_0 = data
                for child_default_type_0_item_data in _child_default_type_0:
                    child_default_type_0_item = LimitView.from_dict(child_default_type_0_item_data)

                    child_default_type_0.append(child_default_type_0_item)

                return child_default_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LimitView] | None | Unset, data)

        child_default = _parse_child_default(d.pop("child_default", UNSET))

        def _parse_parent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent = _parse_parent(d.pop("parent", UNSET))

        group_view = cls(
            enabled=enabled,
            limits=limits,
            name=name,
            child_default=child_default,
            parent=parent,
        )

        group_view.additional_properties = d
        return group_view

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
