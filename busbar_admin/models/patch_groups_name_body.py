from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.patch_groups_name_body_clear_item import PatchGroupsNameBodyClearItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_input_child_default import ConfigInputChildDefault
    from ..models.config_input_limit_type_0 import ConfigInputLimitType0
    from ..models.config_input_limit_type_1 import ConfigInputLimitType1
    from ..models.config_input_limit_type_2 import ConfigInputLimitType2
    from ..models.config_input_limit_type_3 import ConfigInputLimitType3
    from ..models.config_input_limit_type_4 import ConfigInputLimitType4
    from ..models.config_input_limit_type_5 import ConfigInputLimitType5
    from ..models.config_input_limit_type_6 import ConfigInputLimitType6
    from ..models.config_input_limit_type_7 import ConfigInputLimitType7


T = TypeVar("T", bound="PatchGroupsNameBody")


@_attrs_define(repr=False)
class PatchGroupsNameBody:
    """Omitted and null legacy fields preserve their current value. Non-null limits and child_default replace the entire
    value. clear explicitly removes parent or child_default; do not also set that field. An empty child_default is a
    present empty template, not removal.

        Attributes:
            parent (None | str | Unset):
            enabled (bool | None | Unset):
            limits (list[ConfigInputLimitType0 | ConfigInputLimitType1 | ConfigInputLimitType2 | ConfigInputLimitType3 |
                ConfigInputLimitType4 | ConfigInputLimitType5 | ConfigInputLimitType6 | ConfigInputLimitType7] | None | Unset):
            child_default (ConfigInputChildDefault | None | Unset):
            clear (list[PatchGroupsNameBodyClearItem] | Unset):
    """

    parent: None | str | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    limits: (
        list[
            ConfigInputLimitType0
            | ConfigInputLimitType1
            | ConfigInputLimitType2
            | ConfigInputLimitType3
            | ConfigInputLimitType4
            | ConfigInputLimitType5
            | ConfigInputLimitType6
            | ConfigInputLimitType7
        ]
        | None
        | Unset
    ) = UNSET
    child_default: ConfigInputChildDefault | None | Unset = UNSET
    clear: list[PatchGroupsNameBodyClearItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.config_input_child_default import ConfigInputChildDefault  # noqa: PLC0415
        from ..models.config_input_limit_type_0 import ConfigInputLimitType0  # noqa: PLC0415
        from ..models.config_input_limit_type_1 import ConfigInputLimitType1  # noqa: PLC0415
        from ..models.config_input_limit_type_2 import ConfigInputLimitType2  # noqa: PLC0415
        from ..models.config_input_limit_type_3 import ConfigInputLimitType3  # noqa: PLC0415
        from ..models.config_input_limit_type_4 import ConfigInputLimitType4  # noqa: PLC0415
        from ..models.config_input_limit_type_5 import ConfigInputLimitType5  # noqa: PLC0415
        from ..models.config_input_limit_type_6 import ConfigInputLimitType6  # noqa: PLC0415

        parent: None | str | Unset
        if isinstance(self.parent, Unset):
            parent = UNSET
        else:
            parent = self.parent

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
                limits_type_0_item: dict[str, Any]
                if isinstance(limits_type_0_item_data, ConfigInputLimitType0):
                    limits_type_0_item = limits_type_0_item_data.to_dict()
                elif isinstance(limits_type_0_item_data, ConfigInputLimitType1):
                    limits_type_0_item = limits_type_0_item_data.to_dict()
                elif isinstance(limits_type_0_item_data, ConfigInputLimitType2):
                    limits_type_0_item = limits_type_0_item_data.to_dict()
                elif isinstance(limits_type_0_item_data, ConfigInputLimitType3):
                    limits_type_0_item = limits_type_0_item_data.to_dict()
                elif isinstance(limits_type_0_item_data, ConfigInputLimitType4):
                    limits_type_0_item = limits_type_0_item_data.to_dict()
                elif isinstance(limits_type_0_item_data, ConfigInputLimitType5):
                    limits_type_0_item = limits_type_0_item_data.to_dict()
                elif isinstance(limits_type_0_item_data, ConfigInputLimitType6):
                    limits_type_0_item = limits_type_0_item_data.to_dict()
                else:
                    limits_type_0_item = limits_type_0_item_data.to_dict()

                limits.append(limits_type_0_item)

        else:
            limits = self.limits

        child_default: dict[str, Any] | None | Unset
        if isinstance(self.child_default, Unset):
            child_default = UNSET
        elif isinstance(self.child_default, ConfigInputChildDefault):
            child_default = self.child_default.to_dict()
        else:
            child_default = self.child_default

        clear: list[str] | Unset = UNSET
        if not isinstance(self.clear, Unset):
            clear = []
            for clear_item_data in self.clear:
                clear_item = clear_item_data.value
                clear.append(clear_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if parent is not UNSET:
            field_dict["parent"] = parent
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if limits is not UNSET:
            field_dict["limits"] = limits
        if child_default is not UNSET:
            field_dict["child_default"] = child_default
        if clear is not UNSET:
            field_dict["clear"] = clear

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_input_child_default import ConfigInputChildDefault  # noqa: PLC0415
        from ..models.config_input_limit_type_0 import ConfigInputLimitType0  # noqa: PLC0415
        from ..models.config_input_limit_type_1 import ConfigInputLimitType1  # noqa: PLC0415
        from ..models.config_input_limit_type_2 import ConfigInputLimitType2  # noqa: PLC0415
        from ..models.config_input_limit_type_3 import ConfigInputLimitType3  # noqa: PLC0415
        from ..models.config_input_limit_type_4 import ConfigInputLimitType4  # noqa: PLC0415
        from ..models.config_input_limit_type_5 import ConfigInputLimitType5  # noqa: PLC0415
        from ..models.config_input_limit_type_6 import ConfigInputLimitType6  # noqa: PLC0415
        from ..models.config_input_limit_type_7 import ConfigInputLimitType7  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_parent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent = _parse_parent(d.pop("parent", UNSET))

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_limits(
            data: object,
        ) -> (
            list[
                ConfigInputLimitType0
                | ConfigInputLimitType1
                | ConfigInputLimitType2
                | ConfigInputLimitType3
                | ConfigInputLimitType4
                | ConfigInputLimitType5
                | ConfigInputLimitType6
                | ConfigInputLimitType7
            ]
            | None
            | Unset
        ):
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

                    def _parse_limits_type_0_item(
                        data: object,
                    ) -> (
                        ConfigInputLimitType0
                        | ConfigInputLimitType1
                        | ConfigInputLimitType2
                        | ConfigInputLimitType3
                        | ConfigInputLimitType4
                        | ConfigInputLimitType5
                        | ConfigInputLimitType6
                        | ConfigInputLimitType7
                    ):
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_config_input_limit_type_0 = ConfigInputLimitType0.from_dict(data)

                            return componentsschemas_config_input_limit_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_config_input_limit_type_1 = ConfigInputLimitType1.from_dict(data)

                            return componentsschemas_config_input_limit_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_config_input_limit_type_2 = ConfigInputLimitType2.from_dict(data)

                            return componentsschemas_config_input_limit_type_2
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_config_input_limit_type_3 = ConfigInputLimitType3.from_dict(data)

                            return componentsschemas_config_input_limit_type_3
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_config_input_limit_type_4 = ConfigInputLimitType4.from_dict(data)

                            return componentsschemas_config_input_limit_type_4
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_config_input_limit_type_5 = ConfigInputLimitType5.from_dict(data)

                            return componentsschemas_config_input_limit_type_5
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_config_input_limit_type_6 = ConfigInputLimitType6.from_dict(data)

                            return componentsschemas_config_input_limit_type_6
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_config_input_limit_type_7 = ConfigInputLimitType7.from_dict(data)

                        return componentsschemas_config_input_limit_type_7
                        raise ValueError("Invalid value for limits_type_0_item")

                    limits_type_0_item = _parse_limits_type_0_item(limits_type_0_item_data)

                    limits_type_0.append(limits_type_0_item)

                return limits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid value for limits")

        limits = _parse_limits(d.pop("limits", UNSET))

        def _parse_child_default(data: object) -> ConfigInputChildDefault | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                child_default_type_0 = ConfigInputChildDefault.from_dict(data)

                return child_default_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid value for child_default")

        child_default = _parse_child_default(d.pop("child_default", UNSET))

        _clear = d.pop("clear", UNSET)
        clear: list[PatchGroupsNameBodyClearItem] | Unset = UNSET
        if _clear is not UNSET:
            clear = []
            for clear_item_data in _clear:
                clear_item = PatchGroupsNameBodyClearItem(clear_item_data)

                clear.append(clear_item)

        if d:
            raise ValueError("Unexpected fields for PatchGroupsNameBody")
        patch_groups_name_body = cls(
            parent=parent,
            enabled=enabled,
            limits=limits,
            child_default=child_default,
            clear=clear,
        )

        return patch_groups_name_body
