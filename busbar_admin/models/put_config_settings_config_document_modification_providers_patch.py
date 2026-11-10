from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_config_settings_config_document_modification_providers_patch_set import (
        PutConfigSettingsConfigDocumentModificationProvidersPatchSet,
    )


T = TypeVar("T", bound="PutConfigSettingsConfigDocumentModificationProvidersPatch")


@_attrs_define(repr=False)
class PutConfigSettingsConfigDocumentModificationProvidersPatch:
    """Edits providers.yaml through its boot grammar in the same Store transaction. Paths start with catalog entry names.
    Deployment overrides that shadow an edit are refused.

        Attributes:
            set_ (PutConfigSettingsConfigDocumentModificationProvidersPatchSet | Unset):
            remove (list[str] | Unset):
    """

    set_: PutConfigSettingsConfigDocumentModificationProvidersPatchSet | Unset = UNSET
    remove: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        set_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.set_, Unset):
            set_ = self.set_.to_dict()

        remove: list[str] | Unset = UNSET
        if not isinstance(self.remove, Unset):
            remove = self.remove

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if set_ is not UNSET:
            field_dict["set"] = set_
        if remove is not UNSET:
            field_dict["remove"] = remove

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_config_settings_config_document_modification_providers_patch_set import (
            PutConfigSettingsConfigDocumentModificationProvidersPatchSet,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _set_ = d.pop("set", UNSET)
        set_: PutConfigSettingsConfigDocumentModificationProvidersPatchSet | Unset
        if isinstance(_set_, Unset):
            set_ = UNSET
        else:
            set_ = PutConfigSettingsConfigDocumentModificationProvidersPatchSet.from_dict(_set_)

        remove = cast(list[str], d.pop("remove", UNSET))

        if d:
            raise ValueError("Unexpected fields for PutConfigSettingsConfigDocumentModificationProvidersPatch")
        put_config_settings_config_document_modification_providers_patch = cls(
            set_=set_,
            remove=remove,
        )

        return put_config_settings_config_document_modification_providers_patch
