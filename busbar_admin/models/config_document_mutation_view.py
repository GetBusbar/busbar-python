from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_document_mutation_view_configuration import ConfigDocumentMutationViewConfiguration


T = TypeVar("T", bound="ConfigDocumentMutationView")


@_attrs_define(repr=False)
class ConfigDocumentMutationView:
    """
    Attributes:
        applied (bool):
        persisted (bool):
        config_version (int):
        configuration (ConfigDocumentMutationViewConfiguration): Sanitized installed configuration, bound to
            config_version/ETag. Configured values are not an acknowledgement of physical listener, Store, or asynchronous
            plugin activation.
        reload_to_apply (list[str] | Unset):
        note (str | Unset):
    """

    applied: bool
    persisted: bool
    config_version: int
    configuration: ConfigDocumentMutationViewConfiguration
    reload_to_apply: list[str] | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applied = self.applied

        persisted = self.persisted

        config_version = self.config_version

        configuration = self.configuration.to_dict()

        reload_to_apply: list[str] | Unset = UNSET
        if not isinstance(self.reload_to_apply, Unset):
            reload_to_apply = self.reload_to_apply

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applied": applied,
                "persisted": persisted,
                "config_version": config_version,
                "configuration": configuration,
            }
        )
        if reload_to_apply is not UNSET:
            field_dict["reload_to_apply"] = reload_to_apply
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_document_mutation_view_configuration import ConfigDocumentMutationViewConfiguration  # noqa: PLC0415

        d = dict(src_dict)
        applied = d.pop("applied")

        persisted = d.pop("persisted")

        config_version = d.pop("config_version")

        configuration = ConfigDocumentMutationViewConfiguration.from_dict(d.pop("configuration"))

        reload_to_apply = cast(list[str], d.pop("reload_to_apply", UNSET))

        note = d.pop("note", UNSET)

        config_document_mutation_view = cls(
            applied=applied,
            persisted=persisted,
            config_version=config_version,
            configuration=configuration,
            reload_to_apply=reload_to_apply,
            note=note,
        )

        config_document_mutation_view.additional_properties = d
        return config_document_mutation_view

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
