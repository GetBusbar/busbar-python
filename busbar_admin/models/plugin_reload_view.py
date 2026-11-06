from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.plugin_view import PluginView


T = TypeVar("T", bound="PluginReloadView")


@_attrs_define(repr=False)
class PluginReloadView:
    """The result of re-scanning the plugins directory (`POST /api/v1/admin/plugins/reload`): the
    current dynamic-library inventory, each with its ABI-validity. Reconciles the reported set to the
    folder (the folder is the source of truth), exactly as `config/reload` reconciles config to disk.
    A store change still applies on the next store (re)load, not as a hot swap.

        Attributes:
            plugins (list[PluginView]): The dynamic-library plugins now present in the directory, sorted by filename.
            note (str): A human note on when a store change actually takes effect.
    """

    plugins: list[PluginView]
    note: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plugins = []
        for plugins_item_data in self.plugins:
            plugins_item = plugins_item_data.to_dict()
            plugins.append(plugins_item)

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plugins": plugins,
                "note": note,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plugin_view import PluginView  # noqa: PLC0415

        d = dict(src_dict)
        plugins = []
        _plugins = d.pop("plugins")
        for plugins_item_data in _plugins:
            plugins_item = PluginView.from_dict(plugins_item_data)

            plugins.append(plugins_item)

        note = d.pop("note")

        plugin_reload_view = cls(
            plugins=plugins,
            note=note,
        )

        plugin_reload_view.additional_properties = d
        return plugin_reload_view

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
